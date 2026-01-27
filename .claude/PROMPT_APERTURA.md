================================================================================
                    🚀 PROMPT DE APERTURA - CLAUDE CODE
                         (Copiar al iniciar sesión)
================================================================================

INICIO DE SESIÓN CLAUDE CODE

================================================================================
📁 PROYECTO: cd ~/Desktop/"EL GREEN HUB"/"RADIKAL"/"RADIKAL TECH CLUB"
================================================================================

RADIKAL TECH CLUB - Plataforma One-Stop Shop IA para MiPyMEs LATAM

================================================================================
                         FASE 1: CARGA DE CONTEXTO
================================================================================

ANTES DE HACER CUALQUIER COSA, lee estos archivos EN ORDEN:

1. CONFIGURACIÓN DEL PROYECTO:
   ```bash
   # Reglas y contexto del proyecto
   cat CLAUDE.md
   ```

2. ESTADO ACTUAL:
   ```bash
   # Historial de sesiones anteriores
   cat .claude/SESSION_LOG.md

   # Estado del trabajo y datos clave
   cat .claude/PROGRESO.md

   # Quick reference
   cat .claude/RESUMEN_PROXIMA_SESION.md
   ```

3. DOCUMENTOS DE REFERENCIA (si necesitas profundizar):
   - `FINANCIERO/Plan_Estrategico_Radikal_One_Stop_Shop_v4.docx` → Estrategia
   - `FINANCIERO/Presupuesto Radikal 2026.xlsx` → Gastos
   - `FINANCIERO/Inversion Radikal.xlsx` → Inversión histórica

================================================================================
                         FASE 2: DATOS CLAVE DEL PROYECTO
================================================================================

📊 NÚMEROS QUE DEBES RECORDAR:

┌─────────────────────────────────────────────────────────────────────────────┐
│                           INVERSIÓN                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ Total histórico:        $113,935.27 USD                                     │
│ Pre-JP Pineda:          $60,602.97 USD                                      │
│ Desde JP Pineda:        $53,332.31 USD  ← USAR ESTE PARA ESTADOS FINANCIEROS│
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                           PRESUPUESTO 2026                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ Gastos Admin Anuales:   $281,719 USD                                        │
│ Gasto Mensual:          $23,477 USD                                         │
│ Colombia:               $76,844/año (27.3%)                                 │
│ Panamá:                 $204,874/año (72.7%)                                │
│ TRM:                    3,650 COP/USD                                       │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                           MODELO DE INGRESOS                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ Servicio    │ Setup   │ Mensual  │ Fee Pauta │ Total/cliente/año           │
├─────────────┼─────────┼──────────┼───────────┼─────────────────────────────┤
│ Launch      │ $800    │ $75      │ -         │ $1,700                      │
│ Sell        │ $1,500  │ $150     │ 15%       │ $3,750                      │
│ Optimize    │ $600    │ $200     │ -         │ $3,000                      │
├─────────────┴─────────┴──────────┴───────────┴─────────────────────────────┤
│ ARPC (promedio): $2,771/año    │    Breakeven: 102 clientes                │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                           EQUITY JP PINEDA                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ Participación total:    10% (111 de 1,111 acciones)                         │
│ Vesting:                3 AÑOS, 33% anual (NO 4 años)                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Enero 2026 (Año 1):     33.33% → 3.33% de la compañía                       │
│ Enero 2027 (Año 2):     66.67% → 6.67% de la compañía                       │
│ Enero 2028 (Año 3):     100%   → 10.0% de la compañía                       │
└─────────────────────────────────────────────────────────────────────────────┘

================================================================================
                         FASE 3: ENTREGABLES EXISTENTES
================================================================================

📁 ARCHIVOS CLAVE:

