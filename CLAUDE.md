# CLAUDE.md - Reglas del Proyecto RADIKAL TECH CLUB

## Descripción del Proyecto
Radikal Tech Club es una plataforma "One-Stop Shop" de IA para comercialización y mercadeo dirigida a MiPyMEs (Micro, Pequeñas y Medianas Empresas) en Latinoamérica, específicamente Colombia, México, Chile, Costa Rica y Panamá.

## Estructura del Proyecto
```
RADIKAL TECH CLUB/
├── .claude/                    ← Documentación de sesiones Claude
│   ├── SESSION_LOG.md          ← Historial detallado de sesiones
│   └── PROGRESO.md             ← Estado actual del proyecto
├── FINANCIERO/                 ← Documentos financieros
│   ├── DASHBOARD_RADIKAL_2026.html  ← Dashboard principal (abrir en navegador)
│   ├── *.xlsx                  ← Datos financieros (Excel)
│   └── *.docx                  ← Documentos legales y planes
├── *.pdf                       ← Análisis de mercado e investigación
└── CLAUDE.md                   ← Este archivo
```

## Reglas y Preferencias

### Formato de Entregables
- **PREFERIR HTML** sobre Markdown para visualizaciones y reportes
- Usar Chart.js para gráficos interactivos
- Dashboard con tabs/secciones navegables
- Colores del proyecto: #1a1a2e (primary), #e94560 (highlight), #00d9a5 (success)

### Idioma
- Documentación en **ESPAÑOL**
- Variables y código en inglés

### Datos Financieros Críticos
```
TRM (COP/USD): 3,650
Inversión Total: $113,935.27 USD
├── Pre-JP Pineda: $60,602.97
└── Desde JP Pineda: $53,332.31

Gastos Admin Anuales: $281,719 USD
Gasto Mensual (Burn Rate): $23,477 USD
Breakeven: 102 clientes
```

### Equity JP Pineda
```
Participación: 10% (111 de 1,111 acciones)
Vesting: 3 AÑOS (NO 4), 33% anual
├── Enero 2026: 3.33%
├── Enero 2027: 6.67%
└── Enero 2028: 10.0%
```

### Modelo de Servicios (precios USD)
| Servicio | Setup | Mensual | Fee Pauta |
|----------|-------|---------|-----------|
| Launch | $800 | $75 | - |
| Sell | $1,500 | $150 | 15% |
| Optimize | $600 | $200 | - |

## Archivos Importantes

### Para Leer al Inicio de Sesión
1. `.claude/SESSION_LOG.md` - Qué se hizo en sesiones anteriores
2. `.claude/PROGRESO.md` - Estado actual y pendientes
3. Este archivo (`CLAUDE.md`) - Reglas del proyecto

### Documentos de Referencia
- `Plan_Estrategico_Radikal_One_Stop_Shop_v4.docx` - Estrategia completa
- `Presupuesto Radikal 2026.xlsx` - Datos de gastos
- `Inversion Radikal.xlsx` - Histórico de inversión
- `CONVERTIBLE PROMISSORY NOTE.docx` - Modelo de acuerdo (Theodore)

### Entregable Principal
- `FINANCIERO/DASHBOARD_RADIKAL_2026.html` - Abrir en navegador

## Cosas a Recordar

### ✅ Hacer
- Usar extracción XML para leer archivos .docx/.xlsx
- Separar datos "Antes de JP" vs "Desde JP"
- Validar números con el usuario
- Crear visuales HTML interactivos

### ❌ Evitar
- Asumir vesting de 4 años (son 3)
- Mezclar períodos de inversión
- Crear archivos Markdown cuando se pide HTML
- Usar precios irreales para MiPyMEs

## Comandos Útiles

```bash
# Abrir dashboard
open "FINANCIERO/DASHBOARD_RADIKAL_2026.html"

# Extraer texto de Word
unzip -p "archivo.docx" word/document.xml | sed 's/<[^>]*>//g'

# Extraer datos de Excel
unzip -p "archivo.xlsx" xl/worksheets/sheet1.xml
```

## Contacto y Contexto
- **Organización:** El Green Hub / RADIKAL
- **CEO:** Juan Pablo Pineda
- **Equipo:** Alejandro Rua, Oscar Pérez, David Duarte
- **Mercado objetivo:** ~8 millones de MiPyMEs en LATAM

---
**Última actualización:** 27 Enero 2026
