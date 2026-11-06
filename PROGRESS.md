# PROGRESS

## Trabajo actual
- Ninguno.

## Pendiente de Ariel
- Agregar `.env.*` (p. ej. `.env.local`) a `.gitignore`: hoy solo `.env` está ignorado.

## Para la próxima orden
- Pendientes del análisis de «Inclusive Components» (Heydon Pickering, 2018–2019; contrastar cada detalle técnico con la fuente oficial vigente antes de editar):
  - Carrusel: rota solo, reanuda sin pedirlo y las flechas sobre los puntos avanzan doble.
  - Notificaciones: `alertdialog` sin foco y aviso que pide acción con temporizador.
  - Tabla ordenable: `th` con `tabindex` y sin botón.
  - Next.js: título «focus management» sin mover el foco.
  - Guía «cuándo no usar el componente».
  - Receta de tooltip/toggletip (el CSS del libro, solo `:hover`/`:focus`, no cumple 1.4.13: no copiarlo).
  - `aria-label` y traducción (investigar primero).
  - Hallazgo de WCAG-IC-1: `examples/components/tree-view.html` (l. 76 y 218) usa `aria-pressed` y `aria-selected` sobre botones de nodo del árbol; defecto distinto del de los toggles, no corregido.
- B2 (opcional): aclarar en `templates/site-audit-workbook.md` (~línea 39) que «three AAA entries» se refiere a los registros del dataset, no a todos los criterios AAA de WCAG 2.2.

## Terminados
- 2026-11-06 WCAG-IC-1 — toggles con una sola forma (etiqueta fija con `aria-pressed`, o etiqueta cambiante sin él) en `SKILL.md` y `media-player.html` con regla nueva en la guía de botones; `examples/components/README.md` sin afirmar pruebas no registradas; fila Tooltip de `data/aria-patterns.csv` con 1.4.13 y nombre vs descripción; tags de axe con `wcag21a,wcag21aa` en `SKILL.md` y `templates/a11y-ci.yml` (cierra M1); entrada en `CHANGELOG.md`; HTML no probados en navegador · commits 7cce8bb (etapa 1), 56dbe71 (etapa 2) y la etapa 3 de cierre (HEAD de `tarea/wcag-ic-1`) · rondas 0 · auditor pendiente · pendiente: carrusel, notificaciones, tabla ordenable, Next.js, guía «cuándo no usar», receta tooltip/toggletip, `aria-label` y traducción, `tree-view.html` (ver «Para la próxima orden»)
- 2026-11-06 WCAG-SITEAUDIT-1 — procedimiento (`references/site-audit-procedure.md`) y libro de evidencia (`templates/site-audit-workbook.md`) para auditoría de sitios, `templates/audit-report.md` adaptado, índices en `SKILL.md` y ambos README, entrada en `CHANGELOG.md`; correcciones de revisión: se quita la etiqueta inexistente `wcag22a` de axe-core y se aclara que 2.4.11 es solo de WCAG 2.2 · commits 5b6454c (etapa 2), b18e1fa (etapa 3) y la etapa 4 de cierre (HEAD de `tarea/wcag-siteaudit-1`, reformula la condición de 1.4.10 según la norma); la etapa 1 fue solo revisión, sin commit · rondas 0 · auditor Opus 0/1/3, 1 pasada · pendiente: M1 y B2 (ver «Para la próxima orden»)
- 2026-11-06 WCAG-SETUP-1 — permisos versionados (`.claude/settings.json`), `AGENTS.md`, `CLAUDE.md`, `PROGRESS.md` y línea base de pruebas registrada · decisión de Ariel 2026-11-06: fusionar SÍ publica (`main` es lo que clonan los usuarios) · commits 1398d98 (etapa 1), 02c4e09 (etapa 2), 4b6c4d1 (etapa 3, corrección) y la etapa 4 de cierre (HEAD de `tarea/wcag-setup-1`) · rondas 1 · auditor Opus 0/3/4, 1 pasada · pendiente: `.env.local` sin ignorar; destino de los 5 archivos de Ariel

## Línea base de pruebas
Fecha 2026-11-06, Windows, Python 3.12.10, pytest 8.3.3. Corrida de WCAG-SETUP-1 en `tarea/wcag-setup-1`, con los 5 archivos de auditoría de sitios sin commit en el árbol; repetida en `tarea/wcag-siteaudit-1` con esos archivos ya commiteados: mismo resultado (90 passed en 11.18 s, los dos comandos de CI con salida 0).

- `python -m pytest tests/ -v` → **90 passed, 0 failed** en 12.60 s (`tests/test_search.py`: 87 pruebas; `tests/test_skill_metadata.py`: 3 pruebas: `test_required_fields_present`, `test_name_follows_spec`, `test_description_within_1024_chars`). Sin fallos que listar.
- `python scripts/search.py wcag --level AA --output json` → salida 0 (paso de integridad de CSV de la CI).
- `python scripts/search.py all --keyword contrast --output json` → salida 0 (paso de búsqueda cruzada de la CI).
- Aviso no bloqueante: `PytestDeprecationWarning` de `pytest_asyncio` por `asyncio_default_fixture_loop_scope` sin definir (plugin instalado localmente; la CI solo instala `pytest`).
- No corre: lint, typecheck ni build (el proyecto no los tiene). Los ejemplos HTML no se validan con pruebas automáticas; su verificación es manual.
