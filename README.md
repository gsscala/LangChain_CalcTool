
## 📋 Descrição do Projeto

Este projeto implementa um agente conversacional inteligente que combina conhecimento geral com capacidade de realizar cálculos matemáticos através de ferramentas (tools).

## 🎯 Objetivo

Criar um agente baseado em LangChain que:
- Responde perguntas de conhecimento geral diretamente
- Identifica quando uma pergunta requer cálculos matemáticos
- Utiliza uma ferramenta de calculadora customizada para resolver operações matemáticas
- Demonstra o conceito de **Tool Calling** em LLMs

## 🔧 Tecnologias Utilizadas

- **LangChain**: Framework para desenvolvimento de aplicações com LLMs
- **Ollama**: Para execução local do modelo Llama 3.1
- **Python 3.x**: Linguagem de programação
- **LangChain Tools**: Sistema de ferramentas customizadas

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/gsscala/LangChain_CalcTool
cd LangChain_CalcTool
```

2. Instale as dependências:
```bash
pip install langchain langchain_ollama langchain_core
```

3. Certifique-se de ter o Ollama instalado e o modelo Llama 3.1 disponível:
```bash
ollama pull llama3.1
```

## 🚀 Como Usar

Execute o script principal:
```bash
python main.py
```

O script executa dois testes automáticos:
1. **Teste de Conhecimento Geral**: "Quem foi Albert Einstein?"
2. **Teste de Cálculo Matemático**: "Quanto é 128 vezes quarenta e seis?"

## 🏗️ Estrutura do Código

### Componentes Principais

1. **Ferramenta Calculadora** (`@tool calculadora`):
   - Recebe expressões matemáticas como string
   - Avalia usando sintaxe Python
   - Retorna o resultado ou mensagem de erro

2. **LLM** (`ChatOllama`):
   - Modelo: Llama 3.1
   - Temperature: 0 (respostas determinísticas)

3. **Prompt Template**:
   - System: Define o comportamento do assistente
   - Instruções sobre uso correto da calculadora
   - Placeholders para histórico e scratchpad

4. **Agente**:
   - `create_tool_calling_agent`: Cria agente com capacidade de usar ferramentas
   - `AgentExecutor`: Executa o agente com verbose ativado

## 💡 Exemplos de Uso

```python
# Conhecimento Geral (sem usar calculadora)
executar_assistente("Quem foi Albert Einstein?")

# Cálculo Matemático (usa a calculadora)
executar_assistente("Quanto é 128 vezes quarenta e seis?")

# Outros exemplos possíveis:
executar_assistente("Qual é a raiz quadrada de 144?")
executar_assistente("Calcule 2 elevado a 10")
```

## 🔍 Como Funciona

1. O usuário faz uma pergunta
2. O agente analisa se precisa de ferramentas
3. **Se for conhecimento geral**: Responde diretamente
4. **Se for matemática**: 
   - Converte a pergunta em expressão Python
   - Chama a ferramenta `calculadora`
   - Retorna o resultado formatado

## ⚠️ Observações de Segurança

> **Nota**: O código utiliza `eval()` para fins demonstrativos. Como melhoria, poderia ser utilizada uma biblioteca dedicada para isso, caso contrário é possível que código malicioso seja executado