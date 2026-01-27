"""
RADIKAL TECH CLUB - Dashboard Financiero Interactivo 2026
Plataforma One-Stop Shop IA para MiPyMEs LATAM
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page config
st.set_page_config(
    page_title="RADIKAL TECH CLUB - Dashboard Financiero 2026",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #e94560, #00d9a5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
    }
    .metric-label {
        font-size: 0.85rem;
        opacity: 0.8;
    }
    .highlight-box {
        background: linear-gradient(135deg, #e94560, #ff6b6b);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    .success-box {
        background: linear-gradient(135deg, #00d9a5, #4dffc3);
        padding: 2rem;
        border-radius: 15px;
        color: #1a1a2e;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for services
if 'servicios' not in st.session_state:
    st.session_state.servicios = [
        {'nombre': 'Radikal Launch', 'setup': 800, 'mensual': 75, 'fee_pauta': 0, 'pauta_mensual': 0, 'clientes': 25, 'descripcion': 'De idea a marca, landing, kit de contenidos'},
        {'nombre': 'Radikal Sell', 'setup': 1500, 'mensual': 150, 'fee_pauta': 15, 'pauta_mensual': 250, 'clientes': 25, 'descripcion': 'Sistema de venta completo: tienda, campañas, automatizaciones'},
        {'nombre': 'Radikal Optimize', 'setup': 600, 'mensual': 200, 'fee_pauta': 0, 'pauta_mensual': 0, 'clientes': 10, 'descripcion': 'Diagnóstico 360°, sondeos, tests A/B'}
    ]

if 'gastos_colombia' not in st.session_state:
    st.session_state.gastos_colombia = [
        {'concepto': 'Juan Pablo Pineda (CEO)', 'mensual_cop': 14000000},
        {'concepto': 'David Duarte', 'mensual_cop': 2500000},
        {'concepto': 'Servicios Legales', 'mensual_cop': 416667},
        {'concepto': 'Auxilio Conectividad', 'mensual_cop': 100000},
        {'concepto': 'Cámara de Comercio', 'mensual_cop': 28825}
    ]

if 'gastos_panama' not in st.session_state:
    st.session_state.gastos_panama = [
        {'concepto': 'Juan Pablo Pineda (CEO)', 'mensual_usd': 14000},
        {'concepto': 'Alejandro Rua', 'mensual_usd': 1380},
        {'concepto': 'Oscar Pérez', 'mensual_usd': 1380},
        {'concepto': 'Legales', 'mensual_usd': 125},
        {'concepto': 'Google Workspace', 'mensual_usd': 88},
        {'concepto': 'Shopify', 'mensual_usd': 25},
        {'concepto': 'ChatGPT', 'mensual_usd': 20},
        {'concepto': 'Contabo', 'mensual_usd': 5.40},
        {'concepto': 'Freepik', 'mensual_usd': 6.98},
        {'concepto': 'Apify', 'mensual_usd': 42.47}
    ]

if 'trm' not in st.session_state:
    st.session_state.trm = 3650

# Constants
CAPITAL_ACTUAL = 113935
INVERSION_DESDE_JP = 53332.31

# Helper functions
def calcular_ingreso_cliente(servicio):
    suscripcion_anual = servicio['mensual'] * 12
    fee_anual = (servicio['fee_pauta'] / 100) * servicio['pauta_mensual'] * 12
    return servicio['setup'] + suscripcion_anual + fee_anual

def calcular_total_ingresos():
    total = 0
    for s in st.session_state.servicios:
        total += calcular_ingreso_cliente(s) * s['clientes']
    return total

def calcular_total_gastos():
    trm = st.session_state.trm
    total_colombia = sum(g['mensual_cop'] for g in st.session_state.gastos_colombia) / trm * 12
    total_panama = sum(g['mensual_usd'] for g in st.session_state.gastos_panama) * 12
    return total_colombia + total_panama

# Header
st.markdown('<h1 class="main-header">RADIKAL TECH CLUB</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Dashboard Financiero Interactivo 2026 - Plataforma One-Stop Shop IA para MiPyMEs</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/rocket.png", width=80)
    st.title("Configuración")

    st.session_state.trm = st.number_input("TRM (COP/USD)", value=st.session_state.trm, step=50)

    st.markdown("---")
    st.markdown("### Datos Clave")
    st.metric("Capital Actual", f"${CAPITAL_ACTUAL:,.0f}")
    st.metric("Inversión Desde JP", f"${INVERSION_DESDE_JP:,.2f}")

    st.markdown("---")
    st.markdown("### Equipo")
    st.markdown("👤 **CEO:** Juan Pablo Pineda")
    st.markdown("👥 **Tech:** A. Rua, O. Pérez, D. Duarte")

# Main tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Informe Financiero",
    "💰 Modelo de Ingresos",
    "📋 Presupuesto 2026",
    "📈 Escenarios de Capital",
    "🤝 Equity Agreement"
])

# TAB 1: Informe Financiero
with tab1:
    st.header("Informe Financiero - Inversión Bajo Gestión JP Pineda")

    # Highlight box
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="highlight-box">
            <h3>Inversión Total Bajo Gestión JP Pineda</h3>
            <div style="font-size: 2.5rem; font-weight: bold;">${INVERSION_DESDE_JP:,.2f} USD</div>
            <p>Período: Enero 2025 - Presente</p>
        </div>
        """, unsafe_allow_html=True)

    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Inversión Pre-JP", "$60,602.97", delta=None)
    with col2:
        st.metric("Inversión Desde JP", f"${INVERSION_DESDE_JP:,.2f}", delta="Gestión actual")
    with col3:
        st.metric("Total Histórico", "$113,935.27", delta=None)

    st.markdown("---")

    # Distribution chart
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribución por Jurisdicción")
        jurisdiccion_data = pd.DataFrame({
            'Jurisdicción': ['Radikal Colombia', 'Radikal Panamá', 'Radikal USA'],
            'Monto': [6893.12, 37467.19, 8972.00],
            'Porcentaje': [12.9, 70.3, 16.8]
        })

        fig = px.pie(jurisdiccion_data, values='Monto', names='Jurisdicción',
                     color_discrete_sequence=['#6c5ce7', '#00cec9', '#fdcb6e'],
                     hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Detalle por País")
        st.dataframe(jurisdiccion_data.style.format({
            'Monto': '${:,.2f}',
            'Porcentaje': '{:.1f}%'
        }), use_container_width=True)

    # Justification table
    st.subheader("Justificación de Gastos")
    gastos_detalle = pd.DataFrame([
        {'País': 'COLOMBIA', 'Concepto': 'Juan Pablo Pineda (CEO)', 'Monto USD': 6506.19, 'Justificación': 'Dirección estratégica'},
        {'País': 'COLOMBIA', 'Concepto': 'Legal', 'Monto USD': 222.07, 'Justificación': 'Estructuración corporativa'},
        {'País': 'COLOMBIA', 'Concepto': 'Reembolso Apps', 'Monto USD': 164.86, 'Justificación': 'Herramientas digitales'},
        {'País': 'PANAMÁ', 'Concepto': 'Juan Pablo Pineda', 'Monto USD': 22627.00, 'Justificación': 'Gestión regional'},
        {'País': 'PANAMÁ', 'Concepto': 'Alejandro Rua', 'Monto USD': 1380.00, 'Justificación': 'Desarrollo técnico'},
        {'País': 'PANAMÁ', 'Concepto': 'Oscar Pérez', 'Monto USD': 1380.00, 'Justificación': 'Desarrollo técnico'},
        {'País': 'PANAMÁ', 'Concepto': 'Infraestructura Digital', 'Monto USD': 690.46, 'Justificación': 'Google, GoDaddy, etc.'},
        {'País': 'PANAMÁ', 'Concepto': 'Legales Panamá', 'Monto USD': 11389.73, 'Justificación': 'Constitución y compliance'},
        {'País': 'USA', 'Concepto': 'Firstbase', 'Monto USD': 2780.00, 'Justificación': 'Incorporación'},
        {'País': 'USA', 'Concepto': 'Lok Foods', 'Monto USD': 1547.46, 'Justificación': 'Cliente piloto'},
        {'País': 'USA', 'Concepto': 'Karu', 'Monto USD': 4644.88, 'Justificación': 'Cliente estratégico'},
    ])
    st.dataframe(gastos_detalle.style.format({'Monto USD': '${:,.2f}'}), use_container_width=True)

# TAB 2: Modelo de Ingresos
with tab2:
    st.header("Modelo de Ingresos - Editor de Servicios")

    st.info("💡 **Editor de Servicios** - Modifica precios, cantidades y agrega nuevos servicios. Los cálculos se actualizan automáticamente.")

    # Service editor
    for i, servicio in enumerate(st.session_state.servicios):
        with st.expander(f"🎯 {servicio['nombre']}", expanded=True):
            col1, col2 = st.columns([3, 1])
            with col1:
                servicio['nombre'] = st.text_input("Nombre", servicio['nombre'], key=f"nombre_{i}")
                servicio['descripcion'] = st.text_input("Descripción", servicio['descripcion'], key=f"desc_{i}")
            with col2:
                if st.button("🗑️ Eliminar", key=f"del_{i}"):
                    st.session_state.servicios.pop(i)
                    st.rerun()

            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                servicio['setup'] = st.number_input("Setup (USD)", value=servicio['setup'], step=100, key=f"setup_{i}")
            with col2:
                servicio['mensual'] = st.number_input("Mensual (USD)", value=servicio['mensual'], step=25, key=f"mensual_{i}")
            with col3:
                servicio['fee_pauta'] = st.number_input("Fee Pauta (%)", value=servicio['fee_pauta'], step=5, key=f"fee_{i}")
            with col4:
                servicio['pauta_mensual'] = st.number_input("Pauta Mensual", value=servicio['pauta_mensual'], step=50, key=f"pauta_{i}")
            with col5:
                servicio['clientes'] = st.number_input("# Clientes", value=servicio['clientes'], step=5, key=f"clientes_{i}")

            ingreso_cliente = calcular_ingreso_cliente(servicio)
            ingreso_total = ingreso_cliente * servicio['clientes']

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Ingreso/Cliente/Año", f"${ingreso_cliente:,.0f}")
            with col2:
                st.metric("Ingreso Total Anual", f"${ingreso_total:,.0f}")

    # Add service button
    if st.button("➕ Agregar Nuevo Servicio"):
        st.session_state.servicios.append({
            'nombre': 'Nuevo Servicio',
            'setup': 500,
            'mensual': 100,
            'fee_pauta': 0,
            'pauta_mensual': 0,
            'clientes': 10,
            'descripcion': 'Descripción del nuevo servicio'
        })
        st.rerun()

    st.markdown("---")

    # Summary
    st.subheader("Resumen de Ingresos Proyectados")

    total_clientes = sum(s['clientes'] for s in st.session_state.servicios)
    total_setups = sum(s['setup'] * s['clientes'] for s in st.session_state.servicios)
    total_mrr = sum(s['mensual'] * s['clientes'] for s in st.session_state.servicios)
    total_fee = sum((s['fee_pauta']/100) * s['pauta_mensual'] * 12 * s['clientes'] for s in st.session_state.servicios)
    total_arr = total_mrr * 12
    total_ingresos = calcular_total_ingresos()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Clientes", total_clientes)
    with col2:
        st.metric("Ingresos por Setups", f"${total_setups:,.0f}")
    with col3:
        st.metric("MRR (Mensual)", f"${total_mrr:,.0f}")
    with col4:
        st.metric("Fee de Pauta Anual", f"${total_fee:,.0f}")

    # Highlight total
    st.markdown(f"""
    <div class="success-box">
        <h3>Ingresos Anuales Proyectados</h3>
        <div style="font-size: 2.5rem; font-weight: bold;">${total_ingresos:,.0f}</div>
        <p>{(total_arr/total_ingresos*100):.1f}% recurrente (suscripciones)</p>
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    arpc = total_ingresos / total_clientes if total_clientes > 0 else 0
    with col1:
        st.metric("ARPC (Promedio/Cliente)", f"${arpc:,.0f}")
    with col2:
        st.metric("LTV Estimado (3 años)", f"${arpc * 2.1:,.0f}")
    with col3:
        st.metric("MRR Proyectado", f"${total_mrr:,.0f}")
    with col4:
        st.metric("ARR Proyectado", f"${total_arr:,.0f}")

    # Chart
    servicios_df = pd.DataFrame([{
        'Servicio': s['nombre'],
        'Ingresos': calcular_ingreso_cliente(s) * s['clientes'],
        'Clientes': s['clientes']
    } for s in st.session_state.servicios])

    fig = px.bar(servicios_df, x='Servicio', y='Ingresos', color='Servicio',
                 color_discrete_sequence=['#6c5ce7', '#00cec9', '#fdcb6e', '#e94560'])
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# TAB 3: Presupuesto 2026
with tab3:
    st.header("Presupuesto Integral 2026 - Ingresos vs Gastos")

    ingresos = calcular_total_ingresos()
    gastos = calcular_total_gastos()
    resultado = ingresos - gastos

    # Two columns for income and expenses
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💚 INGRESOS PROYECTADOS")

        # Income breakdown
        income_data = []
        for s in st.session_state.servicios:
            income_data.append({
                'Concepto': f"{s['nombre']} ({s['clientes']} clientes)",
                'Monto': calcular_ingreso_cliente(s) * s['clientes']
            })

        income_df = pd.DataFrame(income_data)
        st.dataframe(income_df.style.format({'Monto': '${:,.0f}'}), use_container_width=True)

        st.metric("TOTAL INGRESOS ANUALES", f"${ingresos:,.0f}")

    with col2:
        st.subheader("🔴 GASTOS OPERATIVOS")

        # Colombia expenses
        st.markdown("**Colombia**")
        colombia_df = pd.DataFrame(st.session_state.gastos_colombia)
        colombia_df['Mensual USD'] = colombia_df['mensual_cop'] / st.session_state.trm
        colombia_df['Anual USD'] = colombia_df['Mensual USD'] * 12
        st.dataframe(colombia_df[['concepto', 'Mensual USD', 'Anual USD']].style.format({
            'Mensual USD': '${:,.0f}',
            'Anual USD': '${:,.0f}'
        }), use_container_width=True)

        # Panama expenses
        st.markdown("**Panamá**")
        panama_df = pd.DataFrame(st.session_state.gastos_panama)
        panama_df['Anual USD'] = panama_df['mensual_usd'] * 12
        st.dataframe(panama_df[['concepto', 'mensual_usd', 'Anual USD']].rename(columns={'mensual_usd': 'Mensual USD'}).style.format({
            'Mensual USD': '${:,.0f}',
            'Anual USD': '${:,.0f}'
        }), use_container_width=True)

        st.metric("TOTAL GASTOS ANUALES", f"${gastos:,.0f}")

    st.markdown("---")

    # Result
    st.subheader("RESULTADO OPERACIONAL")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Ingresos Anuales", f"${ingresos:,.0f}")
    with col2:
        st.metric("Gastos Anuales", f"${gastos:,.0f}")
    with col3:
        delta_color = "normal" if resultado >= 0 else "inverse"
        st.metric("Resultado Neto", f"${resultado:,.0f}", delta="Superávit" if resultado >= 0 else "Déficit")
    with col4:
        margen = (resultado / ingresos * 100) if ingresos > 0 else 0
        st.metric("Margen Operativo", f"{margen:.1f}%")

    # Result box
    if resultado >= 0:
        st.success(f"### ✅ SUPERÁVIT OPERACIONAL: +${resultado:,.0f}\nLa operación es autosostenible con las proyecciones actuales")
    else:
        st.error(f"### ⚠️ DÉFICIT OPERACIONAL: -${abs(resultado):,.0f}\nSe requiere aporte de capital adicional")

    # Additional metrics
    st.markdown("---")
    burn_rate = gastos / 12
    runway = CAPITAL_ACTUAL / burn_rate if burn_rate > 0 else 0
    clientes_breakeven = int(gastos / arpc) if arpc > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Burn Rate Mensual", f"${burn_rate:,.0f}")
    with col2:
        st.metric("Runway Actual", f"{runway:.1f} meses")
    with col3:
        st.metric("Clientes para Breakeven", clientes_breakeven)
    with col4:
        if total_clientes >= clientes_breakeven:
            st.metric("Estado Breakeven", "✅ Logrado")
        else:
            st.metric("Estado Breakeven", "⏳ Pendiente")

# TAB 4: Escenarios de Capital
with tab4:
    st.header("Análisis de Necesidades de Capital")

    ingresos = calcular_total_ingresos()
    gastos = calcular_total_gastos()
    resultado = ingresos - gastos

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Capital Actual Disponible", f"${CAPITAL_ACTUAL:,.0f}")
    with col2:
        if resultado >= 0:
            st.metric("Superávit Proyectado", f"+${resultado:,.0f}")
        else:
            st.metric("Déficit Proyectado", f"-${abs(resultado):,.0f}")
    with col3:
        capital_req = max(0, abs(resultado) - CAPITAL_ACTUAL) if resultado < 0 else 0
        st.metric("Capital Adicional Requerido", f"${capital_req:,.0f}")

    st.markdown("---")

    # Scenarios
    st.subheader("Escenarios de Sensibilidad")

    valoracion = st.number_input("Valoración Pre-Money (USD)", value=500000, step=50000)

    escenarios = [
        {'nombre': 'Pesimista', 'porcentaje': 50, 'color': '#e94560'},
        {'nombre': 'Conservador', 'porcentaje': 75, 'color': '#ffc107'},
        {'nombre': 'Base', 'porcentaje': 100, 'color': '#00d9a5'},
        {'nombre': 'Optimista', 'porcentaje': 125, 'color': '#00cec9'},
    ]

    escenarios_data = []
    for esc in escenarios:
        ing_esc = ingresos * (esc['porcentaje'] / 100)
        deficit_esc = ing_esc - gastos
        capital_req_esc = max(0, abs(deficit_esc)) if deficit_esc < 0 else 0
        equity_ceder = (capital_req_esc / (valoracion + capital_req_esc) * 100) if capital_req_esc > 0 else 0

        escenarios_data.append({
            'Escenario': esc['nombre'],
            '% Cumplimiento': f"{esc['porcentaje']}%",
            'Ingresos': ing_esc,
            'Resultado': deficit_esc,
            'Capital Req.': capital_req_esc,
            'Equity a Ceder': equity_ceder,
            'Fundadores Post': 90 - equity_ceder * 0.9,
            'JP Pineda Post': 10 - equity_ceder * 0.1
        })

    escenarios_df = pd.DataFrame(escenarios_data)
    st.dataframe(escenarios_df.style.format({
        'Ingresos': '${:,.0f}',
        'Resultado': '${:,.0f}',
        'Capital Req.': '${:,.0f}',
        'Equity a Ceder': '{:.1f}%',
        'Fundadores Post': '{:.1f}%',
        'JP Pineda Post': '{:.1f}%'
    }), use_container_width=True)

    # Chart
    fig = go.Figure()
    for esc in escenarios_data:
        fig.add_trace(go.Bar(
            name=esc['Escenario'],
            x=[esc['Escenario']],
            y=[esc['Ingresos']],
            marker_color=escenarios[[e['nombre'] for e in escenarios].index(esc['Escenario'])]['color']
        ))
    fig.add_hline(y=gastos, line_dash="dash", line_color="red", annotation_text="Breakeven")
    fig.update_layout(title="Ingresos por Escenario vs Breakeven", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# TAB 5: Equity Agreement
with tab5:
    st.header("Equity Vesting Agreement - Juan Pablo Pineda (CEO)")

    st.markdown("""
    <div class="highlight-box">
        <h3>Equity Vesting Agreement</h3>
        <div style="font-size: 2rem; font-weight: bold;">10% de participación | Vesting de 3 años | Inicio: Enero 2026</div>
    </div>
    """, unsafe_allow_html=True)

    # Vesting timeline
    st.subheader("Cronograma de Vesting (3 Años - 33% Anual)")

    vesting_data = pd.DataFrame([
        {'Fecha': '1 Enero 2026', 'Acciones': 37, 'Acumulado': 37, '% Grant': '33.33%', '% Compañía': '3.33%'},
        {'Fecha': '1 Enero 2027', 'Acciones': 37, 'Acumulado': 74, '% Grant': '66.67%', '% Compañía': '6.67%'},
        {'Fecha': '1 Enero 2028', 'Acciones': 37, 'Acumulado': 111, '% Grant': '100%', '% Compañía': '10.0%'},
    ])

    st.dataframe(vesting_data, use_container_width=True)

    # Visual timeline
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #1a1a2e; border-radius: 15px; color: white;">
            <div style="font-size: 2rem; font-weight: bold; color: #00d9a5;">33%</div>
            <div><strong>Año 1</strong></div>
            <div style="color: #888;">Ene 2026</div>
            <div style="color: #00d9a5;">3.33%</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #1a1a2e; border-radius: 15px; color: white;">
            <div style="font-size: 2rem; font-weight: bold; color: #00d9a5;">66%</div>
            <div><strong>Año 2</strong></div>
            <div style="color: #888;">Ene 2027</div>
            <div style="color: #00d9a5;">6.67%</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #e94560; border-radius: 15px; color: white;">
            <div style="font-size: 2rem; font-weight: bold;">100%</div>
            <div><strong>Año 3</strong></div>
            <div style="color: rgba(255,255,255,0.8);">Ene 2028</div>
            <div>10.0%</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Share structure
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Acciones Pre-Grant", "1,000")
    with col2:
        st.metric("Nuevas Acciones", "111")
    with col3:
        st.metric("Total Post-Grant", "1,111")

    # Terms
    st.subheader("Términos Principales")

    terms = [
        ("1. Período de Vesting", "3 años, 33.33% anual. Primer vesting en Enero 2026."),
        ("2. Capitalización Pro-Rata", "JP debe participar en capital calls según su % vested."),
        ("3. Good Leaver", "Retiene acciones vesteadas. No vesteadas se pierden."),
        ("4. Bad Leaver", "Compañía puede recomprar todas las acciones al menor valor."),
        ("5. Change of Control", "100% aceleración si venta/fusión con <50% retención."),
        ("6. Pro-Rata Rights", "Derecho a participar en futuras rondas."),
        ("7. Restricciones", "Transferencia solo con consentimiento del Board."),
        ("8. No Competencia", "12 meses post-terminación."),
        ("9. Ley Aplicable", "República de Panamá, arbitraje ICC."),
    ]

    for title, desc in terms:
        with st.expander(title):
            st.write(desc)

    # Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=['Ene 2026', 'Ene 2027', 'Ene 2028'],
        y=[3.33, 6.67, 10.0],
        mode='lines+markers',
        name='% Compañía',
        line=dict(color='#00d9a5', width=3),
        marker=dict(size=15)
    ))
    fig.update_layout(
        title="Evolución de Participación de JP Pineda",
        yaxis_title="% de la Compañía",
        yaxis=dict(range=[0, 12])
    )
    st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p><strong>RADIKAL TECH CLUB</strong> - Dashboard Financiero Interactivo 2026</p>
    <p style="font-size: 0.8rem;">Plataforma One-Stop Shop IA para MiPyMEs LATAM</p>
    <p style="font-size: 0.75rem; color: #999;">Generado con Streamlit | Enero 2026</p>
</div>
""", unsafe_allow_html=True)
