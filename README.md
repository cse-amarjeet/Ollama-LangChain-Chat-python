# Ollama-LangChain-Chat-python

This repository demonstrates how to integrate the open-source OLLAMA Large Language Model (LLM) with Python and LangChain. It includes various examples, such as simple chat functionality, live token streaming, context-preserving conversations, and API usage.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
  - [Using Virtualenv](#using-virtualenv)
  - [Using Conda](#using-conda)
- [Download and Setup OLLAMA](#download-and-setup-ollama)
- [Usage](#usage)
  - [Chat with OLLAMA using Python](#chat-with-ollama-using-python)
  - [Chat with OLLAMA using LangChain](#chat-with-ollama-using-langchain)
  - [Using OLLAMA API](#using-ollama-api)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project showcases how to utilize the OLLAMA LLM with Python for various chat-based applications. It also includes integration with LangChain for enhanced capabilities such as prompt templates and creating chains.

## Installation

### Prerequisites
- Python 3.10 or higher
- Git
- OLLAMA CLI

### Using Virtualenv

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cse-amarjeet/Ollama-LangChain-Chat-python.git
   cd Ollama-LangChain-Chat-python
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Using Conda

2. **Create and activate a Conda environment:**
   ```bash
   conda create --name ollama-env python=3.10
   conda activate ollama-env
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Download and Setup OLLAMA

1. **Install OLLAMA:**
   Follow the official installation guide for the OLLAMA CLI.

2. **Download the `gemma2:2b` model:**
   Open your terminal and run:
   ```bash
   ollama pull gemma2:2b
   ```
   This will download the `gemma2:2b` model for use in the examples.

3. **Run the model in the terminal:**
   You can test the `gemma2:2b` model by running it directly in the terminal:
   ```bash
   ollama run gemma2:2b
   ```

4. **Verify the installation:**
   Ensure the model is downloaded correctly by running:
   ```bash
   ollama list
   ```
   You should see `gemma2:2b` in the list of available models.

## Usage

### Chat with OLLAMA using Python

1. **Simple Chat Example:**
   Run the basic chat example to interact with OLLAMA.
   ```bash
   python 1_section_ollma/simple_chat.py
   ```

2. **Chat with Live Token Streaming:**
   This example shows how to stream tokens in real-time during the chat.
   ```bash
   python 1_section_ollma/streaming_chat.py
   ```

3. **Context-Preserving Chat Example:**
   Maintain conversation context across multiple interactions.
   ```bash
   python 1_section_ollma/context_chat.py
   ```

4. **Context-Preserving Chat with Streaming:**
   Combine context preservation with live token streaming.
   ```bash
   python 1_section_ollma/context_streaming_chat.py
   ```

### Chat with OLLAMA using LangChain

1. **Basic LangChain Integration:**
   Run the script to use OLLAMA with LangChain for a simple chat interface.
   ```bash
   python 2_section_langchain/langchain_basic.py
   ```

2. **Streaming Tokens with LangChain:**
   Stream tokens in real-time using LangChain.
   ```bash
   python 2_section_langchain/langchain_streaming.py
   ```

3. **Chat History with OLLAMA in LangChain:**
   Keep track of chat history while interacting with OLLAMA.
   ```bash
   python 2_section_langchain/langchain_chat_history.py
   ```

4. **Using Prompt Templates in LangChain:**
   Demonstrates how to create and use prompt templates in LangChain and use ollama models.
   ```bash
   python 2_section_langchain/langchain_prompt_template.py
   ```

5. **Creating Chains with LangChain and OLLAMA:**
   Explore chain creation using LangChain and OLLAMA.
   ```bash
   python 2_section_langchain/langchain_chain.py
   ```

### Using OLLAMA API

1. **Overview of OLLAMA API:**
   Explore the OLLAMA API features with this script.
   ```bash
   python 3_section_apis/ollama_api.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
