import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Set up Streamlit page
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot with LangChain & Ollama Qwen")

# Load Ollama model
llm = Ollama(model="qwen")

# Set up memory for conversation history
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input field
user_input = st.chat_input("Ask me anything...")
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get AI response
    response = conversation.run(user_input)

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Store AI response
    st.session_state.messages.append({"role": "assistant", "content": response})