┌──────────────────────────────────────┬──────────────────────────────────────┐
│ Archivo                              │ Descripción                          │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ FINANCIERO/DASHBOARD_RADIKAL_2026.html│ Dashboard principal - ABRIR EN      │
│                                      │ NAVEGADOR para ver visualizaciones  │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ .claude/SESSION_LOG.md               │ Historial detallado de sesiones      │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ .claude/PROGRESO.md                  │ Estado actual y métricas             │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ CLAUDE.md                            │ Reglas del proyecto                  │
└──────────────────────────────────────┴──────────────────────────────────────┘

Para abrir el dashboard:
```bash
open "FINANCIERO/DASHBOARD_RADIKAL_2026.html"
```

================================================================================
                         FASE 4: PREFERENCIAS DEL USUARIO
================================================================================

✅ EL USUARIO PREFIERE:
- **HTML** sobre Markdown para visualizaciones
- Dashboards interactivos con Chart.js
- Documentación en **ESPAÑOL**
- Validar números antes de asumir
- Separar datos "Pre-JP" vs "Desde JP"

❌ EVITAR:
- Crear archivos .md cuando se pide HTML
- Asumir vesting de 4 años (son 3)
- Mezclar períodos de inversión
- Precios irreales para MiPyMEs

================================================================================
                         FASE 5: HERRAMIENTAS ÚTILES
================================================================================

📋 COMANDOS DE SESIÓN:
┌──────────────────────┬─────────────────────────────────────────────────────┐
│ Comando              │ Función                                             │
├──────────────────────┼─────────────────────────────────────────────────────┤
│ /compact             │ Comprimir historial (usar cada 10-15 mensajes)      │
│ /clear               │ Limpiar contexto (al cambiar de tarea)              │
│ /cost                │ Ver costo de la sesión actual                       │
└──────────────────────┴─────────────────────────────────────────────────────┘

🔧 COMANDOS ÚTILES PARA ESTE PROYECTO:
```bash
# Abrir dashboard
open "FINANCIERO/DASHBOARD_RADIKAL_2026.html"

# Extraer texto de archivos Word
unzip -p "archivo.docx" word/document.xml | sed 's/<[^>]*>//g'

# Extraer datos de Excel
unzip -p "archivo.xlsx" xl/worksheets/sheet1.xml
```

================================================================================
                         FASE 6: PENDIENTES DE SESIONES ANTERIORES
================================================================================

📋 TODO (última sesión: 27 Enero 2026):

1. [ ] **ALTA:** Validar números del dashboard con stakeholders
2. [ ] **ALTA:** Crear versión legal formal del Equity Agreement
3. [ ] **MEDIA:** Agregar proyecciones de flujo de caja mensual
4. [ ] **MEDIA:** Crear pitch deck basado en dashboard
5. [ ] **BAJA:** Agregar sliders interactivos para escenarios

================================================================================
                         FASE 7: CONFIRMAR COMPRENSIÓN
================================================================================

ANTES DE EMPEZAR A TRABAJAR, confirma que entendiste:

□ Este es RADIKAL TECH CLUB - plataforma One-Stop Shop IA para MiPyMEs
□ Hay un dashboard HTML con 5 secciones ya creado
□ Los datos financieros clave (inversión, gastos, vesting)
□ El usuario prefiere HTML sobre Markdown
□ El vesting de JP Pineda es 3 años empezando Enero 2026

================================================================================
                              INICIO
================================================================================

Ahora que has cargado todo el contexto:

1. Resúmeme en 3-5 bullets qué entendiste del proyecto
2. Dime qué entregables ya existen
3. Pregúntame qué quiero lograr en esta sesión

NO empieces a trabajar hasta que yo confirme el objetivo de hoy.

================================================================================
                    EQUIPO DEL PROYECTO
================================================================================

👤 CEO: Juan Pablo Pineda (10% equity, vesting 3 años)
👥 Equipo técnico: Alejandro Rua, Oscar Pérez, David Duarte
🏢 Organización: El Green Hub / RADIKAL
🌎 Mercado: MiPyMEs en Colombia, México, Chile, Costa Rica, Panamá

================================================================================
