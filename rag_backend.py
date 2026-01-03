from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

load_dotenv()

def build_rag_chain(file_path: str):
    # 1️⃣ Load uploaded file
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    # 2️⃣ Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    # 3️⃣ Embeddings + Vector DB
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 4️⃣ LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    # 5️⃣ Prompt
    prompt = ChatPromptTemplate.from_template("""
Answer the question using ONLY the context below.

Context:
{context}

Question:
{input}
""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    return retrieval_chain


def ask_rag(chain, question: str) -> str:
    response = chain.invoke({"input": question})
    return response["answer"]
