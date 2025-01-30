# **LangChain: The Ultimate Guide with Code Examples**  

## **📌 Introduction**  
LangChain is an open-source framework designed to build applications powered by **large language models (LLMs)** like OpenAI’s GPT, Hugging Face models, and Anthropic’s Claude. It allows developers to create **prompt pipelines, autonomous agents, memory-enabled chatbots, and retrieval-augmented generation (RAG) systems** with ease.  

**💡 Why Use LangChain?**  
- Modular and composable architecture  
- Supports multiple LLM providers (OpenAI, Hugging Face, etc.)  
- Handles **prompt management, chains, memory, and agents**  
- Provides **retrieval mechanisms (vector databases, FAISS, Pinecone, ChromaDB, etc.)**  
- Enables **autonomous agents** that can use tools like search engines and APIs  

---

## **🔧 1. Installing LangChain**  
Before diving in, install LangChain and other dependencies:  

```bash
pip install langchain openai faiss-cpu chromadb tiktoken
```

- `langchain` → Core framework  
- `openai` → OpenAI LLM integration  
- `faiss-cpu` → Vector store for retrieval  
- `chromadb` → Alternative vector store  
- `tiktoken` → Tokenizer for OpenAI models  

---

# **📂 2. Core Components of LangChain**  
LangChain is built on **six key components**:  
1️⃣ **LLMs** – Integrates with OpenAI, Hugging Face, and other models  
2️⃣ **Prompt Templates** – Structures inputs for LLMs  
3️⃣ **Chains** – Sequences multiple steps together  
4️⃣ **Memory** – Stores chat history and maintains context  
5️⃣ **Agents** – Uses LLMs to interact with external tools  
6️⃣ **Retrieval (Vector Stores)** – Searches stored documents  

---

# **📌 3. Large Language Models (LLMs) in LangChain**  

## **🧠 Using OpenAI’s GPT Model**
```python
from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003", openai_api_key="your-api-key")
response = llm.predict("What are the benefits of AI?")
print(response)
```

## **🧠 Using Hugging Face Models**
```python
from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature": 0.5})
response = llm.predict("Explain machine learning.")
print(response)
```

---

# **📌 4. Prompt Templates**  
A **PromptTemplate** structures user input before sending it to an LLM.  

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms."
)

formatted_prompt = prompt.format(topic="Quantum Computing")
print(formatted_prompt)
```

🔹 **Why use Prompt Templates?**  
- Helps **reuse and standardize** prompts  
- Ensures consistency in AI responses  

---

# **📌 5. Chains: Connecting Multiple Components**  
A **Chain** is a sequence of modular components linked together.  

## **🛠 Simple LLMChain Example**
```python
from langchain.chains import LLMChain
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="your-api-key")

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in one paragraph."
)

chain = LLMChain(llm=llm, prompt=prompt)
response = chain.run("Blockchain")
print(response)
```

🔹 **Common Chains in LangChain**  
- `LLMChain` → Basic prompt processing  
- `SequentialChain` → Multiple LLM calls in order  
- `ConversationalChain` → Maintains memory  

---

# **📌 6. Memory: Storing Conversation History**  
Memory allows an LLM to **remember previous conversations**.

## **🛠 Adding Memory to a Chatbot**
```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

memory = ConversationBufferMemory()
llm = OpenAI(openai_api_key="your-api-key")

conversation = ConversationChain(llm=llm, memory=memory)

print(conversation.run("Hello! Who are you?"))
print(conversation.run("Remember that my name is Kunal."))
print(conversation.run("What is my name?"))
```

🔹 **Types of Memory**  
- `ConversationBufferMemory` → Stores recent conversations  
- `ConversationSummaryMemory` → Summarizes past interactions  
- `VectorStoreRetrieverMemory` → Uses embeddings for long-term recall  

---

# **📌 7. Agents: LLMs That Use Tools**  
Agents allow LLMs to **search the web, fetch API data, and interact with tools dynamically**.

## **🛠 Creating an Agent**
```python
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="your-api-key")
tools = load_tools(["serpapi"], serpapi_api_key="your-serp-api-key")

agent = initialize_agent(
    tools=tools, 
    llm=llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

response = agent.run("What is the latest news about AI?")
print(response)
```

🔹 **Agent Types**  
- `ZeroShotAgent` → Uses LLM without pre-set logic  
- `ConversationalAgent` → Maintains chat history  
- `SelfQueryAgent` → Queries databases intelligently  

---

# **📌 8. Retrieval Augmented Generation (RAG) with Vector Stores**  
LLMs can **retrieve relevant documents** using vector stores like FAISS and ChromaDB.

## **🛠 Using FAISS for Vector Search**
```python
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document

docs = [
    Document(page_content="AI is transforming industries."),
    Document(page_content="Machine Learning is a subset of AI."),
]

embeddings = OpenAIEmbeddings(openai_api_key="your-api-key")
vectorstore = FAISS.from_documents(docs, embeddings)

query = "What is AI?"
results = vectorstore.similarity_search(query)
print(results[0].page_content)
```

🔹 **Vector Stores Supported in LangChain**  
- FAISS  
- Pinecone  
- ChromaDB  

---

# **📌 9. Using LangChain with APIs**  
LangChain integrates with multiple APIs for advanced AI functionalities.

## **🛠 Fetching Data from an API**
```python
from langchain.tools import Tool

def fetch_weather(location: str) -> str:
    return f"Weather in {location}: 25°C, sunny."

weather_tool = Tool(
    name="Weather API",
    func=fetch_weather,
    description="Fetches the weather for a given location."
)

print(weather_tool.run("New York"))
```

---

# **📌 10. Building a LangChain Chatbot**  
Combining **memory, chains, and LLMs**, we can create an **AI-powered chatbot**.

```python
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

llm = OpenAI(openai_api_key="your-api-key")
memory = ConversationBufferMemory()

chatbot = ConversationChain(llm=llm, memory=memory)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot.run(user_input)
    print(f"AI: {response}")
```

---

# **🚀 Conclusion**  
LangChain **simplifies AI development** by providing tools for **prompt engineering, chaining, memory, agents, and retrieval**. Whether you're building a chatbot, a research assistant, or an autonomous agent, LangChain helps you get there faster.

Would you like to see a **complete project** built using LangChain? 🎯
