# Progreso del Proyecto - RADIKAL TECH CLUB

**Ultima actualizacion:** 27 Enero 2026
**Actualizado por:** Claude Code (Opus 4.5)

## Estado General: En track

## Resumen Ejecutivo
Radikal Tech Club es una plataforma "One-Stop Shop" de IA para comercializacion y mercadeo dirigida a MiPyMEs en Latinoamerica. Se completo la documentacion financiera, contratos de vesting (Panama y NY Law), dashboard Streamlit, y se publico el repositorio en GitHub. Proyecto listo para deploy en Streamlit Cloud y revision legal.

---

## Features/Modulos

### Completados
| Feature | Fecha | Notas |
|---------|-------|-------|
| Dashboard HTML Financiero | 27/01/2026 | 5 secciones interactivas con Chart.js |
| Dashboard Streamlit | 27/01/2026 | App Python con Plotly, lista para deploy |
| Informe de Gastos Justificados | 27/01/2026 | Total gestion JP: $53,332.31 |
| Modelo de Ingresos Calibrado | 27/01/2026 | Launch/Sell/Optimize, editable |
| Escenarios de Capital | 27/01/2026 | 4 escenarios con dilucion |
| Contrato Vesting Panama | 27/01/2026 | Ley 32/1927, arbitraje ICC |
| Contrato Vesting NY Law | 27/01/2026 | NY BCL, arbitraje AAA |
| Repositorio GitHub | 27/01/2026 | https://github.com/Fsardi19/radikal-tech-club |
| Organizacion Proyecto | 27/01/2026 | Carpetas DOCS/, LEGAL/, .gitignore |

### En Progreso
| Feature | % Avance | Bloqueadores | Proximo paso |
|---------|----------|--------------|--------------|
| Deploy Streamlit Cloud | 90% | Manual por usuario | Ir a share.streamlit.io |
| Revision legal contratos | 0% | Abogado externo | Enviar a abogado |

### Pendientes
| Feature | Prioridad | Dependencias |
|---------|-----------|--------------|
| Validar numeros con stakeholders | Alta | Ninguna |
| Pitch Deck | Media | Dashboard aprobado |
| Flujo de caja mensual | Media | Ninguna |
| Sliders interactivos | Baja | Ninguna |

---

## Estructura de Archivos del Proyecto

```
RADIKAL TECH CLUB/
├── .claude/                           # Documentacion sesiones
│   ├── SESSION_LOG.md
│   ├── PROGRESO.md                    # Este archivo
│   ├── PROMPT_APERTURA.md
│   └── RESUMEN_PROXIMA_SESION.md
├── .streamlit/
│   └── config.toml                    # Tema oscuro
├── DOCS/                              # Documentos referencia (local)
│   ├── ANALISIS/
│   │   ├── Analisis de Mercado de Servicios AI.pdf
│   │   ├── Analisis de Mercado de Servicios AI.docx
│   │   ├── Investigacion de soporte.pdf
│   │   └── Investigacion de soporte.docx
│   ├── ESTRATEGIA/
│   │   └── Plan_Estrategico_Radikal_One_Stop_Shop_v4.docx
│   └── Respuesta Propuesta Batech.docx
├── FINANCIERO/                        # Documentos financieros
│   ├── DASHBOARD_RADIKAL_2026.html    # En Git
│   ├── Inversion Radikal.xlsx         # Local
│   ├── Presupuesto Radikal 2026.xlsx  # Local
│   └── CONVERTIBLE PROMISSORY NOTE.docx
├── LEGAL/                             # Contratos (local)
│   ├── CONTRATO_VESTING_JUAN_PABLO_PINEDA.html
│   └── VESTING_AGREEMENT_JUAN_PABLO_PINEDA_NY_LAW.html
├── streamlit_app.py                   # App principal
├── requirements.txt
├── README.md
├── CLAUDE.md
└── .gitignore
```

---

## Datos Financieros Clave

### Inversion Historica
| Concepto | Monto USD |
|----------|-----------|
| Pre-JP Pineda | $60,602.97 |
| Desde JP Pineda | $53,332.31 |
| **Total** | **$113,935.27** |

### Presupuesto 2026
| Pais | Mensual | Anual | % |
|------|---------|-------|---|
| Colombia | $6,404 | $76,844 | 27.3% |
| Panama | $17,073 | $204,874 | 72.7% |
| **Total** | **$23,477** | **$281,719** | 100% |

### Modelo de Ingresos (por cliente/ano)
| Servicio | Setup | Suscripcion | Fee | Total |
|----------|-------|-------------|-----|-------|
| Launch | $800 | $900 | - | $1,700 |
| Sell | $1,500 | $1,800 | $450 | $3,750 |
| Optimize | $600 | $2,400 | - | $3,000 |

### Metricas Clave
- **Breakeven:** 102 clientes
- **ARPC:** $2,771/ano
- **% Recurrente:** 62%
- **Runway:** 4.8 meses
- **Burn Rate:** $23,477/mes

### Equity JP Pineda
| Fecha | % Grant | % Compania | Acciones |
|-------|---------|------------|----------|
| Ene 2026 | 33.33% | 3.33% | 37 |
| Ene 2027 | 66.67% | 6.67% | 74 |
| Ene 2028 | 100% | 10.0% | 111 |

**Condiciones:**
- Sin pago por acciones
- Capitalizacion pro-rata obligatoria segun % vested

---

## Enlaces Importantes

| Recurso | URL |
|---------|-----|
| GitHub Repo | https://github.com/Fsardi19/radikal-tech-club |
| Streamlit Cloud | https://share.streamlit.io (deploy pendiente) |
| Dashboard HTML | Abrir local: FINANCIERO/DASHBOARD_RADIKAL_2026.html |

---

## Decisiones Tomadas

1. **Vesting 3 anos (no 4):** Alineado con preferencia del usuario
2. **Inicio Enero 2026:** El vesting empieza inmediatamente, sin cliff
3. **Sin pago por acciones:** Solo compromiso de capitalizacion pro-rata
4. **Precios calibrados:** Para mercado MiPyMEs Colombia
5. **Visualizacion HTML/Streamlit:** Preferido sobre Markdown
6. **Archivos sensibles locales:** .xlsx, .docx, LEGAL/ no van a Git
7. **Arbitraje:** ICC para Panama, AAA para NY

---

## Notas para el Equipo

### Para Deploy en Streamlit
1. Ir a https://share.streamlit.io
2. Click "New app"
3. Seleccionar `Fsardi19/radikal-tech-club`
4. Branch: `main`, File: `streamlit_app.py`
5. Deploy

### Para Revision Legal
- Enviar LEGAL/CONTRATO_VESTING_*.html a abogado
- Panama Law: arbitraje ICC, Ley 32/1927
- NY Law: arbitraje AAA, NY BCL

### Contactos del Proyecto
- CEO: Juan Pablo Pineda
- Equipo tecnico: Alejandro Rua, Oscar Perez, David Duarte

---

## Historial de Versiones

| Fecha | Version | Cambios |
|-------|---------|---------|
| 27/01/2026 | 2.0 | Contratos vesting, Streamlit, GitHub, reorganizacion |
| 27/01/2026 | 1.0 | Dashboard HTML inicial, documentacion |

---
