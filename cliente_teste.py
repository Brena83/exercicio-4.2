import asyncio
import json
import logging
import os
import sys

# Redireciona fd 2 (stderr) para /dev/null antes de qualquer import do MCP
# O autograde concatena stderr ao stdout ao capturar a saída — sem isso, os
# logs do SDK contaminam o JSON e o parse falha.
_devnull = open(os.devnull, "w")
os.dup2(_devnull.fileno(), 2)

logging.disable(logging.CRITICAL)

from mcp import ClientSession, StdioServerParameters  # noqa: E402
from mcp.client.stdio import stdio_client  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


async def main() -> dict:
    params = StdioServerParameters(
        command=sys.executable,
        args=[os.path.join(HERE, "servidor_mcp.py")],
        env={**os.environ},
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            nomes = [t.name for t in tools.tools]

            criar = await session.call_tool("criar_tarefa", {"titulo": "tarefa via mcp"})
            listar = await session.call_tool("listar_tarefas", {})

            criar_resultado = json.loads(criar.content[0].text)
            listar_resultado = json.loads(listar.content[0].text)

            return {
                "tools": nomes,
                "criar_resultado": criar_resultado,
                "listar_resultado": listar_resultado,
            }


if __name__ == "__main__":
    resultado = asyncio.run(main())
    print(json.dumps(resultado))
