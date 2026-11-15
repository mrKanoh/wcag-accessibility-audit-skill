# Mobile accessibility

Platform guidance for iOS, Android and the mobile web, plus code for SwiftUI, Jetpack Compose and React Native. Each snippet says whether it was compiled or checked against documentation.

## Contents

- [Mobile Accessibility](#mobile-accessibility)
  - [iOS (VoiceOver)](#ios-voiceover)
  - [Android (TalkBack)](#android-talkback)
  - [Web on mobile](#web-on-mobile)
- [Native Mobile — Code Examples](#native-mobile--code-examples)
  - [SwiftUI (iOS / iPadOS / macOS)](#swiftui-ios--ipados--macos)
  - [Jetpack Compose (Android)](#jetpack-compose-android)
- [React Native Accessibility](#react-native-accessibility)
  - [Core props](#core-props)
  - [Touch targets (WCAG 2.5.8 equivalent)](#touch-targets-wcag-258-equivalent)
  - [Dynamic Type (font scaling)](#dynamic-type-font-scaling)
  - [Reduce Motion](#reduce-motion)
  - [Focus management (screen transition)](#focus-management-screen-transition)

---

## Mobile Accessibility

### iOS (VoiceOver)
- Touch targets ≥ **44×44 pt**
- `accessibilityLabel`, `accessibilityHint`, `accessibilityTraits` set correctly
- Custom gestures must have single-tap alternatives
- Dynamic Type: respect user font size (`UIFontMetrics`)
- Reduce Motion: honor `UIAccessibility.isReduceMotionEnabled`
- Test in **Accessibility Inspector** (Xcode)

### Android (TalkBack)
- Touch targets ≥ **48×48 dp**
- `contentDescription` on non-text elements
- `android:labelFor` to link labels to inputs
- `importantForAccessibility="no"` on decorative views
- Support large font scale and high-contrast text
- Test with **Accessibility Scanner** app

### Web on mobile
- Respect `prefers-reduced-motion`, `prefers-contrast`, `prefers-color-scheme`
- Use `<input type="email|tel|number|url|search">` for correct keyboards
- `autocomplete` tokens (`email`, `name`, `street-address`, `postal-code`, `cc-number`…)
- Avoid hover-only affordances (no hover on touch)

---

## Native Mobile — Code Examples

### SwiftUI (iOS / iPadOS / macOS)

```swift
// Accessible custom card
struct CourseCard: View {
    let title: String
    let instructor: String
    let duration: String
    let isCompleted: Bool
    let onOpen: () -> Void

    var body: some View {
        // A real Button gives the control its action and the button trait; do not add .isButton to a view with no action.
        Button(action: onOpen) {
            VStack(alignment: .leading) {
                Text(title).font(.headline)
                Text(instructor).font(.subheadline)
                Text(duration).font(.caption)
            }
        }
        .buttonStyle(.plain)
        .accessibilityElement(children: .combine)
        .accessibilityLabel("\(title), by \(instructor), \(duration)")
        // State belongs in the value, not the hint (hints describe the result of the action and users can turn them off).
        .accessibilityValue(isCompleted ? "Completed" : "")
    }
}

// Accessible form field
struct EmailField: View {
    @Binding var email: String
    @State private var isInvalid = false

    var body: some View {
        VStack(alignment: .leading) {
            TextField("Email", text: $email)
                .textContentType(.emailAddress)
                .keyboardType(.emailAddress)
                .textInputAutocapitalization(.never)   // replaces autocapitalization(_:), deprecated
                .accessibilityLabel("Email address")
                // Do not overwrite the field's value (the typed text) with an error string.
                // Show the error as visible text (not colour alone) and announce it when it appears.
            if isInvalid {
                Text("Enter a valid email address")
                    .foregroundColor(.red)
            }
        }
        .onChange(of: isInvalid) { _, nowInvalid in   // two-parameter form: iOS 17+
            if nowInvalid {
                AccessibilityNotification.Announcement("Enter a valid email address").post()   // iOS 17+
            }
        }
    }
}

// Respect system accessibility settings (read them inside a View)
struct SettingsAwareView: View {
    @Environment(\.accessibilityReduceMotion) var reduceMotion
    @Environment(\.accessibilityInvertColors) var invertColors
    @Environment(\.dynamicTypeSize) var dynamicTypeSize  // Dynamic Type; sizeCategory is deprecated

    var body: some View {
        Text("Hello")
            .animation(reduceMotion ? nil : .easeInOut, value: dynamicTypeSize)
    }
}
// Verified against Apple's documentation data (developer.apple.com, 2026-11): AccessibilityNotification.Announcement
// (iOS 17+), textInputAutocapitalization(_:) (iOS 15+), autocapitalization(_:) and sizeCategory deprecated with
// dynamicTypeSize as replacement. accessibilityLiveRegion(_:) has no page in SwiftUI's documentation, so it was removed.
// Not compiled.
```

### Jetpack Compose (Android)

```kotlin
// Accessible card
@Composable
fun CourseCard(
    title: String,
    instructor: String,
    duration: String,
    isCompleted: Boolean,
    onClick: () -> Unit
) {
    Card(
        modifier = Modifier
            .clickable(onClick = onClick)
            // mergeDescendants = true: one focus target for the whole card instead of three Text nodes.
            // contentDescription replaces the merged Text children as the label: keep it only if you need
            // different wording (here it adds the completed state). Otherwise drop it and let the Texts be the label.
            .semantics(mergeDescendants = true) {
                contentDescription = "$title, by $instructor, $duration" +
                    if (isCompleted) ", completed" else ""
                role = Role.Button   // alternative: clickable(role = Role.Button, onClick = onClick)
            }
    ) {
        Column(modifier = Modifier.padding(16.dp)) {
            Text(title, style = MaterialTheme.typography.titleMedium)
            Text(instructor, style = MaterialTheme.typography.bodyMedium)
            Text(duration, style = MaterialTheme.typography.bodySmall)
        }
    }
}

// Accessible text field with error
@Composable
fun EmailField(email: String, onValueChange: (String) -> Unit, isError: Boolean) {
    OutlinedTextField(
        value = email,
        onValueChange = onValueChange,
        label = { Text("Email") },
        isError = isError,
        keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Email),
        supportingText = {
            if (isError) {
                Text(
                    "Enter a valid email address",
                    modifier = Modifier.semantics { liveRegion = LiveRegionMode.Assertive }
                )
            }
        },
        modifier = Modifier
            .fillMaxWidth()
            .semantics {
                if (isError) error("Enter a valid email address")
            }
    )
}

// Reduce motion
// Compose has no reduce-motion flag: androidx.compose.ui.platform.AccessibilityManager only offers
// calculateRecommendedTimeoutMillis(). Android's signal is "animators disabled system-wide"
// (Developer Options animator duration scale 0, or Battery Saver): ValueAnimator.areAnimatorsEnabled().
@Composable
fun AnimatedContent() {
    // API 26+. Read once per composition; it is not observable state, so it does not
    // recompose when the setting changes while the screen is open.
    val reduceMotion = remember { !ValueAnimator.areAnimatorsEnabled() }
    val animationSpec = if (reduceMotion) snap<Float>() else tween<Float>(300)
    // use animationSpec in animations
}
// Verified against developer.android.com/reference/android/animation/ValueAnimator#areAnimatorsEnabled() and
// developer.android.com/reference/kotlin/androidx/compose/ui/platform/AccessibilityManager (2026-11). Not compiled.
```

---

## React Native Accessibility

React Native accessibility maps to the same WCAG principles but uses platform-specific APIs.

### Core props
```tsx
import { useEffect } from 'react';
import {
  View, Text, TouchableOpacity, TextInput,
  AccessibilityInfo, Platform
} from 'react-native';

// ── Accessible card (combines children into one focus target)
function CourseCard({ title, instructor, isCompleted }: Props) {
  return (
    <View
      accessible={true}                          // combine into single focus
      accessibilityLabel={`${title}, by ${instructor}`}
      accessibilityHint={isCompleted ? undefined : 'Double-tap to open course'}
      accessibilityRole="button"
      accessibilityState={{ selected: isCompleted }}
    >
      <Text>{title}</Text>
      <Text>{instructor}</Text>
    </View>
  );
}

// ── Accessible text input with error
function EmailInput({ value, onChange, error }: InputProps) {
  // iOS has no live-region prop: announce the error when it first appears.
  // On Android the live region below announces content changes of a view; it may not announce a view that is
  // freshly mounted, as this conditional <Text> is. Keep the <Text> mounted (empty until there is an error) or test with
  // TalkBack on a device. iOS has no live-region prop, hence the explicit announcement here (iOS only, to avoid double reads).
  useEffect(() => {
    if (error && Platform.OS === 'ios') AccessibilityInfo.announceForAccessibility(error);
  }, [error]);

  return (
    <View>
      <Text nativeID="email-label">Email address</Text>
      <TextInput
        value={value}
        onChangeText={onChange}
        accessibilityLabel="Email address"         // name on iOS and Android
        accessibilityLabelledBy="email-label"      // Android only; optional once accessibilityLabel is set
        keyboardType="email-address"
        autoComplete="email"
        textContentType="emailAddress"            // iOS autofill
      />
      {error && (
        // React Native documents no aria-invalid / error-message prop. Show the error as visible text
        // next to the field (not colour alone). accessibilityLiveRegion is Android-only; announce on iOS.
        <Text accessibilityLiveRegion="assertive" accessibilityRole="alert">
          {error}
        </Text>
      )}
    </View>
  );
}

// Verified against reactnative.dev/docs/accessibility and /docs/accessibilityinfo (2026-11). Not compiled.
// Removed: accessibilityInvalidated and accessibilityErrorMessage, which are not documented there.
```

### Touch targets (WCAG 2.5.8 equivalent)
```tsx
import { StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  // iOS: minimum 44x44 pt; Android: minimum 48x48 dp
  touchable: {
    minWidth: 44,
    minHeight: 44,
    justifyContent: 'center',
    alignItems: 'center',
  },
  // hitSlop expands tap area without changing visual size
  // Use when the visual element must be smaller
});

// Use hitSlop for small icons
<TouchableOpacity
  hitSlop={{ top: 12, bottom: 12, left: 12, right: 12 }}
  accessibilityRole="button"
  accessibilityLabel="Delete item"
/>
```

### Dynamic Type (font scaling)
```tsx
import { Text } from 'react-native';

// allowFontScaling defaults to true, so a fixed fontSize still scales with the user's text size setting
<Text style={{ fontSize: 16 }}>Scales by default</Text>

// ❌ Only this blocks scaling: opting out explicitly
<Text allowFontScaling={false} style={{ fontSize: 16 }}>Does not scale</Text>

// ✅ Be explicit if you like (same as the default)
<Text allowFontScaling={true} style={{ fontSize: 16 }}>Scalable text</Text>
// Verified against reactnative.dev/docs/text (allowFontScaling default true, maxFontSizeMultiplier) (2026-11). Not compiled.

// ✅ maxFontSizeMultiplier: prevent runaway scaling in tight UIs
<Text maxFontSizeMultiplier={1.5} style={{ fontSize: 14 }}>Compact text</Text>
```

### Reduce Motion
```tsx
import { useEffect, useState } from 'react';
import { AccessibilityInfo } from 'react-native';
import Animated, { useSharedValue, withTiming, withSpring } from 'react-native-reanimated';

function AnimatedCard() {
  const [reduceMotion, setReduceMotion] = useState(false);
  const opacity = useSharedValue(0);

  useEffect(() => {
    AccessibilityInfo.isReduceMotionEnabled().then(setReduceMotion);
    const sub = AccessibilityInfo.addEventListener('reduceMotionChanged', setReduceMotion);
    return () => sub.remove();
  }, []);

  useEffect(() => {
    opacity.value = reduceMotion
      ? withTiming(1, { duration: 0 })   // instant
      : withSpring(1);                    // animated
  }, [reduceMotion]);

  return <Animated.View style={{ opacity }} />;
}
```

### Focus management (screen transition)
```tsx
import { useRef, useEffect } from 'react';
import { View, Text, AccessibilityInfo } from 'react-native';
// Verified against reactnative.dev/docs/accessibilityinfo (2026-11): sendAccessibilityEvent(ref, 'focus') replaces
// the deprecated setAccessibilityFocus(reactTag); the view needs accessible={true}. Not compiled or run on a device.

function NewScreen() {
  const headingRef = useRef<View>(null);

  useEffect(() => {
    // Move VoiceOver/TalkBack focus to the screen heading on mount.
    // setAccessibilityFocus(findNodeHandle(...)) is deprecated; pass the ref instead.
    if (headingRef.current) AccessibilityInfo.sendAccessibilityEvent(headingRef.current, 'focus');
  }, []);

  return (
    <View>
      <View
        ref={headingRef}
        accessible={true}
        accessibilityRole="header"
      >
        <Text>Settings</Text>
      </View>
    </View>
  );
}
```

> Quick search: `python scripts/search.py keys --reader TalkBack` for TalkBack gestures,
> `python scripts/search.py keys --reader VoiceOver --platform iOS` for VoiceOver iOS.
