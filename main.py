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


llm = ChatOllama(model="llama3", temperature=0)

tools = [calculadora]

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente prestativo que pode responder perguntas gerais ou usar uma calculadora para matemática."
        " Para usar a calculadora, você deve garantir que sua expressão seja resolvível pela sintaxe do Python. Ou seja, "
        "1 + 1, 2 * 3, 4 / 9, 2 ** (1/2), 0.5 / 9"),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])
