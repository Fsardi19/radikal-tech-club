# CLAUDE.md - Reglas del Proyecto RADIKAL TECH CLUB

## Descripcion del Proyecto
Radikal es una plataforma de marketing con inteligencia artificial: cinco agentes (Ankor, Sira, Nexo, Kronos, Indexa) que investigan la marca y su competencia, generan imagenes, videos y textos, y los publican en redes sociales. Mercado hispanohablante en Latinoamerica y Estados Unidos. Sitio: https://www.radikaltech.ai

Hasta 2025 el proyecto exploro otros modelos (precios del agro, comercializacion de productos, venta en Estados Unidos con Shopify e IA). La plataforma actual funciona desde mayo de 2026.

## Contexto completo (leer siempre)
El detalle del proyecto esta en un archivo local que no va a Git:

@CONTEXTO_RADIKAL.md

Ahi estan: producto y sitio, historia de los pivotes, personas, estructura societaria, ronda de inversion, cifras actuales e historicas, inconsistencias detectadas, entregables y pendientes. Si ese archivo no carga, leerlo a mano antes de trabajar.

## El repositorio es PUBLICO
- **GitHub:** https://github.com/Fsardi19/radikal-tech-club (visibilidad publica)
- Este archivo y la carpeta `.claude/` estan versionados. **No escribir aqui ni en `.claude/` cifras, terminos de la ronda, participaciones, nombres de inversionistas ni nada confidencial.** Eso va en `CONTEXTO_RADIKAL.md`.
- No ejecutar `git add .` sin revisar antes `git status`.
- No hacer commit ni push sin que el usuario lo pida.

## Estructura del Proyecto
```
RADIKAL TECH CLUB/
├── CLAUDE.md                   # Este archivo (publico)
├── CONTEXTO_RADIKAL.md         # Contexto completo (LOCAL, no en Git)
├── .claude/                    # Documentacion de sesiones (publico)
│   ├── SESSION_LOG.md          # Historial de sesiones
│   ├── PROGRESO.md             # Estado actual
│   ├── PROMPT_APERTURA.md      # Prompt para iniciar sesion
│   └── RESUMEN_PROXIMA_SESION.md
├── RONDA/                      # Entregables de la ronda y la asamblea (LOCAL)
│   └── LINEA_DE_TIEMPO_PIVOTES_RADIKAL.html
├── DOCS/                       # Documentos de referencia (LOCAL)
│   ├── ANALISIS/               # Mercado, investigacion, recomendaciones vs Sintra
│   └── ESTRATEGIA/             # Plan estrategico v4 (nov 2025)
├── FINANCIERO/                 # Dashboard HTML (en Git); xlsx y docx (LOCAL)
├── LEGAL/                      # Contratos de vesting (LOCAL)
├── streamlit_app.py            # Dashboard Streamlit (modelo financiero anterior)
├── Recomendaciones_Optimizacion_RADIKAL_TECH_AI.html
├── requirements.txt
├── README.md
└── .gitignore
```

Carpetas hermanas en `../`:
- `RADIKAL ORIGINAL/` - estrategia de negocio y de marca de 2024 (etapa anterior).
- `PIANO PIANO/` - proyecto aparte del aceite de oliva, una de las marcas de prueba.

## Reglas y Preferencias

### Formato de Entregables
- **PREFERIR HTML** sobre Markdown para visualizaciones y reportes
- Usar Chart.js (HTML) o Plotly (Streamlit) para graficos interactivos
- Colores del proyecto: #1a1a2e (primary), #e94560 (highlight), #00d9a5 (success)
- El sitio web usa otros colores (morado oscuro y rosado). Preguntar cual usar si el entregable es de cara a clientes.
- Entregables para la asamblea o inversionistas: guardarlos en `RONDA/`

### Idioma
- Documentacion en **ESPANOL**
- Variables y codigo en ingles

### Cifras
- Las cifras del modelo de enero de 2026 (Launch / Sell / Optimize, breakeven de 102 clientes) ya no aplican.
- Las cifras actuales vienen de una conversacion y no estan validadas. **Confirmar con el usuario antes de ponerlas en un entregable.**
- Separar siempre datos "Antes de JP" y "Desde JP".
- Vesting de JP Pineda: **3 anos, no 4**.

## Para Leer al Inicio de Sesion
1. Este archivo y `CONTEXTO_RADIKAL.md`
2. `.claude/RESUMEN_PROXIMA_SESION.md`
3. `.claude/PROGRESO.md`

## Al Cerrar la Sesion
1. Actualizar `CONTEXTO_RADIKAL.md` con todo lo nuevo (incluido lo confidencial)
2. Actualizar `.claude/SESSION_LOG.md`, `PROGRESO.md` y `RESUMEN_PROXIMA_SESION.md` sin datos confidenciales
3. Actualizar la memoria de Claude si cambio algo duradero

## Cosas a Recordar

### Hacer
- Usar `~/.claude/xlsx-venv/bin/python` para leer .docx y .xlsx
- Indicar de donde sale cada cifra (sitio, reunion o archivo)
- Validar numeros con el usuario
- Crear visuales HTML o Streamlit interactivos

### Evitar
- Asumir vesting de 4 anos (son 3)
- Mezclar periodos de inversion
- Crear archivos Markdown cuando se pide HTML
- Usar las cifras del modelo anterior como si fueran vigentes
- Subir a Git archivos sensibles (.xlsx, .docx, LEGAL/, RONDA/, CONTEXTO_RADIKAL.md)

## Comandos Utiles

```bash
# Abrir la linea de tiempo de la ronda
open "RONDA/LINEA_DE_TIEMPO_PIVOTES_RADIKAL.html"

# Abrir dashboard HTML (modelo anterior)
open "FINANCIERO/DASHBOARD_RADIKAL_2026.html"

# Ejecutar Streamlit local
streamlit run streamlit_app.py

# Git - revisar antes de subir (repo publico)
git status
```

## Contacto y Contexto
- **Organizacion:** El Green Hub / RADIKAL
- **Personas y roles:** ver `CONTEXTO_RADIKAL.md`

---
**Ultima actualizacion:** 7 Octubre 2026
