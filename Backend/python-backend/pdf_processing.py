import os
import pdfplumber
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from config import Config

def extract_and_create_context(folder_path):
    loader = DirectoryLoader(path= folder_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                          chunk_overlap=50)
    texts = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}) 
    db = FAISS.from_documents(texts, embeddings)
    db.save_local("faiss")

    return db


def create_chain(vectorStore):
  model = ChatOpenAI(
      model= 'gpt-3.5-turbo',
      temperature=0.4,
      openai_api_key=Config.SECRET_KEY
  )

  prompt = ChatPromptTemplate.from_messages([
  ("system",Config.PROMPT),
  MessagesPlaceholder(variable_name="chat_history"),
  ("human","{input}")])

  chain = create_stuff_documents_chain(
      llm=model,
      prompt=prompt
  )
  retriever = vectorStore.as_retriever(search_kwargs={"k": 3})

  retrieval_chain = create_retrieval_chain(
      retriever,
      chain)
  return retrieval_chain