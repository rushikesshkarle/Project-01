import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter


from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import create_retrieval_chain


from langchain_classic.chains.combine_documents import create_stuff_documents_chain

load_dotenv()

# Loading data here
loader = TextLoader("data.txt", encoding="utf-8")
documents = loader.load()

# Splitting data into Small chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Convert the text >>>> Embeddings 
embeddings = OpenAIEmbeddings()

# Store embedding data
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# give to LLM ...define LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

# Template for prompt to give to LLM
prompt = ChatPromptTemplate.from_template(
    """
Answer the question using ONLY the context below.

Context:
{context}

Question:
{input}
"""
)

# Chain are defined 
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Front part for user interaction 
print("\n🔹 LangChain RAG Chatbot (type 'exit' to quit)\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    response = retrieval_chain.invoke({"input": query})
    print("\nBot:", response["answer"])
