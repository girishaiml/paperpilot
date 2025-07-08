PaperPilot: Your PDF-Powered AI Assistant
PaperPilot is a lightweight, AI-powered tool that allows users to extract meaningful answers from PDF documents. By uploading a PDF and asking a question, users can receive context-aware responses based on the document’s content using OpenAI’s GPT-4 API.

Features
Upload and parse any PDF file (academic papers, technical docs, manuals, etc.)

Ask natural language questions about the uploaded content

Get quick and accurate answers powered by GPT-4

Simple frontend built with HTML and JavaScript

Python Flask backend for file handling and API communication

Clean, privacy-focused design with no PDF data stored

Sample Output
Question: What is the product name?


Question: What is this PDF about?


Tech Stack
Frontend: HTML, CSS, JavaScript (Vanilla)

Backend: Python Flask

AI Integration: OpenAI GPT-4 API

PDF Processing: PyMuPDF (fitz)

Deployment: Render, EC2, or any standard Python-compatible server

Getting Started
Clone the repository

bash
Copy
Edit
git clone https://github.com/girishaiml/paperpilot.git
cd paperpilot
Install Python dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add your OpenAI key

Create a .env file inside the backend/ directory and add the following line:

ini
Copy
Edit
OPENAI_API_KEY=your-openai-key
Run the Flask app

bash
Copy
Edit
python backend/app.py
Open the frontend

Open the frontend/index.html file in your browser manually (double click or use Live Server in VS Code).

Deployment Notes
Ensure .env is excluded from version control

You can deploy the app using:

Render (recommended for Flask)

AWS EC2 (manual setup)

Docker (optional if you want containerized deployment)

Repository Guidelines
No API keys should be committed

Keep the code modular for future LLM integrations

Screenshots should be stored under /screenshots for documentation

<img width="1440" alt="Screenshot 2025-07-08 at 3 30 57 PM" src="https://github.com/user-attachments/assets/0d06983f-800c-416b-8e5a-f3c9404d22eb" />
<img width="1440" alt="Screenshot 2025-07-08 at 3 30 39 PM" src="https://github.com/user-attachments/assets/5c555c74-9da8-4c18-acb0-2a836404207d" />
