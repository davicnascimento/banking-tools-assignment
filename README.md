# Banking Product Search Tool

Exercício para criar uma tool em Python que pesquisa informação bancária fictícia num ficheiro Excel e é chamada pelo agente através de tool calling.

## Objetivo

Construir um agente que recebe uma pergunta sobre produtos bancários e usa uma tool para pesquisar `data/banking_products.xlsx`.

Exemplos:

- `Qual é a taxa da conta standard?`
- `Que cartões têm cashback?`
- `Existe algum produto para estudantes?`
- `Quais são as comissões da conta premium?`

O agente deve usar a tool apenas quando a resposta depender dos dados do Excel. Não deve inventar informação que não esteja no ficheiro.

## Estrutura fornecida

```text
banking-tools-assignment/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── data/
│   └── banking_products.xlsx
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── tools.py
│   └── agent.py
└── tests/
    └── test_tools.py
```

## Tarefas

1. Criar uma feature branch no formato `feature/{nome}-tool-implementation`.
2. Copiar `.env.example` para `.env`.
3. Criar uma chave gratuita no Groq seguindo `GROQ_SETUP.md` fornecido.
4. Implementar a função `search_banking_products` em `src/tools.py`.
5. Definir o schema da tool para o modelo poder chamá-la.
6. Criar o `SYSTEM_PROMPT` em `src/agent.py`.
7. Implementar o ciclo de tool calling: enviar a pergunta, detetar a chamada da tool, executar a pesquisa e enviar o resultado de volta ao modelo.
8. Apresentar uma resposta final curta em português.
9. Adicionar testes para pesquisa por nome, categoria e ausência de resultados.
10. Testar pelo menos cinco perguntas diferentes.
11. Abrir um Pull Request para `main`.

## Dados do Excel

O ficheiro contém produtos fictícios com as colunas:

- `product_name`
- `category`
- `description`
- `monthly_fee`
- `interest_rate`
- `cashback`
- `target_customer`

A tool deve aceitar uma pesquisa textual e devolver apenas os registos relevantes. A pesquisa pode considerar `product_name`, `category`, `description` e `target_customer`.

## Regras do agente

- Usa os dados do Excel como fonte de verdade.
- Nunca inventa produtos, taxas, comissões ou benefícios.
- Se não encontrar resultados, informa claramente o utilizador.
- Não revela o conteúdo completo do ficheiro sem necessidade.
- Não pede passwords, PINs ou códigos de autenticação.
- Responde em português e em no máximo três frases.
- Não deve chamar a tool para perguntas que não estejam relacionadas com produtos bancários.

## Instalação

Requer Python 3.10 ou superior.

```bash
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
copy .env.example .env
```

Preencher `GROQ_API_KEY` no `.env`. Nunca fazer commit desse ficheiro.

## Execução

```bash
python app.py
```

## Testes

```bash
python -m pytest
```

## Critérios de aceitação

- A tool lê o ficheiro Excel sem alterar os dados.
- A pesquisa funciona sem distinguir maiúsculas e minúsculas.
- A tool devolve uma estrutura JSON previsível.
- O modelo consegue decidir quando chamar a tool.
- O resultado da tool é enviado de volta ao modelo.
- O agente não inventa informação quando não existem resultados.
- Erros de configuração e de leitura do ficheiro são apresentados claramente.
- A chave da API não aparece no código nem em commits.
