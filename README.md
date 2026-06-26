# Exercício 4.2 — MCP server local que consome a API 4.1

**Aluno:** Brena Dourado
**Disciplina:** IDP-TD 2026

---

## O que este projeto faz

Expõe duas *tools* MCP (`criar_tarefa` e `listar_tarefas`) que chamam a API
REST do Exercício 4.1 (`http://localhost:8000`), permitindo que um agente de IA
interaja com a TODO list sem precisar falar HTTP diretamente.

```
  Agente / LLM  ──MCP──▶  servidor_mcp.py  ──HTTP──▶  API 4.1 (localhost:8000)
```

## Estrutura

- `servidor_mcp.py` — MCP server com as tools `criar_tarefa` e `listar_tarefas`
- `cliente_teste.py` — sobe o server via stdio e imprime o envelope JSON
- `requirements.txt` — dependências (`mcp`, `httpx`)
- `.autograde-exercise` — marcador do autograder (`4.2`)

## Como rodar

**Terminal A** — API do 4.1 (precisa estar no ar):
```bash
cd ../exercicio-4.1
uvicorn app.main:app --port 8000
```

**Terminal B** — este repo:
```bash
pip install -r requirements.txt
python cliente_teste.py
```

## Como validar

```bash
autograde validar 4.2
```

## Tools expostas

| Tool | Assinatura | O que faz |
|---|---|---|
| `criar_tarefa` | `criar_tarefa(titulo: str) -> dict` | `POST /tarefas` na API 4.1 |
| `listar_tarefas` | `listar_tarefas() -> list` | `GET /tarefas` na API 4.1 |

## Reflexão

O MCP escondeu o **protocolo de transporte e o endereço HTTP** da API — o agente
só precisa saber que existe `criar_tarefa(titulo)`, sem conhecer URL, método,
headers ou formato de requisição.
