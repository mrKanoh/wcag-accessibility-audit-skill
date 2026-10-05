<div align="center">

# ♿ wcag-accessibility-skill (Español)

**Una skill para Claude Code sobre accesibilidad web y móvil — basada en WCAG 2.1/2.2 Nivel AA.**

[🇺🇸 Read in English](./README.md)

<br>

</div>

---

## ✨ Multilingüe por Diseño

Aunque las bases de datos subyacentes (`CSV`) están en inglés, **esta skill está diseñada para ser completamente multilingüe**. 

Cuando uses Claude Code y le hables en español, Claude buscará automáticamente en las bases de datos, extraerá los patrones y criterios, y te **responderá en un español técnico perfecto**, utilizando el glosario oficial de accesibilidad (`data/glossary-es.csv`).

Puedes preguntarle a Claude:
* *"¿Cómo hago este modal accesible?"*
* *"¿Cuál es el contraste de color requerido para texto grande?"*
* *"Revisa este código React y dime si cumple con WCAG 2.2."*
* *"¿Qué estándar aplica en Europa para el 2025?"*

Claude te entregará los fragmentos de código ARIA y las explicaciones traducidas al momento.

---

## 📦 Instalación

**Requiere [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) instalado.**

Ejecuta esto en la carpeta de tu proyecto para instalar la skill globalmente:

```bash
claude skill add https://github.com/mrKanoh/claude-wcag-accessibility-skill.git
```

## 🗄️ Bases de Datos (Consultables vía CLI)

Además de usar a Claude, puedes buscar en las 14 bases de datos usando el CLI que viene incluido. Si instalas el paquete con `pip install .`, tendrás el comando `wcag-search`.

| Comando CLI | Contenido |
|-------------|-----------|
| `wcag-search wcag` | 59 criterios WCAG: los A y AA de 2.1 más los 9 añadidos en **2.2**. **Catálogo incompleto:** faltan los 28 AAA de 2.1. 4.1.1 es una entrada histórica de 2.1, retirada en 2.2 |
| `wcag-search wcag3` | Estado del borrador WCAG 3 y enlaces al W3C (sin criterios) |
| `wcag-search aria` | +25 patrones de componentes WAI-ARIA |
| `wcag-search tools` | Herramientas de pruebas (axe, WAVE, etc.) |
| `wcag-search keys` | Atajos de teclado para lectores de pantalla |
| `wcag-search semantic`| Semántica HTML y roles implícitos |
| `wcag-search cognitive`| Accesibilidad cognitiva (COGA) |
| `wcag-search legal` | Marcos legales por país (EAA, ADA, etc.) |
| `wcag-search all` | Búsqueda cruzada en todas las bases de datos |

## 🧩 Componentes HTML de Ejemplo

El proyecto incluye ejemplos de componentes HTML listos para producción y testeados con teclado y lectores de pantalla. Se encuentran en `examples/components/`:

1. `date-picker.html` (Calendario)
2. `toast-notifications.html` (Notificaciones Toast)
3. `carousel.html` (Carrusel)
4. `tree-view.html` (Vista de árbol)
5. `combobox.html` (Autocompletado)
6. `data-grid.html` (Tabla de datos interactiva)
7. `media-player.html` (Reproductor de medios con subtítulos)
8. `tabs.html` (Pestañas)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes leer la guía completa en [`CONTRIBUTING.md`](./CONTRIBUTING.md). 
