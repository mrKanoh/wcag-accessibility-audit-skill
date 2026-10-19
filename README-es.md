<div align="center">

# ♿ WCAG Accessibility Audit Skill

**Skill gratuita y de código abierto para agentes de IA y personas que trabajan con accesibilidad WCAG 2.1/2.2 AA.**

Revisa código de interfaces web, prepara pruebas de teclado y lectores de pantalla
y organiza hallazgos de accesibilidad en español o inglés. Incluye patrones WAI-ARIA,
guías para móvil, bases consultables y plantillas de informes. Las revisiones de IA
y los análisis automáticos necesitan validación manual.

[![Alcance: WCAG 2.1/2.2 AA](https://img.shields.io/badge/Alcance-WCAG_2.1%2F2.2_AA-blueviolet)](https://www.w3.org/WAI/standards-guidelines/wcag/)
[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-green)](./LICENSE)
[![Pruebas](https://img.shields.io/github/actions/workflow/status/mrKanoh/wcag-accessibility-audit-skill/test.yml?branch=main&label=tests)](https://github.com/mrKanoh/wcag-accessibility-audit-skill/actions/workflows/test.yml)

[Read in English](./README.md)

[Qué hace](#qué-hace) · [Instalación](#instalación) · [Compatibilidad](#matriz-de-compatibilidad-según-documentación-oficial) · [Primer uso](#primer-uso) · [Alcance y límites](#alcance-y-límites) · [Bases consultables](#bases-consultables)

</div>

## Qué hace

Esta skill ofrece instrucciones y referencias reutilizables para desarrolladores, diseñadores y personas que revisan accesibilidad con ayuda de IA:

- Revisar código de interfaces y proponer correcciones de semántica, formularios, teclado, foco, contraste y WAI-ARIA (roles, estados y propiedades para tecnologías de asistencia).
- Preparar pruebas manuales con teclado y lectores de pantalla, incluidos NVDA, JAWS, VoiceOver y TalkBack.
- Organizar hallazgos, criterios de aceptación, entregas de diseño e informes de auditoría.
- Consultar datos de referencia y adaptar ejemplos de comprobaciones automáticas al proyecto.

La skill indica al agente que responda en el idioma del usuario. Los datos de referencia están principalmente en inglés; el [glosario inglés–español incluido](./data/glossary-es.csv) sirve de apoyo para la terminología en español.

## Instalación

El proyecto está pensado para personas que usan distintos agentes de IA, no solo Claude Code. Sus datos, prompts y plantillas también pueden consultarse directamente sin IA. El repositorio sigue el [formato abierto Agent Skills](https://agentskills.io/specification): un directorio con un `SKILL.md` más `scripts/` y `data/`. Un único `SKILL.md` es el núcleo para todos los productos; no hay copias por proveedor.

### Tres formas de usarla

1. **Skill nativa**: en un agente que admita Agent Skills, instala el **directorio completo** con el nombre `wcag-accessibility` (la especificación exige que `name` coincida con el nombre del directorio).
2. **Búsqueda con Python**: si el agente puede leer los archivos y ejecutar comandos, puede consultar las bases con `python scripts/search.py …` desde la raíz de la skill. Esto requiere **Python 3.10 o superior** (`requires-python = ">=3.10"` en `pyproject.toml`); cargar las instrucciones no lo requiere.
3. **Contexto manual**: entrega al asistente `SKILL.md` y los `data/*.csv` pertinentes o los [`prompts/`](./prompts) como contexto, donde el producto lo permita. Este modo no tiene descubrimiento automático ni ejecución. Si el asistente no puede ejecutar una consulta, debe indicarlo, pedirte los datos o darte el comando para que lo ejecutes tú. No debe inventar resultados.

Leer instrucciones y ejecutar Python son capacidades distintas: un agente puede tener la primera sin la segunda.

### Matriz de compatibilidad (según documentación oficial)

Estados de evidencia: **documentado** = el proveedor documenta el formato y las rutas; **NO VERIFICADO** = este proyecto no lo ha probado. Solo se ha probado Claude Code, y únicamente en el entorno descrito bajo la tabla; instalación, descubrimiento y ejecución siguen **NO VERIFICADOS** para Codex, Cursor y Copilot. No leas esta tabla como garantía de compatibilidad.

| Agente | Ubicaciones documentadas | Límites documentados | Fuente |
|--------|-------------------------|----------------------|--------|
| Claude Code | Personal `~/.claude/skills/<nombre>/SKILL.md`; proyecto `.claude/skills/<nombre>/SKILL.md`; se admiten archivos auxiliares | `/reload-skills` si la carpeta `skills` de primer nivel es nueva | [docs](https://code.claude.com/docs/en/skills) |
| Codex (OpenAI) | Repositorio `.agents/skills` (desde el directorio de trabajo hasta la raíz del repo); usuario `$HOME/.agents/skills`; administrador `/etc/codex/skills` | Las skills con el mismo nombre no se fusionan. Las skills del repositorio están disponibles en tareas de nube; las personales locales no se sincronizan allí. Ejecutar scripts requiere el entorno y los permisos de destino | [Skills](https://learn.chatgpt.com/docs/build-skills), [entornos de nube](https://learn.chatgpt.com/docs/environments/cloud-environments) |
| Cursor | Proyecto `.agents/skills/`, `.cursor/skills/`; usuario `~/.agents/skills/`, `~/.cursor/skills/`; también lee `.claude/skills/`, `.codex/skills/`, `~/.claude/skills/`, `~/.codex/skills/` | El agente ejecuta los scripts referenciados al invocar la skill. Cloud Agents: solo se sincroniza `~/.cursor/skills/`, y solo si se activa; las skills de proyecto y `~/.agents/skills/` no se copian | [docs](https://cursor.com/docs/skills) |
| GitHub Copilot | Proyecto `.github/skills`, `.claude/skills`, `.agents/skills`; personal `~/.copilot/skills`, `~/.agents/skills` | Documentado para el agente en la nube de Copilot, la revisión de código, la CLI, la app de Copilot y el modo agente en VS Code y JetBrains. La página no cubre el frontmatter ni la ejecución de scripts | [docs](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |

| Estado | Claude Code | Codex | Cursor | Copilot |
|--------|-------------|-------|--------|---------|
| Soporte documentado del formato | Sí | Sí | Sí | Sí |
| Instalación comprobada | Sí (copia de proyecto, ver abajo) | NO VERIFICADO | NO VERIFICADO | NO VERIFICADO |
| Descubrimiento comprobado | Sí (copia de proyecto, ver abajo) | NO VERIFICADO | NO VERIFICADO | NO VERIFICADO |
| Ejecución comprobada | Sí (`search.py`, ver abajo) | NO VERIFICADO | NO VERIFICADO | NO VERIFICADO |

**Alcance de la prueba con Claude Code (2026-10-19):** Claude Code 2.1.292 en Windows 11, modo no interactivo (`claude -p`, `--setting-sources project`), modelo `claude-sonnet-5-5`. Los archivos de la skill se copiaron a mano en un proyecto aislado, en `.claude/skills/wcag-accessibility/`; Claude Code listó la skill al iniciar y la cargó. En una ejecución el agente corrió el `scripts/search.py` incluido (`--wcag-version`, `--id`, `aria --component`) y sus conteos de registros de WCAG 2.1/2.2 (50/58) coincidieron con una ejecución directa del script. En una segunda ejecución revisó de forma estática un `form.html` pequeño sin modificar archivos. Son dos ejecuciones en un solo entorno, no una garantía para otras versiones, sistemas operativos, modelos o sesiones interactivas. Una comprobación posterior ejecutó seis casos pequeños de revisión de formularios y un recorrido de instalación y primer uso en una sesión nueva, a partir de una copia local de los archivos candidatos (no desde GitHub); es un recorrido técnico, no una prueba de usabilidad con una persona externa, y no incluyó lector de pantalla. En ella un caso produjo primero un hallazgo inventado y pasó en una repetición, y una respuesta interpretó `--wcag-version` como «solo los criterios añadidos en esa versión» (las notas del catálogo ahora explican que selecciona lo que pertenece a una versión). Los registros de las pruebas están en la carpeta local `reports/` del entorno de desarrollo, que Git ignora: no forman parte del repositorio publicado. No se probó la instalación mediante ningún marketplace o canal de distribución de terceros (incluido Agensi).

### Obtener una copia local sin elegir un agente

Desde la carpeta donde quieras guardarla:

```bash
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git wcag-accessibility
cd wcag-accessibility
```

Si el destino ya existe, revísalo primero o elige otra ubicación. Puedes consultar esta copia o ejecutar las búsquedas Python sin un agente. Para la detección nativa de skills, utiliza en cambio la ubicación específica de la aplicación que se indica abajo; un clon genérico no queda instalado automáticamente en todos los agentes.

### Instalar el paquete completo

Requisitos: Git para clonar y actualizar; Python 3.10+ solo para `scripts/search.py`. Elige **una ubicación por producto** y evita mantener copias duplicadas: no hay una carpeta documentada que sirva para los cuatro productos. Claude Code lee `~/.claude/skills/`; Codex y Copilot (personal) leen `~/.agents/skills/`; Cursor lee ambas, así que solo necesita una.

```bash
# Claude Code (Cursor también lee esta carpeta)
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git ~/.claude/skills/wcag-accessibility

# Codex, GitHub Copilot, Cursor (nivel de usuario)
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git ~/.agents/skills/wcag-accessibility
```

```powershell
# Windows (PowerShell), Claude Code; cómo Codex/Copilot resuelven $HOME en Windows es NO VERIFICADO
git clone https://github.com/mrKanoh/wcag-accessibility-audit-skill.git "$env:USERPROFILE\.claude\skills\wcag-accessibility"
```

Para un solo repositorio, clona en la carpeta de proyecto de ese repositorio (por ejemplo `.claude/skills/wcag-accessibility` o `.agents/skills/wcag-accessibility`, según la tabla). Los agentes en la nube (agente en la nube de Copilot, Cursor Cloud Agents, Codex en la nube) trabajan con lo que ve su entorno, así que una instalación local a nivel de usuario puede no aplicarse allí; consulta la página de cada proveedor.

Si el directorio de destino ya existe, `git clone` falla y no se sobrescribe nada. No lo borres:

- Si es un clon de este repositorio, ejecuta antes `git status` dentro de él. Confirma con commit o guarda con stash los cambios locales que quieras conservar y luego actualiza con `git pull`.
- Si es otra instalación, consérvala: renómbrala o muévela fuera de las carpetas de skills, para que dos copias no se carguen a la vez, o clona en otro directorio fuera de ellas para compararlas antes de decidir cuál instalar.

Copiar solo `SKILL.md` **no** equivale a la instalación completa: las instrucciones se cargarían, pero faltarían las bases consultables y `scripts/search.py`.

### Servidor MCP (opcional, ajeno al formato de skill)

`scripts/mcp-server.py` expone las bases CSV como 15 **recursos** MCP (`wcag://…`). No define herramientas ni prompts y no es un motor de auditoría. La lectura de recursos depende del cliente; aquí no se aporta un registro de validación de clientes (**NO VERIFICADO**). Importa el paquete Python `mcp`, que no está declarado en `pyproject.toml`. Este repositorio no lo configura por ti.

En Claude Code, si la carpeta `skills` de primer nivel no existía al iniciar la sesión, ejecuta `/reload-skills`. Leer instrucciones no concede acceso a archivos ni permiso para ejecutar scripts en ningún agente.

## Primer uso

Carga la skill con el mecanismo admitido por tu agente o proporciona manualmente las instrucciones y archivos auxiliares relevantes. Para la instalación de Claude Code anterior, invócala directamente:

```text
/wcag-accessibility
```

En cualquiera de las modalidades, pega o identifica el componente que quieres revisar y describe su comportamiento esperado:

```text
Revisa este modal según WCAG 2.2 AA. Identifica el código inspeccionado,
explica cada posible barrera, cita el criterio relacionado y propone
correcciones pequeñas. Separa los hallazgos confirmados de lo que necesita
pruebas en navegador, con teclado o lector de pantalla. No modifiques archivos todavía.
```

Un hallazgo útil debe identificar el elemento, la barrera, el criterio relacionado, una corrección propuesta y la verificación pendiente. Por ejemplo:

> **Ejemplo ilustrativo:** un botón que solo muestra un icono no tiene nombre accesible en el HTML proporcionado (4.1.2). Añadir un nombre accesible adecuado y comprobar su anuncio en un navegador con lector de pantalla. Código revisado; prueba con lector no ejecutada.

También puedes preguntar de forma natural, por ejemplo: «¿Cómo pruebo este formulario con NVDA?». En Claude Code, la activación automática depende de que Claude relacione tu petición con la descripción de la skill. Si no se activa, usa `/wcag-accessibility`. Consulta la [documentación oficial de skills](https://code.claude.com/docs/en/skills).

## Alcance y límites

- **Objetivo WCAG:** las instrucciones usan WCAG 2.1 AA de forma predeterminada y explican incorporaciones de 2.2. Indica la versión y el nivel que necesitas. La insignia de alcance describe el contenido; no es una certificación.
- **Cobertura del catálogo:** [wcag-criteria.csv](./data/wcag-criteria.csv) contiene 59 registros: los 50 criterios A/AA de 2.1 más los nueve añadidos en 2.2, incluidos tres de nivel AAA. Faltan los 28 criterios AAA heredados de 2.1. El criterio 4.1.1 se conserva para consultas históricas de 2.1; fue eliminado en 2.2.
- **Metadatos de versión:** cada registro tiene un campo `versions` (`2.1`, `2.2` o `2.1;2.2`), visible en JSON. Usa `--wcag-version 2.1` o `--wcag-version 2.2` en el subcomando `wcag` para conservar solo los registros etiquetados con esa versión (coincidencia exacta con el campo; 2.1 devuelve 50 registros e incluye 4.1.1, 2.2 devuelve 58 e incluye 2.5.8). Sin ese argumento no se filtra. El filtro selecciona los criterios que pertenecen a una versión, no solo los que esa versión añadió: todos los registros AA pertenecen a 2.2, así que `--wcag-version 2.2 --level AA` devuelve los mismos 24 registros que `--level AA`. Para listar solo las nueve adiciones de 2.2, usa `--output json` y conserva los registros cuyo `versions` sea exactamente `2.2`; la tabla y la salida CSV no muestran `versions`. El catálogo no incluye criterios AAA de 2.1, por lo que combinar el filtro de versión con `--level AAA` no da una lista completa.
- **Evidencia de revisión:** las sugerencias de IA y los análisis automáticos no demuestran conformidad. Prueba las páginas, estados, flujos completos, teclado y tecnologías de asistencia relevantes en el entorno de destino. Registra qué se comprobó realmente.
- **Otras plataformas y referencias legales:** las guías móviles y los resúmenes por jurisdicción son puntos de partida. Selecciona los requisitos aplicables a la plataforma y verifica las fuentes legales oficiales vigentes; una consulta a la base no determina las obligaciones legales de tu producto.

La fuente normativa es la [recomendación WCAG 2.2 del W3C](https://www.w3.org/TR/WCAG22/). El comando `wcag3` devuelve un aviso sobre el borrador y enlaces al W3C, no un catálogo de criterios.

## Bases consultables

La interfaz de línea de comandos (CLI) de Python se puede usar sin ningún agente de IA. Estas consultas usan la biblioteca estándar de Python y no requieren paquetes adicionales.

Ejecuta las consultas desde la raíz de tu copia local (`wcag-accessibility` en el clon genérico anterior). Si usaste la instalación personal de Claude Code, entra en su carpeta:

```bash
# macOS / Linux
cd ~/.claude/skills/wcag-accessibility
```

```powershell
# Windows (PowerShell)
Set-Location "$env:USERPROFILE\.claude\skills\wcag-accessibility"
```

Para una instalación de proyecto en Claude Code, usa `.claude/skills/wcag-accessibility`; con otros agentes, utiliza la ubicación real del repositorio. Ejecuta las siguientes consultas desde esa carpeta:

```bash
# Criterios relacionados con contraste, con metadatos de versión
python scripts/search.py wcag --keyword contrast --output json

# Patrón modal: roles, teclado y gestión del foco
python scripts/search.py aria --component modal --detail

# Glosario inglés–español
python scripts/search.py glossary --keyword contrast
```

Las consultas de contraste y glosario deberían devolver registros relacionados; la del modal debería describir el comportamiento del diálogo. Si `python` no está disponible, prueba `python3` en macOS/Linux o `py` en Windows y comprueba que sea Python 3.10 o superior. El error «can't open file» suele indicar que estás fuera de la raíz de la skill.

<details>
<summary>Más consultas y opciones de salida</summary>

```bash
# Solo registros etiquetados AA (no A + AA)
python scripts/search.py wcag --level AA

# Solo registros etiquetados con una versión WCAG (se combina con --level, --id, --keyword, --principle)
python scripts/search.py wcag --wcag-version 2.2 --level AA

# Todos los registros WCAG disponibles; revisa nivel y versiones según tu objetivo
python scripts/search.py wcag --output json

# Atajos de NVDA para navegar por encabezados
python scripts/search.py keys --reader NVDA --action heading

# Lectores de pantalla gratuitos para Windows
python scripts/search.py tools --type screen-reader --platform Windows --free --url

# Búsqueda en todas las bases
python scripts/search.py all --keyword contrast --output json

# Subcomandos y opciones específicas de WCAG
python scripts/search.py --help
python scripts/search.py wcag --help
```

La conformidad de nivel AA exige cumplir los criterios de nivel A y AA. `--level AA` filtra un nivel exacto; no genera una lista completa para evaluar conformidad AA. Los términos de búsqueda deben coincidir con el idioma de los datos; utiliza inglés en la mayoría de las bases.

Usa `--output json` o `--output csv` para obtener datos estructurados y `--export results.json` para guardar el formato seleccionado en un archivo. Los registros WCAG en JSON incluyen `versions`; la tabla y la salida CSV muestran menos campos.

</details>

<details>
<summary>Consultar las 14 bases</summary>

| Comando después de `python scripts/search.py` | Datos de referencia |
|---|---|
| `wcag` | Criterios WCAG, niveles, técnicas, fallos, fuentes y versiones |
| `aria` | Roles, propiedades, teclado y gestión del foco de componentes |
| `tools` | Herramientas de prueba por plataforma, tipo y coste |
| `keys` | Atajos de lectores de pantalla |
| `semantic` | Semántica HTML y recomendaciones de uso |
| `typography` | Tipografía, espaciado, redistribución del contenido y zoom |
| `color` | Contraste, estados, colores forzados y percepción del color |
| `kpis` | Métricas de accesibilidad y objetivos sugeridos |
| `handoff` | Listas para investigación, diseño, desarrollo, pruebas y lanzamiento |
| `models` | Modelos de discapacidad |
| `glossary` | Terminología inglés–español y definiciones |
| `legal` | Resúmenes de referencia por jurisdicción |
| `resources` | Estándares, guías, investigación, herramientas y comunidades |
| `cognitive` | Patrones de accesibilidad cognitiva |

Usa `all --keyword contrast` para buscar entre estas bases. `wcag3` es un comando de estado separado.

</details>

## Ejemplos y recursos del proyecto

El repositorio incluye ocho ejemplos HTML: [calendario](./examples/components/date-picker.html), [notificaciones](./examples/components/toast-notifications.html), [carrusel](./examples/components/carousel.html), [vista de árbol](./examples/components/tree-view.html), [autocompletado](./examples/components/combobox.html), [tabla interactiva](./examples/components/data-grid.html), [reproductor multimedia](./examples/components/media-player.html) y [pestañas](./examples/components/tabs.html).

Úsalos como ejemplos para aprender y adaptar. Antes de incorporarlos a un producto, revisa su comportamiento y pruébalos con los navegadores y tecnologías de asistencia que necesiten tus usuarios. Su inclusión no demuestra que estén listos para producción ni que se haya completado una prueba de compatibilidad.

| Recurso | Para qué sirve |
|---|---|
| [SKILL.md](./SKILL.md) | Instrucciones para el agente y entrada para aplicaciones con soporte de skills |
| [Prompts](./prompts/) | Doce instrucciones para revisión, corrección, contenido, entregas de diseño y planificación de pruebas |
| [Informe de auditoría](./templates/audit-report.md) | Punto de partida para documentar alcance, hallazgos y evidencia |
| [Plantilla de integración continua](./templates/a11y-ci.yml) | Ejemplo de comprobaciones automáticas; adapta dependencias, comandos, URL, rutas de configuración y tratamiento de fallos a tu proyecto |
| [Plantilla de informe VPAT](./templates/vpat-2.5-template.md) | Apoyo para informes; consulta los [recursos oficiales de VPAT de ITI](https://www.itic.org/policy/accessibility/vpat) antes de preparar un informe de conformidad de accesibilidad (ACR) |
| [Bibliografía](./RESOURCES.md) | Estándares y lecturas adicionales |
| [Código del servidor MCP](./scripts/mcp-server.py) | Servidor opcional del Protocolo de Contexto de Modelo para exponer los datos de referencia; requiere el paquete Python `mcp` y configurar el cliente por separado |
| [Historial de cambios](./CHANGELOG.md) | Cambios registrados del proyecto |

## Referencias y créditos

Los estándares y materiales de referencia incluyen [WCAG 2.1](https://www.w3.org/TR/WCAG21/), [WCAG 2.2](https://www.w3.org/TR/WCAG22/), la [guía de patrones WAI-ARIA](https://www.w3.org/WAI/ARIA/apg/), [WebAIM](https://webaim.org/), [Deque axe-core](https://github.com/dequelabs/axe-core) y [The A11Y Project](https://www.a11yproject.com/).

Se reconocen como referencias e inspiración los [recursos de accesibilidad de Paul J. Adam](https://pauljadam.com/) y la arquitectura de la skill `ui-ux-pro-max`. Estos créditos no implican autoría, revisión ni respaldo del proyecto por las personas u organizaciones citadas. La [bibliografía](./RESOURCES.md) contiene enlaces a recursos individuales.

## Contribuciones

Son bienvenidas las correcciones de documentación, criterios, ejemplos y traducciones. Consulta [CONTRIBUTING.md](./CONTRIBUTING.md) para conocer el proceso. Incluye una fuente para las correcciones técnicas y distingue la revisión de código de las pruebas realmente ejecutadas.

Para ejecutar las pruebas Python existentes desde una copia de desarrollo con pytest instalado:

```bash
python -m pytest tests/ -v
```

Estas pruebas verifican la herramienta de búsqueda y comprobaciones de datos; no demuestran conformidad de accesibilidad ni compatibilidad con lectores de pantalla.

## Licencia

[MIT](./LICENSE). Puedes usar, compartir y adaptar el proyecto según sus términos, conservando el aviso de copyright y el aviso de permiso.
