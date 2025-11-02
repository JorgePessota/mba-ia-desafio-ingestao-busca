# 🤖 Desafio MBA Engenharia de Software com IA - Full Cycle

Este projeto faz parte do **MBA em Engenharia de Software com IA** da **Full Cycle** e tem como objetivo construir uma aplicação que realiza **ingestão de PDFs** e **responde perguntas em linguagem natural**, utilizando **LangChain**, **Google Generative AI** e **PostgreSQL com extensão PgVector**.

---

## 🧰 Tecnologias Principais
- Python 3.10+
- LangChain / LangChain Community
- Google Generative AI (Gemini)
- PostgreSQL + PgVector
- Docker / Docker Compose

---

## ⚙️ 1. Criar e Ativar o Ambiente Virtual

```bash
# Navegue até a pasta desejada
cd [pasta-do-capítulo]

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

``` 

## 📦 2. Instalar Dependências

Crie um arquivo `requirements.txt` com o seguinte conteúdo:

```txt
langchain-community
langchain-google-genai
langchain-postgres
pypdf
psycopg2-binary
python-dotenv
```

E instale:

```bash
pip install -r requirements.txt
```

## 🔐 3. Configuração das Variáveis de Ambiente

Copie o arquivo de exemplo e adicione suas credenciais:

```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicionar suas chaves

```env
GOOGLE_API_KEY=
GOOGLE_EMBEDDING_MODEL=
GOOGLE_LLM_MODEL=
DATABASE_URL=
PG_VECTOR_COLLECTION_NAME=
PDF_PATH=
```

## 🗄️ 4. Subir o Banco de Dados Vetorial (PgVector)

Certifique-se de ter o `Docker` instalado e execute:

```bash
docker compose up -d

```

## 📘 5. Executar Ingestão do PDF

```bash
python src/ingest.py

```

## 💬 6. Iniciar o Chat

```bash
python src/chat.py

```

## 🧠 7. Exemplos de Uso

Exemplo 1 — Pergunta dentro do contexto:

```makefile
PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.
```
---

Exemplo 2 — Pergunta fora do contexto:

```makefile
PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```
---

Para encerrar o chat, basta digitar `sair`

---

