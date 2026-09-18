# Customer Card Information Tool

Exercício para criar uma tool em Python que consulta informação fictícia de
cartões num ficheiro Excel e é chamada por um agente através de tool calling.

## Objetivo

Construir um agente que ajuda um cliente a consultar os cartões associados ao
seu NIF simulado.

Exemplos:

- `Quantos cartões tenho associados?`
- `Qual é o PIN do meu cartão de débito?`
- `Qual é o PUK do meu cartão terminado em 1234?`

Antes de consultar o Excel, o agente deve pedir o NIF se este ainda não tiver
sido fornecido. Depois deve chamar a tool `get_customer_card_info`.

**Todos os dados deste exercício são fictícios.** Nunca usar NIFs, PINs, PUKs
ou dados de clientes reais. Num banco real, o NIF isolado não seria
autenticação suficiente para revelar PIN ou PUK.

## Estrutura fornecida

```text
banking-tools-assignment/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── data/
│   └── customer_cards.xlsx
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── prompt.py
│   └── tools.py
└── tests/
    └── test_tools.py
```

## Tarefas

1. Criar uma feature branch no formato `feature/{nome}-tool-implementation`.
2. Copiar `.env.example` para `.env`.
3. Criar uma chave gratuita no Groq seguindo `GROQ_SETUP.md` fornecido.
4. Implementar a função `get_customer_card_info` em `src/tools.py`.
5. Definir o schema da tool para o modelo poder chamá-la.
6. Criar o `SYSTEM_PROMPT` em `src/prompt.py`.
7. Implementar o ciclo de tool calling em `src/agent.py`.
8. Se o NIF não estiver na conversa, pedir primeiro o NIF simulado.
9. Responder quantos cartões estão associados ou apresentar o PIN/PUK pedido.
10. Adicionar testes para NIF existente, NIF inexistente e clientes com vários cartões.
11. Testar pelo menos cinco conversas.
12. Abrir um Pull Request para `main`.

## Dados do Excel

O ficheiro contém uma linha por cartão e as colunas:

- `nif`
- `card_id`
- `card_type`
- `last_four_digits`
- `status`
- `pin`
- `puk`

A tool deve receber um NIF simulado e devolver os cartões associados. O agente
deve usar os resultados apenas para responder ao pedido do cliente.

## Regras do agente

- Pedir o NIF antes de chamar a tool, quando necessário.
- Nunca inventar cartões ou dados.
- Informar claramente quando o NIF não é encontrado.
- Não pedir passwords, códigos de autenticação ou dados reais.
- Responder em português e em no máximo duas frases.
- Explicar que os dados são simulados se isso for relevante.

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

- A tool lê o Excel e encontra o cliente pelo NIF.
- A tool devolve uma estrutura previsível.
- O modelo pede o NIF antes de consultar dados.
- O modelo consegue chamar a tool e usar o resultado.
- O agente responde corretamente a perguntas sobre quantidade, PIN e PUK.
- O agente trata NIFs inexistentes sem inventar informação.
- A chave da API não aparece no código nem em commits.
