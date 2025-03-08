import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Initialize Hugging Face Embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Function to load and process resumes
def load_and_embed_resume(pdf):
    loader = PyPDFLoader(pdf)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)
    return chunks

# Streamlit UI
st.title("AI-Powered Resume Filter ")

# Upload job description
job_description = st.text_area("Enter the Job Description:")

# Upload resumes
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type="pdf", accept_multiple_files=True)

if job_description and uploaded_files:
    st.write("Processing Resumes...")

    # Embed the job description using Hugging Face
    job_embedding = embeddings.embed_query(job_description)

    # Process resumes
    resume_chunks = []
    for uploaded_file in uploaded_files:
        temp_file = f"./{uploaded_file.name}"
        with open(temp_file, "wb") as file:
            file.write(uploaded_file.getvalue())

        chunks = load_and_embed_resume(temp_file)
        resume_chunks.extend(chunks)

    # Create FAISS vector store
    vector_db = FAISS.from_documents(resume_chunks, embeddings)
    retriever = vector_db.as_retriever()

    # Rank resumes based on similarity
    similar_resumes = retriever.get_relevant_documents(job_description)


    st.subheader("Top Matching Resumes:")
    for idx, doc in enumerate(similar_resumes):
        st.write(f"**Rank {idx+1}:** {doc.metadata.get('source', 'Unknown Resume')}")
        st.write(doc.page_content[:500] + "...")  # Show snippet of the resume

    # User query
    question = st.text_input("Ask about the resumes:")
    if question:
        st.warning("Answering questions feature currently requires a working LLM. Consider adding an open-source LLM or external API.")
