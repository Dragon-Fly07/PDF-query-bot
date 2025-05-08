from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

"""
get_data: Generates the vector database using Meta's FAISS vector store. Uses 1000 characters per document with 100 of them overlapping with the previous document
    - document: path of the pdf file
"""

def get_data(document: str) -> FAISS | None:
    if not document:
        return 

    docs = PDFPlumberLoader(document).load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = splitter.split_documents(docs)

    db = FAISS.from_documents(docs, embedding=embeddings)
    return db


"""
query_agent: Takes the databases, performs a search based on query and then passes it into a LLM. Generates an answer based on the results
    - query: Question to be asked
    - marks: number of points required for the answer
    - db: vector store
"""

def query_agent(query: str, marks: int, db:FAISS) -> str | None:
    if db is None:
        return 

    marker = {
        2 : 5,
        4 : 7,
        6 : 9,
        8 : 13,
        12: 15
    }
    k = marker[marks]
    pages = db.similarity_search(query, k)
    data = " ".join([d.page_content for d in pages])

    llm = GoogleGenerativeAI(model="gemini-2.0-flash")
    prompt = PromptTemplate(input_variables=["query", data], template="You are an expert in the field of ancirent Tamil technology. You are given the documents {data} on certain topics pertaining to your field. You job is to be helpful and take in questions and answer them to the highest accuracy possible. If you feel you do not know the answer to a question, say \"I don't know\". With those documents as context, answer {query}.")
    chain = prompt | llm
    response = chain.invoke(input = {"query" : query, "data" : data})
    return response

