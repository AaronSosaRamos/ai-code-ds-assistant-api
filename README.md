# AI Code and DS Assistant API

**AI Code and DS Assistant API** is a powerful and intelligent system designed to assist with coding and data structure (DS) tasks through a chatbot interface. It also provides an advanced **Software Architecture Assistant**, capable of generating architectural graphs, employing a multimodal approach, and ensuring seamless interoperability between **Google Generative AI** and **GPT-4o-mini**. The API features **CodeXpert**, an AI agent for coding assistance and optimization, enhanced with **Tavily** for conducting Internet searches on AI-related topics.

Developed by **Wilfredo Aaron Sosa Ramos**, this API offers dynamic, context-aware responses in JSON format using a **few-shot learning approach**, making it adaptable to a wide range of software development and data structure scenarios.

## Table of Contents

- [1. Features](#1-features)
- [2. Components](#2-components)
  - [2.1 Chatbot for Coding and DS Assistance](#21-chatbot-for-coding-and-ds-assistance)
  - [2.2 Software Architecture Assistant](#22-software-architecture-assistant)
  - [2.3 CodeXpert](#23-codexpert)
- [3. Technologies Used](#3-technologies-used)
- [4. Environment Variables](#4-environment-variables)
- [5. Installation Guide](#5-installation-guide)
- [6. How to Use](#6-how-to-use)

---

## 1. Features

**AI Code and DS Assistant API** provides a comprehensive suite of tools designed to assist developers and software architects. Its main features include:

- **Chatbot for Coding and Data Structure Assistance**: A conversational interface for developers to ask questions and receive code-related help, covering a wide range of coding problems and data structure tasks.
- **Software Architecture Assistant**: Generates architecture diagrams, offers multimodal data handling, and ensures compatibility between **Google Generative AI** and **GPT-4o-mini** for efficient architectural advice.
- **CodeXpert**: An intelligent agent dedicated to optimizing and improving code quality. It uses **Tavily** for conducting Internet searches when the problem domain relates to AI-specific queries.
- **Few-shot Learning Approach**: The API adapts to specific user contexts with minimal input through few-shot learning, providing better and more contextually accurate JSON responses.
- **Interoperability**: Seamlessly integrates multiple AI models to deliver robust and context-aware assistance.

---

## 2. Components

The **AI Code and DS Assistant API** is divided into three main components, each designed to cater to a specific aspect of software development and data structure management.

### 2.1 Chatbot for Coding and DS Assistance

This component acts as a **chatbot** that provides support for coding tasks and data structure-related problems. It allows developers to:

- Ask questions about specific programming languages, algorithms, or data structures.
- Receive real-time suggestions and code snippets in JSON format.
- Get help with debugging, optimizing, and understanding complex codebases.
  
The chatbot provides detailed, context-sensitive answers based on the input received, leveraging both **Google Generative AI** and **GPT-4o-mini** to ensure accurate results.

### 2.2 Software Architecture Assistant

The **Software Architecture Assistant** is designed to help software engineers and architects visualize, design, and improve software systems. This assistant:

- **Generates architectural diagrams** based on user input and system requirements.
- Uses a **multimodal approach**, meaning it can process both textual and graphical input/output, making it highly versatile for complex architectural needs.
- Ensures **interoperability between Google Generative AI and GPT-4o-mini**, allowing for highly intelligent architectural advice that adapts to changing project requirements.
  
This assistant is especially useful for designing scalable, maintainable software architectures, with support for generating JSON outputs for easy integration into other tools.

### 2.3 CodeXpert

**CodeXpert** is an advanced agent focused on **coding assistance and optimization**. This agent:

- **Analyzes code snippets** for potential optimizations and improvements.
- Offers **best practices** and **coding patterns** tailored to the input provided by the user.
- Utilizes **Tavily** for conducting AI-specific Internet searches, helping developers stay up-to-date with the latest advancements in AI and machine learning.
  
With **CodeXpert**, developers can improve their code quality and find solutions to complex coding problems with minimal effort.

---

## 3. Technologies Used

The **AI Code and DS Assistant API** is built using modern AI and web technologies to ensure high performance, scalability, and accuracy. The core technologies include:

- **Python**: The primary programming language used for building the API.
- **FastAPI**: A high-performance web framework for building APIs with Python, providing fast and efficient request handling.
- **LangChain**: A framework for building applications powered by large language models (LLMs), enabling the seamless integration of various AI models.
- **LangGraph**: A powerful tool for managing and processing complex workflows that involve multiple AI models, ensuring that each model interacts smoothly with the others.
- **Google Generative AI**: A multimodal AI model used to generate both text and images, providing powerful support for tasks like code generation and architecture visualization.
- **GPT-4o-mini**: An optimized version of GPT-4 designed for coding assistance, natural language understanding, and code optimization.
- **Tavily**: An AI-powered tool that enhances Internet search capabilities, especially for queries related to AI and machine learning, ensuring developers can access the latest information.
- **Few-shot Learning**: A machine learning technique employed to generate highly accurate responses based on a small number of input examples, allowing the API to generalize across a variety of tasks.

These technologies together create a robust, scalable, and intelligent system for coding and data structure assistance.

---

## 4. Environment Variables

The **AI Code and DS Assistant API** requires the following environment variables for proper configuration:

- **ENV_TYPE**: Specifies the environment type (e.g., development, production).
- **GOOGLE_API_KEY**: The API key for accessing Google Generative AI services.
- **OPENAI_API_KEY**: The API key for accessing GPT-4o-mini via OpenAI.
- **TAVILY_API_KEY**: The API key for enabling Tavily-based Internet search.
- **PROJECT_ID**: The project ID associated with this AI service.

Example `.env` file configuration:

```env
ENV_TYPE=development
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
PROJECT_ID=your_project_id_here
```

Replace `your_*_api_key_here` and `your_project_id_here` with the appropriate credentials provided for the API.

---

## 5. Installation Guide

To set up and run the **AI Code and DS Assistant API** locally, follow these steps:

1. **Clone the repository**:
   - Download the repository to your local machine using the following command:
     ```
     git clone https://github.com/yourusername/AI-Code-and-DS-Assistant-API.git
     ```

2. **Navigate to the project directory**:
   - Move into the project folder:
     ```
     cd AI-Code-and-DS-Assistant-API
     ```

3. **Install dependencies**:
   - Install the required Python dependencies using pip:
     ```
     pip install -r requirements.txt
     ```

4. **Set up environment variables**:
   - Create a `.env` file in the root directory of the project and configure the environment variables as follows:
     ```
     ENV_TYPE=development
     GOOGLE_API_KEY=your_google_api_key_here
     OPENAI_API_KEY=your_openai_api_key_here
     TAVILY_API_KEY=your_tavily_api_key_here
     PROJECT_ID=your_project_id_here
     ```

5. **Run the FastAPI server**:
   - Start the API server locally:
     ```
     uvicorn main:app --reload
     ```

6. **Access the API**:
   - The API will be running locally at `http://localhost:8000`. You can interact with the API via HTTP requests to the provided endpoints.

---

## 6. How to Use

The **AI Code and DS Assistant API** offers a range of endpoints that users can interact with. Here’s how you can use the system effectively:

1. **Coding Assistance (Chatbot)**:
   - Use the chatbot to ask questions related to code snippets, algorithms, or data structures. The chatbot responds in JSON format with suggested code or detailed explanations.

2. **Software Architecture Assistant**:
   - Submit system requirements or architectural questions to receive architecture diagrams and suggestions. The assistant can handle both textual and graphical inputs.

3. **CodeXpert for Optimization**:
   - Provide code snippets to **CodeXpert** for analysis. It will suggest optimizations and best practices, leveraging **Tavily** for AI-related searches when necessary.

4. **Few-shot Learning Responses**:
   - For more context-aware assistance, the API uses few-shot learning to provide tailored responses based on minimal input. Simply provide a small number of examples, and the API will generalize to solve similar tasks.

By leveraging these components, users can enhance their software development workflows, improve code quality, and design scalable architectures with minimal effort.
