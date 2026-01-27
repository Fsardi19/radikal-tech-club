# CLAUDE.md - Reglas del Proyecto RADIKAL TECH CLUB

## Descripcion del Proyecto
Radikal Tech Club es una plataforma "One-Stop Shop" de IA para comercializacion y mercadeo dirigida a MiPyMEs (Micro, Pequenas y Medianas Empresas) en Latinoamerica, especificamente Colombia, Mexico, Chile, Costa Rica y Panama.

## Estructura del Proyecto
```
RADIKAL TECH CLUB/
├── .claude/                    # Documentacion de sesiones Claude
│   ├── SESSION_LOG.md          # Historial detallado de sesiones
│   ├── PROGRESO.md             # Estado actual del proyecto
│   ├── PROMPT_APERTURA.md      # Prompt para iniciar sesion
│   └── RESUMEN_PROXIMA_SESION.md
├── .streamlit/                 # Configuracion Streamlit
│   └── config.toml             # Tema oscuro personalizado
├── DOCS/                       # Documentos de referencia (NO en Git)
│   ├── ANALISIS/               # Analisis de mercado, investigacion
│   └── ESTRATEGIA/             # Planes estrategicos
├── FINANCIERO/                 # Documentos financieros
│   ├── DASHBOARD_RADIKAL_2026.html  # Dashboard HTML (en Git)
│   ├── Inversion Radikal.xlsx       # Datos inversion (local)
│   ├── Presupuesto Radikal 2026.xlsx # Presupuesto (local)
│   └── CONVERTIBLE PROMISSORY NOTE.docx
├── LEGAL/                      # Contratos legales (NO en Git)
│   ├── CONTRATO_VESTING_JUAN_PABLO_PINEDA.html (Panama Law)
│   └── VESTING_AGREEMENT_JUAN_PABLO_PINEDA_NY_LAW.html (NY Law)
├── streamlit_app.py            # App principal Streamlit
├── requirements.txt            # Dependencias Python
├── README.md                   # Documentacion publica
├── CLAUDE.md                   # Este archivo
└── .gitignore
```

## Repositorio y Deploy
- **GitHub:** https://github.com/Fsardi19/radikal-tech-club
- **Streamlit Cloud:** https://radikal-tech-club.streamlit.app (pendiente deploy)

## Reglas y Preferencias

### Formato de Entregables
- **PREFERIR HTML** sobre Markdown para visualizaciones y reportes
- Usar Chart.js (HTML) o Plotly (Streamlit) para graficos interactivos
- Dashboard con tabs/secciones navegables
- Colores del proyecto: #1a1a2e (primary), #e94560 (highlight), #00d9a5 (success)

### Idioma
- Documentacion en **ESPANOL**
- Variables y codigo en ingles

### Datos Financieros Criticos
```
TRM (COP/USD): 3,650
Inversion Total: $113,935.27 USD
├── Pre-JP Pineda: $60,602.97
└── Desde JP Pineda: $53,332.31

Gastos Admin Anuales: $281,719 USD
Gasto Mensual (Burn Rate): $23,477 USD
Breakeven: 102 clientes
```

### Equity JP Pineda
```
Participacion: 10% (111 de 1,111 acciones)
Vesting: 3 ANOS (NO 4), 33% anual
├── Enero 2026: 3.33%
├── Enero 2027: 6.67%
└── Enero 2028: 10.0%

Condiciones:
- Sin pago por acciones
- Compromiso de capitalizacion pro-rata segun % vested
```

### Modelo de Servicios (precios USD)
| Servicio | Setup | Mensual | Fee Pauta |
|----------|-------|---------|-----------|
| Launch | $800 | $75 | - |
| Sell | $1,500 | $150 | 15% |
| Optimize | $600 | $200 | - |

## Archivos Importantes

### Para Leer al Inicio de Sesion
1. `.claude/RESUMEN_PROXIMA_SESION.md` - Quick reference
2. `.claude/PROGRESO.md` - Estado actual y pendientes
3. Este archivo (`CLAUDE.md`) - Reglas del proyecto

### Documentos de Referencia (carpeta DOCS/)
- `ANALISIS/Analisis de Mercado de Servicios AI.pdf` - Estudio de mercado
- `ESTRATEGIA/Plan_Estrategico_Radikal_One_Stop_Shop_v4.docx` - Plan completo

### Entregables Principales
- `FINANCIERO/DASHBOARD_RADIKAL_2026.html` - Dashboard HTML interactivo
- `streamlit_app.py` - Dashboard Streamlit (deploy en cloud)
- `LEGAL/CONTRATO_VESTING_*.html` - Contratos de vesting (Panama y NY Law)

## Cosas a Recordar

### Hacer
- Usar extraccion XML para leer archivos .docx/.xlsx
- Separar datos "Antes de JP" vs "Desde JP"
- Validar numeros con el usuario
- Crear visuales HTML o Streamlit interactivos
- Mantener Git actualizado con cambios relevantes

### Evitar
- Asumir vesting de 4 anos (son 3)
- Mezclar periodos de inversion
- Crear archivos Markdown cuando se pide HTML
- Usar precios irreales para MiPyMEs
- Subir archivos sensibles (.xlsx, .docx, LEGAL/) a Git

## Comandos Utiles

```bash
# Abrir dashboard HTML
open "FINANCIERO/DASHBOARD_RADIKAL_2026.html"

# Ejecutar Streamlit local
streamlit run streamlit_app.py

# Git - actualizar repo
git add . && git commit -m "mensaje" && git push

# Extraer texto de Word
unzip -p "archivo.docx" word/document.xml | sed 's/<[^>]*>//g'
```

## Contacto y Contexto
- **Organizacion:** El Green Hub / RADIKAL
- **CEO:** Juan Pablo Pineda (10% equity)
- **Equipo:** Alejandro Rua, Oscar Perez, David Duarte
- **Mercado objetivo:** ~8 millones de MiPyMEs en LATAM

---
**Ultima actualizacion:** 27 Enero 2026
