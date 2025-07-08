from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF

# Load .env variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client using our secret key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.route('/ask', methods=['POST'])
def handle_question():
    uploaded_pdf = request.files.get('pdf')
    question = request.form.get('question')

    if not uploaded_pdf or not question:
        return jsonify({'error': 'Missing file or question'}), 400

    try:
        # We read PDF content here
        pdf_data = uploaded_pdf.read()
        doc = fitz.open(stream=pdf_data, filetype="pdf")

        full_text = ""
        for page in doc:
            full_text += page.get_text()

        # We prepare the prompt and send it to OpenAI
        prompt = f"The following is the content of a PDF:\n\n{full_text}\n\nNow answer this question based on it:\n{question}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You answer questions based on PDF content provided by the user."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content
        return jsonify({'answer': answer})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(port=5000, debug=True)
