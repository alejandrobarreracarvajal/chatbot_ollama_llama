# Standard Python libraries
import json
import os
import time
import webbrowser  

# Third-party libraries
import gradio as gr            # Framework for creating user interfaces in web applications
import numpy as np             # Matrix manipulation and advanced mathematical functions
import pandas as pd            # Analysis and manipulation of structured data
from PIL import Image          # Handling images in different formats
from docx import Document      # Processing .docx files from Microsoft Word
import easyocr                 # OCR for recognizing text in images and PDFs

# LangChain and other models libraries
from langchain.schema import AIMessage, HumanMessage  # Handling messages in the conversation flow
from langchain_ollama import ChatOllama               # LangChain client for Ollama models
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Text splitter to manage text lengths

# Library for interacting with PDFs and optimizing their processing
import pymupdf4llm  

# Llama model configuration
# For GPU configuration (uncomment the corresponding line):
# ollama_model = ChatOllama(model="llama3.1", server="http://localhost:11434")

# Current configuration for CPU
ollama_model = ChatOllama(model="llama3.2:1b", num_gpu=0, server="http://localhost:11434")

"""
Llama Model Configuration in Ollama

- This code initializes the Llama model using Ollama, enabling local interactions.
- Different versions of Llama are available, each with varying hardware requirements and capabilities.

Available Models:
    - Llama3.2 1B : llama3.2:1b  (recommended for systems with limited resources)
    - Llama3.2 3B : llama3.2
    - Llama3.1 8B : llama3.1  (advanced model, requires high memory and processing)

GPU and CPU Usage:
    - For GPU configuration: uncomment the line with `model="llama3.1"` and omit the `num_gpu` parameter
    - For CPU configuration: `model="llama3.2:1b"`, with `num_gpu=0`
"""

# Initialize EasyOCR reader
"""
Set gpu=True to enable GPU acceleration for faster processing (requires a compatible GPU, e.g., NVIDIA with CUDA).
Set gpu=False to force CPU usage, which is slower but can be used on systems without GPU support.
"""
reader = easyocr.Reader(['en'], gpu=False)

def process_file(file):
    """
    Process a file and extract text based on its type.
    Supports CSV, PDF, JSON, image files (JPG/PNG), DOCX, TXT, PY, and IPYNB.

    Parameters:
    file (str): Path to the file to process.

    Returns:
    str: Extracted text from the file.
    """
    try:
        if file.endswith('.csv'):
            # Read the CSV file in chunks
            chunks = pd.read_csv(file, chunksize=10000) 
            text = pd.concat(chunks).to_string()
        
        elif file.endswith('.pdf'):
            # Read the PDF file using PyMuPDF4LLM
            md_text = pymupdf4llm.to_markdown(file)  # Extract as Markdown
            text = md_text
        
        elif file.endswith('.json'):
            with open(file, 'r') as f:
                text = json.load(f)
                text = str(text)
        
        elif file.endswith('.jpg') or file.endswith('.png'):
            img = Image.open(file)
            img_np = np.array(img)  # Convert image to numpy array
            result = reader.readtext(img_np)  # Extract text from the image
            text = ' '.join([res[1] for res in result])  # Concatenate extracted text
        
        elif file.endswith('.docx'):
            doc = Document(file)
            text = '\n'.join([para.text for para in doc.paragraphs])  # Read text from DOCX
        
        elif file.endswith('.txt'):
            with open(file, 'r') as f:
                text = f.read()
        
        elif file.endswith('.py'):
            with open(file, 'r') as f:
                text = f.read()
        
        elif file.endswith('.ipynb'):
            with open(file, 'r') as f:
                content = json.load(f)
                text = ""
                for cell in content['cells']:
                    if cell['cell_type'] == 'code':
                        text += ''.join(cell['source']) + '\n'
        
        else:
            raise ValueError("Unsupported file type")
        
        if not text:
            raise ValueError("The file is empty.")
        
    except Exception as e:
        text = f"Error processing the file: {str(e)}"
    
    return text

def process_message(message, file=None, history=""):
    """
    Process the user's message and generate a chatbot response.

    Parameters:
    message (str): User's message.
    file (str): Optional path to a file for processing.
    history (str): Conversation history.

    Returns:
    tuple: Formatted response, updated history, empty message.
    """
    if file:
        file_text = process_file(file)
        if len(file_text) > 16000:  
            splitter = RecursiveCharacterTextSplitter(chunk_size=16000, chunk_overlap=0)
            file_text = splitter.split_text(file_text)[0]  
        processed_message = message + "\n" + file_text
    else:
        processed_message = message

    # Add a prompt to guide the model
    prompt = f"""
    ### Document Processing and Question

    **Provided Document/Text:**
    {processed_message}

    **User's Question:**
    {message.split('\n')[-1]}?

    **Expected Response:**
    Please provide a detailed and accurate response considering the document content and the user's question.
    """
    # Send the message to the model in the appropriate format
    human_message = HumanMessage(content=prompt)
    response = ollama_model([human_message], temperature=0.2, max_tokens=512)

    # Format the response with clearer structure and format
    formatted_response = (
        "### Chatbot's Response\n"
        f"**{response.content}**\n"
        "---\n"
    )

    # Progressive output for the output_text component
    output_text_progressive = ""
    for char in formatted_response:
        output_text_progressive += char
        yield output_text_progressive, history, ""  # Progressively in output_text, history only at the end
        time.sleep(0.005)  # Control response speed

    # Update history only after the complete response
    history += f"**User:** {message}\n\n**Chatbot:** {formatted_response}\n"
    
    yield output_text_progressive, history, ""  # Complete response and history at the end


# Determine the model name to display in the header according to the model configured in ollama_model
if ollama_model.model == "llama3.2:1b":
    model_name = "Llama3.2 1B"
elif ollama_model.model == "llama3.2":
    model_name = "Llama3.2 3B"
elif ollama_model.model == "llama3.1":
    model_name = "Llama3.1 8B"
else:
    model_name = "Unknown model"

# Create the user interface with Gradio
with gr.Blocks() as demo:
    # Use model_name in the title
    gr.Markdown(f"<h1 style='color: white; text-align: center;'>Chatbot with {model_name}</h1>")
    
    output_text = gr.Textbox(label="Chatbot's Response", visible=True, interactive=False, lines=20)
    file_input = gr.File(label="File (optional)")
    message_input = gr.Textbox(label="Message", lines=3, placeholder="Write your message here...")
    send_button = gr.Button("Send")
    history_text = gr.Textbox(label="History", visible=True, interactive=False, lines=10)

    def delete_file(file, *args):
        return None

    send_button.click(
        fn=process_message, 
        inputs=[message_input, file_input, history_text], 
        outputs=[output_text, history_text, message_input]
    )
    message_input.submit(
        fn=process_message, 
        inputs=[message_input, file_input, history_text], 
        outputs=[output_text, history_text, message_input]
    )

    send_button.click(
        fn=delete_file, 
        inputs=[file_input], 
        outputs=[file_input]
    )

if __name__ == "__main__":
    demo.launch(inbrowser=True)