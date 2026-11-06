# AGENTS.md — wcag-accesibility-skill

Skill WCAG de accesibilidad (`SKILL.md`, `references/`, `templates/`, `data/*.csv`, `prompts/`, `examples/`, `evals/`) con utilidad de búsqueda en Python (`scripts/search.py`) y pruebas con pytest.

## Repositorio

- Ruta real: `D:\Proyectos\wcag-accesibility-skill`
- Remoto canónico: `mrKanoh/wcag-accessibility-audit-skill`. `git remote -v` aún usa el nombre anterior `claude-wcag-accessibility-skill`; GitHub redirige al canónico. Rama principal: `main`.
- Convención de commits: Conventional Commits (`feat:`, `fix:`, `docs:`, `data:`, `test:`, `chore:`), ver CONTRIBUTING.md. Si el commit es de etapa, pon la etapa al final.
- Cambios de la skill se documentan en `CHANGELOG.md` bajo `[Unreleased]`.

## Cómo verificar

Requiere Python 3.10+ y pytest (`python -m pip install pytest`). No hay lint, typecheck ni build.

- Pruebas: `python -m pytest tests/ -v`
- Integridad de los CSV: `python scripts/search.py wcag --level AA --output json`
- Búsqueda entre bases: `python scripts/search.py all --keyword contrast --output json`

La CI (`.github/workflows/test.yml`, Python 3.10/3.11/3.12) ejecuta esos tres comandos en cada push/PR a `main`. Las pruebas no validan los ejemplos HTML con teclado ni lector de pantalla.

## Qué publica

- Fusionar publica en producción: sí
- `main` es lo que clonan los usuarios (el README manda clonar `main`), así que fusionar a `main` publica. Existe además un canal manual por ZIP en `dist/agensi/` (ignorado por Git). No hay deploy en CI: `.github/workflows/test.yml` solo corre pruebas.
- Fusiona Ariel; nadie más fusiona (por eso `settings.json` niega `gh pr merge *`).

## Qué no tocar

- Archivos con cambios sin commit que no sean de tu orden (trabajo de Ariel o de otro proceso): no los edites, añadas ni reviertas.
- `.env` y variantes, secretos y `.claude/settings.local.json` (extras personales).
- `dist/`, `reports/`, `evals/results/` y `*-workspace/` (generados, ignorados por Git).
- Nada de `git add -A` ni `git add .`: usa rutas explícitas.
