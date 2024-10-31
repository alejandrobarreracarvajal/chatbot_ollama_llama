# Chatbot para Procesamiento de Archivos y Análisis sin Conexión a Internet

Este proyecto es un chatbot que utiliza modelos de Llama para procesar y responder a mensajes de texto sin la necesidad de una conexión a Internet.

## Descripción del Proyecto

Este proyecto utiliza los modelos Llama3.2 (1B/3B) y Llama 3.1 (8B) para procesar y responder a mensajes de texto sin la necesidad de una conexión a Internet. El chatbot es capaz de procesar archivos de diferentes formatos, incluyendo CSV, PDF, JSON, imágenes (JPG/PNG), documentos de Word (.docx), archivos de texto (.txt), y código Python (.py) o cuadernos de Jupyter (.ipynb).

## Características clave

- **Interacción suave:** desarrollado en Gradio, proporciona una experiencia de usuario intuitiva.
- **Versatilidad de archivos:** capaz de procesar múltiples formatos de archivos.
- **Seguridad primero:** funciona localmente, garantizando la privacidad de los datos.
- **Accesible para todos:** los modelos Llama3.2 (1B/3B) están optimizados para CPU, lo que permite su uso sin requerir una GPU, aumentando la accesibilidad para usuarios con hardware limitado.

## Importancia de la Inteligencia Artificial Abierta

La inteligencia artificial abierta ha revolucionado la forma en que procesamos datos y interactuamos digitalmente. Los modelos como Llama3.2 (1B/3B) y Llama 3.1 (8B) son un testimonio de los avances significativos realizados por la comunidad, ofreciendo soluciones poderosas y accesibles para todos.

## Beneficios para Comunidades con Recursos Limitados

Este proyecto tiene como objetivo democratizar el acceso a la inteligencia artificial, permitiendo que más personas, incluyendo aquellas en comunidades rurales o con recursos limitados, puedan beneficiarse de las ventajas de la inteligencia artificial sin necesidad de una conexión a Internet o hardware potente.

## Configuración del Modelo

El modelo utilizado en este proyecto es el Llama3.2 (1B/3B) o Llama 3.1 (8B), dependiendo de la configuración seleccionada. La configuración del modelo se puede cambiar en el archivo `main.py`.

## Requisitos previos

- **Python**: 3.12.2
- **Sistema**: macOS, Windows o Linux
- **Ollama**: instalado y configurado

## Instalación

1. Clona el repositorio y navega al directorio del proyecto:

    ```bash
    git clone https://github.com/your-username/chatbot_ollama_llama.git
    cd chatbot_ollama_llama
    ```

2. Crea y activa un entorno de conda:

    ```bash
    conda create --name chatbot_env python=3.12.2
    conda activate chatbot_env
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar el chatbot, ejecuta el siguiente comando:

```bash
python main.py
