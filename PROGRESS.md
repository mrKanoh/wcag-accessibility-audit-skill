# PROGRESS

## Trabajo actual
- Ninguno.

## Pendiente de Ariel
- Decidir el destino de los 5 archivos con cambios sin commit (auditoría de sitios): `CHANGELOG.md`, `SKILL.md`, `templates/audit-report.md`, `references/site-audit-procedure.md` y `templates/site-audit-workbook.md`. No son de WCAG-SETUP-1 y no se tocaron.
- Agregar `.env.*` (p. ej. `.env.local`) a `.gitignore`: hoy solo `.env` está ignorado.

## Pendientes
- Para la próxima orden: los 5 archivos sin commit de Ariel (auditoría de sitios) esperan su destino (commit, rama propia o descarte); ver «Pendiente de Ariel».
- Para la próxima orden: la línea base de pruebas se tomó con esos archivos presentes en el árbol de trabajo (`SKILL.md` modificado); repetirla cuando se decida su destino.

## Terminados
- 2026-11-06 WCAG-SETUP-1 — permisos versionados (`.claude/settings.json`), `AGENTS.md`, `CLAUDE.md`, `PROGRESS.md` y línea base de pruebas registrada · commits 1398d98 (etapa 1) y el commit de etapa 2 (HEAD de `tarea/wcag-setup-1`) · rondas 0 · auditor pendiente · pendiente: `.env.local` sin ignorar; destino de los 5 archivos de Ariel

## Línea base de pruebas
Fecha 2026-11-06, Windows, Python 3.12.10, pytest 8.3.3, rama `tarea/wcag-setup-1`, con los 5 archivos sin commit de Ariel presentes en el árbol de trabajo.

- `python -m pytest tests/ -v` → **90 passed, 0 failed** en 12.60 s (`tests/test_search.py`: 87 pruebas; `tests/test_skill_metadata.py`: 3 pruebas: `test_required_fields_present`, `test_name_follows_spec`, `test_description_within_1024_chars`). Sin fallos que listar.
- `python scripts/search.py wcag --level AA --output json` → salida 0 (paso de integridad de CSV de la CI).
- `python scripts/search.py all --keyword contrast --output json` → salida 0 (paso de búsqueda cruzada de la CI).
- Aviso no bloqueante: `PytestDeprecationWarning` de `pytest_asyncio` por `asyncio_default_fixture_loop_scope` sin definir (plugin instalado localmente; la CI solo instala `pytest`).
- No corre: lint, typecheck ni build (el proyecto no los tiene). Los ejemplos HTML no se validan con pruebas automáticas; su verificación es manual.
