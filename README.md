# BenIV-Agent

A research prototype for AgentX @Berkeley 2025.

![AgentX](https://img.shields.io/badge/AgentX-Berkeley%20RDI-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Enabled-success)
![License](https://img.shields.io/github/license/ben-rahman/BenIV-Agent)
![MadeWith](https://img.shields.io/badge/Made%20with-Streamlit-red)

> A research prototype for AgentX @Berkeley 2025, focusing on agentic memory and instrumental variable reasoning for safe and explainable LLM systems.

---

## 📄 Proposal
📥 [Read the 1-Page Proposal (PDF)](docs/proposal_1pager.pdf)

---

## 🧠 Project Highlights

- **LangGraph-style Memory:** Context tracking over multiple conversation turns
- **Causal Reasoning with IV:** Using `DoWhy` for explainable decisions
- **Streamlit Dashboard:** Visualizing memory & decision reasoning live
- **Modular Architecture:** Easy to extend and integrate with GPT-4 or Claude

---

## 📁 Folder Structure
BenIV-Agent/
├── app/
│ ├── main.py # Streamlit UI
│ ├── memory_manager.py # LangGraph-style memory
│ └── iv_reasoning.py # IV simulation (DoWhy)
├── data/
│ └── sample_dialogues.json
├── assets/
│ └── diagrams/
├── docs/
│ └── proposal_1pager.pdf
├── requirements.txt
└── README.md

