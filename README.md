# Investment AI Agent Team

![Python](https://img.shields.io/badge/python-3.13-blue)
![Agno](https://img.shields.io/badge/agno-1.7.11-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 🔹 Sobre o Projeto

O Investment AI Agent Team é um sistema de agentes inteligentes focado no mercado de ações dos Estados Unidos, executado diretamente no terminal.
O projeto combina análise quantitativa e análise qualitativa para fornecer informações consolidadas sobre ações em formato de chat interativo, ajudando usuários a entender o que os dados e as notícias recentes indicam sobre comprar ou esperar para cada ativo.

---

## 🎯 Objetivo

- Criar agentes especializados que trabalham em conjunto para analisar o mercado americano.

- Obter dados quantitativos sobre ações (preço atual, histórico, recomendações de analistas).

- Extrair informações qualitativas de notícias recentes e relatórios.

- Consolidar resultados em uma tabela ASCII com nome da ação, preço, recomendação e motivo principal, podendo fornecer links externos para facilitar o entendimento do usuário.

- Permitir interação contínua via chat no terminal.

---

## 🛠 Tecnologias e Ferramentas

- **Python 3.13**
- **[Agno](https://github.com/google/agno)** (versão 1.7.11)
- **YFinanceTools** para dados financeiros
- **FinancialDatasetsTools** para dados históricos e análises de mercado
- **GoogleSearchTools** e **WebBrowserTools** para pesquisas de notícias
- **dotenv** para variáveis de ambiente

---

## 📸 Demonstração na Prática

Veja abaixo algumas imagens do **Investment AI Agent Team** rodando diretamente no terminal, mostrando as análises de ações e recomendações consolidadas em tabelas ASCII:

![Etapa de Raciocinar](docs-imgs/Reasoning-step.jpg)
![Etapa de Responder](docs-imgs/Response-step.jpg)

---

## 📚 Exemplos de uso (inputs)
- "Compare the performance of US tech companies and bring me the latest news about the sector."

- "Give me insights on the US stock market and summarize recent research on artificial intelligence applied to finance."

- "Show me the best-performing US stocks this year and recent headlines about them."

---

## ⚙️ Configuração do Projeto

1. Crie um **.venv**:
```bash

python -m venv .venv
```

2. Ative o **.venv**
- Windows
```bash

.venv\Scripts\activate
```
- Linux
```bash

source .venv/bin/activate
```

3. Instale as dependências:
```bash

pip install -r requirements.txt
```

4. Crie um arquivo **.env** na raiz do seu projeto com suas chaves:
```
GOOGLE_API_KEY=your_google_api_key_here
FINANCIAL_DATASETS_API_KEY=your_financial_datasets_api_key_here
```

---

## 🚀 Como Rodar
Execute no terminal:
```bash

python main.py
```

O sistema iniciará um chat interativo no terminal, onde você pode digitar perguntas sobre ações e receber análises dos agentes.
Se quiser encerrar o chat digite `quit`, `exit` ou `bye`.

---

## 📝 Estrutura do Projeto

```bash

investment-ai-agent-team/
│
├─ agents/
│  ├─ financial_agent.py
│  └─ news_agent.py
│
├─ main.py
├─ .env
├─ requirements.txt
├─ README.md
└─ .gitignore
```

---

## ⚖️ Licença

Este projeto está licenciado sob a MIT License.