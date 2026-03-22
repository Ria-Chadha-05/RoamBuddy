<div align="center">

# 🌍 RoamBuddy

**An AI-powered travel chatbot built with Groq, Gradio, and a persona-driven prompt design.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Gradio](https://img.shields.io/badge/Gradio-UI-FF7C00?style=flat-square&logo=gradio&logoColor=white)](https://gradio.app/)
[![Groq](https://img.shields.io/badge/Groq-API-F55036?style=flat-square&logo=groq&logoColor=white)](https://groq.com/)
[![HuggingFace](https://img.shields.io/badge/Deployed_on-HuggingFace_Spaces-FFD21E?style=flat-square&logo=huggingface&logoColor=black)](https://huggingface.co/spaces)

[Overview](#-overview) · [Features](#-features) · [Tech Stack](#-tech-stack) · [System Architecture](#-system-architecture) · [Getting Started](#-getting-started) · [Persona](#-meet-arya--your-virtual-travel-guide) · [Limitations](#-known-limitations) · [Future Improvements](#-future-improvements)

**🔗 Live App:** [roambuddy.ccbp.tech](https://roambuddy.ccbp.tech)

</div>

---

## 📌 Overview

**RoamBuddy** is a **Generative AI–powered travel chatbot** built to demonstrate end-to-end deployment of a large language model–backed application.

The system integrates a **Python backend**, a **conversational Gradio UI**, and a **persona-driven prompt design** to deliver personalized, practical travel planning assistance — from budget itineraries to hidden local gems.

It is built for **learning and demonstration purposes**, showcasing how LLMs can be wrapped into real-world applications with persona conditioning, API integration, memory management, and cloud deployment.

---

## ✨ Features

### 🗺️ Conversational Travel Planning
- Ask anything — itineraries, budgets, local tips, visa info
- Natural, flowing chat interface powered by Groq's ultra-fast inference
- Persona-conditioned responses for a consistent tone and style

### 🧳 Persona-Driven Responses
- Responses styled by **Arya**, a friendly and street-smart virtual travel guide
- Advice that's practical, budget-aware, and experience-focused
- Consistent personality embedded at the system prompt level

### ⚡ Real-Time LLM Integration via Groq
- Direct integration with the **Groq API** for lightning-fast inference
- Powered by `openai/gpt-oss-120b` via Groq's OpenAI-compatible endpoint
- Stateless-friendly with short-term sliding window memory (last 4 turns)

### 🧠 Lightweight Conversation Memory
- Maintains context across the last 4 conversation turns
- Text trimming and message limiting prevent token overflow
- Graceful error handling for API failures

### 🖥️ Gradio Chat UI
- Clean, minimal chat interface built with **Gradio**
- No frontend setup required — runs out of the box
- Ships with example prompts to get users started instantly

### ☁️ Cloud Deployment
- Deployed and publicly accessible on **Hugging Face Spaces**
- API key managed securely via environment secrets
- Easy to fork, modify, and redeploy

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.x |
| **Frontend / UI** | Gradio |
| **LLM Provider** | Groq API |
| **Model** | `openai/gpt-oss-120b` (via Groq) |
| **Deployment** | Hugging Face Spaces |

---

## 🏗 System Architecture

RoamBuddy follows a clean request–response flow:

```
User Input (Gradio UI)
        ↓
TravelLLM Class (Python)
        ↓
Sliding Window Memory (last 4 turns)
        ↓
Persona Context Applied (System Prompt)
        ↓
Groq API → openai/gpt-oss-120b
        ↓
Generated Response
        ↓
Gradio UI (Real-Time Display) + Memory Updated
```

The chatbot is conditioned with a predefined travel-guide persona at the **system prompt level** to ensure consistent tone, style, and behavior across all conversations.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ria-Chadha-05/RoamBuddy
cd roambuddy
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Your API Key

Create a `.env` file in the root directory and add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

> **Note:** On Hugging Face Spaces, add this as a **Repository Secret** instead of a `.env` file.

### 4️⃣ Run the Application

```bash
python app.py
```

The app will be available at:

```
http://localhost:7860
```

---

## 🧭 Meet Arya – Your Virtual Travel Guide

> *"Pack light, explore boldly, and never skip the street food."*

| Attribute | Detail |
|---|---|
| **Name** | Arya |
| **Role** | Virtual Travel Guide |
| **Personality** | Adventurous, street-smart, friendly |
| **Response Style** | Practical, budget-aware, experience-focused |

Arya's persona is embedded directly into the system prompt, shaping every response RoamBuddy generates — so you always feel like you're getting advice from a well-travelled friend, not a search engine.

---

## 🎬 Demo

<p align="center">
  <a href="https://youtu.be/i0at05ba-9M">
    <img src="https://img.youtube.com/vi/i0at05ba-9M/maxresdefault.jpg" width="800">
  </a>
</p>

---

## ⚠️ Known Limitations

- **Rate Limits** — API usage is subject to Groq provider quotas
- **Quota Exhaustion** — Public access on free tiers may hit usage caps during high traffic
- **Short Memory** — Only the last 4 conversation turns are retained per session
- **No Persistent Memory** — Memory resets on every new session

---

## 🔮 Future Improvements

- 🧠 **Long-term conversation memory** for contextual multi-turn travel planning
- 🤖 **Model switching** to support Hugging Face–hosted open-source models
- 👤 **User-specific personalization** based on preferences and travel history
- 🛡️ **Enhanced error handling** with graceful fallback responses
- 🌐 **Multi-language support** for global travelers

---

## 👩‍💻 Author

**Ria Chadha**

---

<div align="center">

*Built with curiosity, caffeine, and a love for travel ✈️*

</div>
