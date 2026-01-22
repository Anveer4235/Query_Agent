


<div align="center">

# 🧠 AgentsQueries Crew

**A multi-agent Retrieval-Augmented Generation (RAG) system built with CrewAI, LangChain, and a custom retrieval tool to answer company policy questions accurately.**

</div>

---

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white">
  <img alt="CrewAI" src="https://img.shields.io/badge/CrewAI-Multi--Agent-blueviolet">
  <img alt="RAG" src="https://img.shields.io/badge/RAG-Enabled-success">
  <img alt="LangChain" src="https://img.shields.io/badge/LangChain-Framework-blue">
  <img alt="ChromaDB" src="https://img.shields.io/badge/VectorDB-Chroma-orange">
  <img alt="Status" src="https://img.shields.io/badge/Status-Working-success">
</p>

---

<details open>
<summary><b>📕 Table of Contents</b></summary>

- 💡 [What is AgentsQueries?](#-what-is-agentsqueries)
- 🌟 [Key Features](#-key-features)
- 🤖 [Agents Overview](#-agents-overview)
- 🛠️ [Custom Tool](#-custom-tool)
- 🔎 [System Architecture](#-system-architecture)
- 🎬 [Getting Started](#-getting-started)
- ▶️ [Running the Project](#-running-the-project)
- 📁 [Project Structure](#-project-structure)
- 🔧 [Customization & Extensions](#-customization--extensions)
- 📚 [Learning Outcomes](#-learning-outcomes)

</details>

---

## 💡 What is AgentsQueries?

**AgentsQueries** is a **CrewAI-powered multi-agent RAG system** designed to answer employee questions using **internal company policy documents stored as PDFs**.

Instead of relying on pure language-model generation, the system:
- Retrieves **relevant policy text**
- Analyzes it using specialized agents
- Generates **clear, grounded, and reliable answers**

This approach **significantly reduces hallucinations** and ensures answers are based on official company policies.

---

## 🌟 Key Features

### 🔍 Retrieval-Augmented Generation (RAG)
- Semantic search over policy PDFs
- Answers grounded in real documents

### 🤖 Multi-Agent Collaboration
- Each agent has a focused responsibility
- Agents work sequentially to complete the task

### 🛠️ Custom CrewAI Tool
- `PolicyRetrieverTool` performs vector similarity search
- Cleanly integrated into the agent workflow

### 📄 PDF-Based Knowledge Source
- Company policies stored as PDFs
- Chunked, embedded, and persisted for reuse

### ⚡ Persistent Vector Database
- One-time ingestion
- Fast retrieval across multiple runs

---

## 🤖 Agents Overview

### 1️⃣ Query Understanding Agent *(Reserved for future use)*
- Intended for query normalization and intent detection
- Kept for future extensibility

### 2️⃣ Document Retrieval Agent
- Uses `PolicyRetrieverTool`
- Retrieves relevant policy sections using semantic similarity

### 3️⃣ Policy Analyst Agent
- Interprets retrieved policy text
- Extracts rules, conditions, and intent

### 4️⃣ Answer Generator Agent
- Converts analysis into clear, user-friendly answers
- Produces the final response

---

## 🛠️ Custom Tool

### 🔧 PolicyRetrieverTool

**Purpose:**  
Retrieve relevant company policy text using semantic similarity search.

**How it works:**
1. Converts the user query into embeddings  
2. Searches the Chroma vector database  
3. Returns the most relevant policy excerpts  

The tool is implemented as a **custom CrewAI `BaseTool`** and injected directly into the retrieval agent.

---

## 🔎 System Architecture

```text
User Query
   ↓
Document Retrieval Agent
   ↓ (PolicyRetrieverTool + Chroma Vector DB)
Policy Analyst Agent
   ↓
Answer Generator Agent
   ↓
Final Policy-Grounded Answer
````

---

## 🎬 Getting Started

### 📝 Prerequisites

* Python **>= 3.10 and < 3.14**
* OpenAI API key
* **UV** for dependency management

---

### 📦 Installation

```bash
pip install uv
crewai install
```

---

### 🔑 Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

### 📄 Ingest Policy Documents

Before running the agents, ingest the company policy PDF:

```bash
python ingest_policies.py
```

This step:

* Loads the PDF
* Splits text into chunks
* Generates embeddings
* Persists them in ChromaDB

> This step is required only once (or whenever documents change).

---

## ▶️ Running the Project

To start the AgentsQueries Crew:

```bash
crewai run
```

or

```bash
uv run run_crew
```

---

## 📁 Project Structure

```text
agents_queries/
│
├── src/agents_queries/
│   ├── crew.py                 # Crew and agent definitions
│   ├── main.py                 # Entry point
│   ├── tools/
│   │   ├── custom_tool.py      # PolicyRetrieverTool
│   │   └── __init__.py
│   ├── config/
│   │   ├── agents.yaml         # Agent configurations
│   │   └── tasks.yaml          # Task definitions
│
├── ingest_policies.py          # PDF ingestion & vector creation
├── knowledge/vectorstore/      # Persistent Chroma storage
├── .env
└── README.md
```

---

## 🔧 Customization & Extensions

You can extend this project by:

* Activating the Query Understanding Agent
* Adding citations and page numbers to answers
* Supporting multiple policy documents
* Adding memory and follow-up questions
* Building a UI (Streamlit / FastAPI / Web app)

---

## 📚 Learning Outcomes

This project demonstrates:

* How to build a RAG system using PDFs
* How to design multi-agent workflows with CrewAI
* How to create and integrate custom tools
* How vector databases help reduce hallucinations

---



