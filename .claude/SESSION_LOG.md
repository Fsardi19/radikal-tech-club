# Session Log - RADIKAL TECH CLUB

## Sesión: 27 Enero 2026
**Duración aproximada:** ~2 horas
**Modelo:** Claude Opus 4.5

### 🎯 Objetivo de la Sesión
Crear documentación financiera completa para Radikal Tech Club incluyendo:
- Informe de justificación de gastos bajo gestión de JP Pineda
- Escenarios de proyecciones accionarias con entrada de Pineda al 10%
- Acuerdo de equity/vesting para Juan Pablo Pineda como CEO
- Dashboard visual HTML con toda la información financiera

### ✅ Completado
- [x] Lectura y análisis de documentos del proyecto (PDFs de análisis de mercado, investigación de soporte)
- [x] Extracción de datos del Convertible Promissory Note (Theodore/Coffee Carbon)
- [x] Extracción de datos del Presupuesto Radikal 2026
- [x] Lectura del Plan Estratégico Radikal One-Stop Shop v4
- [x] Creación de dashboard HTML interactivo con 5 secciones
- [x] Calibración de ingresos según servicios Launch/Sell/Optimize para MiPyMEs
- [x] Configuración de vesting 3 años (33% anual) empezando Enero 2026

### 📁 Archivos Modificados/Creados
| Archivo | Acción | Descripción |
|---------|--------|-------------|
| FINANCIERO/DASHBOARD_RADIKAL_2026.html | Creado | Dashboard interactivo con 5 secciones: Informe Financiero, Modelo de Ingresos, Presupuesto 2026, Escenarios de Capital, Equity Agreement |
| FINANCIERO/Plan_Estrategico_Radikal_One_Stop_Shop_v4.docx | Movido | Desde Downloads a carpeta del proyecto |
| FINANCIERO/Plan_Estrategico_Radikal_One_Stop_Shop_v4 2.docx | Movido | Desde Downloads a carpeta del proyecto |
| FINANCIERO/INFORME_FINANCIERO_RADIKAL.md | Creado/Eliminado | Reemplazado por dashboard HTML |
| FINANCIERO/ESCENARIOS_ACCIONARIOS_PINEDA.md | Creado/Eliminado | Reemplazado por dashboard HTML |
| FINANCIERO/EQUITY_AGREEMENT_JUAN_PABLO_PINEDA.md | Creado/Eliminado | Reemplazado por dashboard HTML |

### 🔧 Decisiones Técnicas Importantes

**1. Inversión bajo gestión JP Pineda:** $53,332.31 USD
   - Colombia: desde fila 8 en adelante
   - Panamá: desde fila 9 en adelante
   - Este es el monto correcto para estados financieros desde que Pineda es CEO

**2. Modelo de Ingresos Calibrado (servicios para MiPyMEs Colombia):**
   | Servicio | Setup | Suscripción | Extra |
   |----------|-------|-------------|-------|
   | Launch | $800 | $75/mes | - |
   | Sell | $1,500 | $150/mes | 15% pauta |
   | Optimize | $600 | $200/mes | - |

**3. Escenarios de Ingresos:**
   - Conservador (30 clientes): $83,400/año → Déficit $198,319
   - Base (60 clientes): $166,250/año → Déficit $115,469
   - Optimista (100 clientes): $278,000/año → Casi breakeven

**4. Vesting JP Pineda (CORREGIDO):**
   - 3 años, 33% anual
   - Enero 2026 (Año 1): 33% → 3.33%
   - Enero 2027 (Año 2): 66% → 6.67%
   - Enero 2028 (Año 3): 100% → 10.0%

**5. Gastos Administrativos Anuales:** $281,719 USD
   - Colombia: $76,844/año (27.3%)
   - Panamá: $204,874/año (72.7%)

### 🐛 Bugs Encontrados/Resueltos
| Bug | Estado | Solución |
|-----|--------|----------|
| Archivos .docx/.xlsx no se pueden leer | ✅ | Usar unzip + sed para extraer XML |
| Vesting calculado con 4 años | ✅ | Corregido a 3 años per usuario |
| Vesting empezaba en 2027 | ✅ | Corregido para empezar en 2026 |

### ⚠️ Problemas Pendientes
- [ ] Archivos Word binarios no leíbles directamente (Respuesta Propuesta Batech.docx)
- [ ] Validar números exactos con el Excel original de Inversion Radikal.xlsx

### 📋 TODO para Próxima Sesión
1. [ ] Prioridad ALTA: Revisar y validar números del dashboard con stakeholders
2. [ ] Prioridad ALTA: Crear versión legal formal del Equity Agreement para firma
3. [ ] Prioridad MEDIA: Agregar proyecciones mensuales de flujo de caja
4. [ ] Prioridad MEDIA: Crear pitch deck basado en el dashboard
5. [ ] Prioridad BAJA: Agregar más interactividad al dashboard (sliders para escenarios)

### 💡 Notas y Aprendizajes
- El usuario prefiere visuales HTML sobre archivos Markdown
- Los datos financieros deben separarse por período de gestión (Antes JP vs Desde JP)
- El breakeven requiere ~102 clientes con el mix actual de servicios
- Capital actual ($113,935) cubre casi el escenario base de déficit ($115,469)
- El Plan Estratégico define 3 momentos del cliente: Launch, Sell, Optimize

### 🔗 Referencias Útiles
- Convertible Promissory Note de Theodore/Coffee Carbon como modelo para vesting
- Plan Estratégico Radikal One-Stop Shop v4 para modelo de servicios
- Presupuesto Radikal 2026 para gastos administrativos

---

## Datos Clave del Proyecto

### Estructura de Inversión
```
Inversión Total: $113,935.27 USD
├── Pre-JP Pineda: $60,602.97 USD
└── Desde JP Pineda: $53,332.31 USD
    ├── Colombia: $6,893.12 (12.9%)
    ├── Panamá: $37,467.19 (70.3%)
    └── USA: $8,972.00 (16.8%)
```

### Presupuesto 2026
```
Gastos Admin Anuales: $281,719 USD
├── Colombia: $76,844/año ($6,404/mes)
└── Panamá: $204,874/año ($17,073/mes)

Nómina:
├── JP Pineda (COL): $5,307/mes = $63,680/año
├── JP Pineda (PAN): $14,000/mes = $168,000/año
├── David Duarte: $948/mes = $11,371/año
├── Alejandro Rua: $1,380/mes = $16,560/año
└── Oscar Pérez: $1,380/mes = $16,560/año
```

### Equity JP Pineda
```
Participación: 10% (111 acciones de 1,111 total)
Vesting: 3 años, 33% anual
├── Ene 2026: 3.33% (37 acciones)
├── Ene 2027: 6.67% (74 acciones)
└── Ene 2028: 10.0% (111 acciones)
```

---
