# AI-Powered Resume Filter

This project is designed to help recruiters and hiring managers filter resumes efficiently using AI-powered embeddings and semantic search. Leveraging OpenAI's GPT and Hugging Face embeddings, this tool identifies resumes that best match a given job description.

## Features
✅ Upload multiple resumes in PDF format  
✅ Uses **Hugging Face Embeddings** for semantic search  
✅ Ranks resumes based on similarity with the job description  
✅ Provides an interactive Q&A feature to query the resumes  

---

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/AI-Resume-Filter.git
cd AI-Resume-Filter
```

2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Up Environment Variables**
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your-openai-api-key-here
```

---

## Usage

1. **Run the Application**
```bash
streamlit run app.py
```

2. **Upload Resumes and Enter Job Description**
- Provide a job description in the text area.  
- Upload multiple resume PDFs.  
- The system will rank the resumes based on relevance.  

3. **Query Resumes**
- Enter specific questions about the resumes to retrieve targeted insights.  

---

## Example Inputs
### **Job Description Example:**
```
We are looking for a Software Engineer with expertise in Python, Django, and React. The ideal candidate should have experience in building scalable web applications.
```

### **Sample Resumes for Testing:**
- `Software_Engineer_JohnDoe.pdf`
- `Data_Scientist_JaneSmith.pdf`
- `Digital_Marketing_MarkJohnson.pdf`
- `Project_Manager_SarahConnor.pdf`

---

## Requirements
- Python 3.10+
- `streamlit`
- `langchain`
- `openai`
- `faiss-cpu`
- `sentence-transformers`
- `pypdf`

Install requirements with:
```bash
pip install streamlit langchain openai faiss-cpu sentence-transformers pypdf
```

---

## Project Structure
```
├── app.py
├── requirements.txt
├── README.md
├── .env
└── sample_resumes/
    ├── Software_Engineer_JohnDoe.pdf
    ├── Data_Scientist_JaneSmith.pdf
    ├── Digital_Marketing_MarkJohnson.pdf
    └── Project_Manager_SarahConnor.pdf
```

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
Feel free to contribute! Fork the repository, create a feature branch, and submit a pull request.

---

## Contact
For questions or support, reach out to [your.email@example.com](mailto:your.email@example.com).

# AI-Resume-Filter












