import streamlit as st
from datetime import datetime

# ========== CONFIGURAÇÃO BÁSICA DO PAINEL ==========
st.set_page_config(page_title="Central de Dashboards", layout="wide")

# ========== ESTILO PERSONALIZADO ==========
st.markdown("""
    <style>
    /* Fonte e fundo */
    body, .stApp {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Cabeçalho com logo e data */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 10px;
    }

    .logo-container img {
        height: 80px;
        margin-bottom: 30px;
    }

    .data-container {
        font-size: 18px;
        font-weight: 600;
        color: #333;
    }

    /* Título principal */
    .titulo {
        font-size: 40px;
        font-weight: 800;
        color: #0A5272;
        margin-bottom: 10px;
    }

    /* Markdown */
    .markdown-section {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    .sidebar .css-1d391kg {
        background-color: #eaf4fc;
    }
    </style>
""", unsafe_allow_html=True)

# ========== CABEÇALHO COM LOGO E DATA ==========
st.markdown(f"""
    <div class="header-container">
        <div class="logo-container">
            <img src="https://isoolhos.com/wp-content/uploads/2021/06/logo.svg">
        </div>
        <div class="data-container">
            📅 {datetime.today().strftime('%d/%m/%Y')}
        </div>
    </div>
""", unsafe_allow_html=True)


# ========== MENU LATERAL ==========
opcao = st.sidebar.selectbox(
    "📂 Escolha o painel",
    ["🏠 Home", "🏥 Centro Diagnóstico", "💻 Senhas Pendentes", "📦 Ordem de Compras", "🩺 Acompanhamento de Consultas"]
)

# ========== NAVEGAÇÃO ==========
if opcao == "🏠 Home":
    st.markdown('<div class="titulo">📊 Central de Dashboards</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="markdown-section">
        <p>Bem-vindo à <strong>Central de Dashboards</strong>!</p>
        <p>Aqui você encontra acesso rápido e visual aos principais indicadores estratégicos da organização.</p>
        <ul>
            <li>🏥 Centro de Diagnóstico</li>
            <li>📦 Ordem de Compras</li>
            <li>🩺 Acompanhamento de Consultas</li>
            <li>💻 Senhas Pendentes</li>
        </ul>
        <p>Selecione uma das opções no menu lateral para visualizar o painel desejado.</p>
    </div>
    """, unsafe_allow_html=True)

elif opcao == "🏥 Centro Diagnóstico":
    st.markdown('<div class="titulo">🏥 Centro Diagnóstico</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="markdown-section">
        <p>Painel com dados e informações sobre o centro diagnóstico.</p>
        <p><a href="http://10.1.1.63:8501" target="_blank">🔗 Clique aqui para abrir o painel em nova aba</a></p>
    </div>
    """, unsafe_allow_html=True)

elif opcao == "📦 Ordem de Compras":
    st.markdown('<div class="titulo">📦 Ordem de Compras</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="markdown-section">
        <p>Painel com indicadores sobre ordens de compras aprovadas.</p>
        <p><a href="http://10.1.1.63:8502" target="_blank">🔗 Clique aqui para abrir o painel em nova aba</a></p>
    </div>
    """, unsafe_allow_html=True)

elif opcao == "🩺 Acompanhamento de Consultas":
    st.markdown('<div class="titulo">🩺 Acompanhamento de Consultas</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="markdown-section">
        <p>Painel com dados de acompanhamento clínico.</p>
        <p><a href="http://10.1.1.63:8503" target="_blank">🔗 Clique aqui para abrir o painel em nova aba</a></p>
    </div>
    """, unsafe_allow_html=True)

elif opcao == "💻 Senhas Pendentes":
    st.markdown('<div class="titulo">💻 Senhas Pendentes</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="markdown-section">
        <p>Painel com informações sobre as senhas em análise.</p>
        <p><a href="http://10.1.1.63:8504" target="_blank">🔗 Clique aqui para abrir o painel em nova aba</a></p>
    </div>
    """, unsafe_allow_html=True)
