# 🧠 LangGraph Workflow Agent – Gemini Edition

A powerful, extensible AI workflow agent built using [LangGraph](https://github.com/langchain-ai/langgraph) that leverages:

- **Google Gemini** models via **Vertex AI**
- **LangGraph Studio** for debugging, visualization & time travel
- **Tavily** for real-time web search
- **Workflow creation, review, and saving**
- **Human-in-the-loop (HITL) editing**
- **Extensible tool interface with memory**

![LangGraph Studio View](./static/studio_ui_output.JPG)

---

## 🚀 What It Does

This agent functions as a **workflow orchestrator**. It takes a user query and:

1. Uses the LLM to **generate a task-specific workflow**
2. Optionally allows the user to **review/edit** the generated steps
3. Utilizes tools like **Tavily Search** for real-time queries
4. Saves the workflow to a file using a custom **Save Workflow** tool
5. Stores interactions in memory for contextual reasoning

---

## 🛠️ Tech Stack

| Component         | Description                                           |
|------------------|-------------------------------------------------------|
| **LLM Backend**   | Google Gemini (`gemini-2.0-flash`) via Vertex AI     |
| **Tooling**       | Tavily Search, Save-to-File Workflow Tool            |
| **LangGraph IDE** | Full support for LangGraph Studio                    |
| **HITL**          | CLI-based review before finalizing output            |
| **Memory**        | In-memory state storage                              |

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
  git clone <your-repo-url>
  cd react-agent
```
## 2. Set Up Environment Variables

Update the .env file with your credentials and update all credits.

You Can Use a different model other than gemini , just add its api and chnage the model and provider name in configuration.py

## 3. Install Python Dependencies

```bash
uv pip install -e .
```
Run this in your virtual environment , If you use another LLm not gemini then install specific package for using its api also.

# Running the Agent

LangGraph Studio Mode
For visualization and debugging: 
```bash
langgraph dev
```

##  Features

| Feature                | File / Description                              |
|------------------------|-------------------------------------------------|
| **Prompt Design**      | `prompts.py` – Editable system instructions     |
| **Model Loader**       | `google_model.py` – Connects to Gemini          |
| **Workflow Agent**     | `graph.py` – Agent loop with logic              |
| **Tavily Search Tool** | `tools.py` – Web search integration             |
| **Save Workflow Tool** | `tools.py` – Writes agent workflow to disk      |
| **Human Review**       | HITL step in agent routing logic                |
| **Memory System**      | `memory.py` – Simple in-memory message store    |

---


## File Structure
```
src/react_agent/
│
├── graph.py              # Main workflow agent logic
├── tools.py              # Tavily + Save Workflow tools
├── prompts.py            # Prompt templates
├── state.py              # Agent input/output schema
├── configuration.py      # LangGraph configuration
└── utils.py              # Helper functions
```
