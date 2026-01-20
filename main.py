from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

@tool
def calculadora(expressao: str) -> str:
    """
    Recebe uma expressão como '128 * 46' e retorna o resultado.
    """
    try:
        # Avalia a expressão de forma simples
        # Em produção, usaríamos uma biblioteca mais segura
        resultado = eval(expressao)
        return str(resultado)
    except Exception as e:
        return f"Erro no cálculo: {e}"
