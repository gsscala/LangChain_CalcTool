from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

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


llm = ChatOllama(model="llama3.1", temperature=0)

tools = [calculadora]

system_prompt = ("Você é um assistente prestativo que pode responder perguntas gerais ou usar uma calculadora para matemática."
    " Para usar a calculadora, você deve garantir que sua expressão seja resolvível pela sintaxe do Python. Ou seja, "
    "1 + 1, 2 * 3, 4 / 9, 2 ** (1/2), 0.5 / 9")

# O agente decide se usa a ferramenta ou responde diretamente 
agent_executor = create_agent(llm, tools, system_prompt=system_prompt)

def executar_assistente(pergunta):
    print(f"\n--- Pergunta: {pergunta} ---")
    resposta = agent_executor.invoke({"messages": [("user", pergunta)]})
    print(f"Resposta Final: {resposta['messages'][-1].content}")

if __name__ == "__main__":
    # Teste 1: Conhecimento Geral (Deve responder sozinho)
    executar_assistente("Quem foi Albert Einstein?")
    
    # Teste 2: Matemática (Deve acionar a calculadora)
    executar_assistente("Quanto é 128 vezes quarenta e seis?")
    
    executar_assistente("Qual é a raiz quadrada de 144?")
    executar_assistente("Qual é a raiz quadrada do sexto inteiro positivo?")
    
    executar_assistente("Calcule dois elevado a 10")