# Chatbots Repository

This repository contains multiple chatbot projects developed using Gemini Pro. Each chatbot is organized into its own folder, designed to cater to different use cases and applications. The repository serves as a collection of AI-powered conversational agents, demonstrating various capabilities and integrations.

## InvoiceExtractor:

Start
 │
 ▼
Load environment variables (.env) 
 │
 ▼
Configure Google Gemini API  
 │
 ▼
Initialize Streamlit App  
 │
 ▼
User inputs prompt (Text)  
 │
 ▼
User uploads an image (Invoice)  
 │
 ├── Yes → Display uploaded image  
 │ └── No  → Wait for image upload  
 │
 ▼
User clicks 'Extract Invoice Information' button  
 │
 ▼
Extract image details (Convert to bytes, get MIME type)  
 │
 ▼
Pass the input prompt, image data, and user input to Gemini model  
 │
 ▼
Receive response from Gemini API  
 │
 ▼
Display extracted invoice information  
 │
 ▼
End  


## PDF_QA_Chatbot:

Start
 │
 ▼
Load environment variables (.env)  
 │
 ▼
Configure Google Gemini API  
 │
 ▼
Initialize Streamlit App  
 │
 ▼
User uploads PDF(s)  
 │
 ├── Yes → Extract text from PDF(s)  
 │ └── No  → Wait for file upload  
 │
 ▼
Split extracted text into chunks  
 │
 ▼
Convert text chunks into vector embeddings using FAISS  
 │
 ▼
Save vector store locally ("faiss_index")  
 │
 ▼
User inputs a question  
 │
 ▼
Load FAISS index and retrieve similar documents  
 │
 ▼
Pass retrieved documents and question to Gemini model  
 │
 ▼
Receive and display AI-generated response  
 │
 ▼
End  

