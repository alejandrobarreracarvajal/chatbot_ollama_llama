# Chatbot with Ollama and Llama

This project is a chatbot that uses the Llama model, based on the Ollama setup, to analyze and process files of different formats and answer questions based on the content.

## Requirements

- **Python**: 3.12.2
- **System**: Works on macOS, Windows, and Linux.
  
## Installation

1. **Clone the repository and navigate to the project directory:**

    ```bash
    git clone https://github.com/your-username/chatbot_ollama_llama.git
    cd chatbot_ollama_llama
    ```

2. **Create and activate a conda environment:**

    ```bash
    conda create --name chatbot_env python=3.12.2
    conda activate chatbot_env
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Ollama server:**
   - Make sure you have [Ollama](https://ollama.com/) installed and configured.
   - Adjust the server address in the code to `http://localhost:11434` or as appropriate for your setup.
   - If using a GPU, set `num_gpu` in the model initialization line.

## Usage

To start the chatbot, run the following command:

```bash
python chatbot.py
