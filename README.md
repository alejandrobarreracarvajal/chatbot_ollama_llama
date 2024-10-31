# Chatbot for File Processing and Analysis Without Internet Connection Based on CPU or GPU Architecture and Different Llama Models

🌍 **Democratizing Access to Open Source Artificial Intelligence**  
Open-source artificial intelligence has transformed the way we process data and interact in the digital environment. Models like Llama3.2 (1B/3B) and Llama 3.1 (8B) represent significant advancements made by the community, offering powerful and accessible solutions for everyone.

👥 **Project Description**  
This project presents a chatbot that utilizes Llama3.2 (1B/3B) and Llama 3.1 (8B) models to process and respond to text messages without the need for an Internet connection. The chatbot is capable of handling a variety of file formats, including CSV, PDF, JSON, images (JPG/PNG), Word documents (.docx), text files (.txt), and Python (.py) or Jupyter Notebook (.ipynb) code.

✨ **Key Features:**
- **Smooth Interaction:** Developed in Gradio, it provides an intuitive and fluid user experience.
- **File Versatility:** Capable of processing multiple formats, ensuring flexibility in data handling.
- **Security First:** Operates locally, ensuring user data privacy.
- **Accessible for Everyone:** Llama3.2 (1B/3B) models are optimized for CPU, allowing use without the need for a GPU, increasing accessibility for users with limited hardware.

## Benefits for Communities with Limited Resources

This project aims to democratize access to artificial intelligence, enabling more people, including those in rural communities or with limited resources, to benefit from the advantages of artificial intelligence without the need for an Internet connection or powerful hardware.

## Model Configuration

The model used in this project is Llama3.2 (1B/3B) or Llama 3.1 (8B), depending on the selected configuration. The model configuration can be changed in the `main.py` file.

## Prerequisites

- **Python:** 3.12.2
- **System:** macOS, Windows, or Linux
- **Ollama:** installed and configured

## Installation

1. Clone the repository and navigate to the project directory:

    ```bash
    git clone https://github.com/alejandrobarreracarvajal/chatbot_ollama_llama.git
    cd chatbot_ollama_llama
    ```

2. Create and activate a conda environment:

    ```bash
    conda create --name chatbot_env python=3.12.2
    conda activate chatbot_env
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set Up the Ollama Server:
   Make sure you have [Ollama](https://ollama.com/) installed and configured.

## Download the Models

### Available Models:
- **Llama3.2 1B:** `llama3.2:1b` (recommended for systems with limited resources)
- **Llama3.2 3B:** `llama3.2`
- **Llama3.1 8B:** `llama3.1` (advanced model, requires high memory and processing)

---

## Usage

### Using the Ollama
If your goal is to run Llama 3 as a chatbot, you can start it directly from the terminal with the following command:

```bash
ollama run llama3
```
### Using the Chatbot
To start the chatbot, run the following command:

```bash
python main.py
```
