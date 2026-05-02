# OpsPilot AI — AI Personal Operations Manager

OpsPilot AI is an AI-powered operations assistant that analyzes leads and tasks, generates a daily briefing using an LLM (Groq), sends it via Gmail, and stores the results in MySQL.

The system combines **n8n automation + FastAPI backend** to create a scalable and production-style architecture.

---

## 🚀 Problem

Freelancers and small teams often manage:

- leads
- follow-ups
- deadlines
- tasks

manually or across multiple tools.

This leads to:
- missed opportunities
- poor prioritization
- inconsistent follow-ups

---

## 💡 Solution

OpsPilot AI automates daily operations by:

1. Fetching data from MySQL
2. Processing it through a FastAPI backend
3. Sending structured data to an LLM (Groq)
4. Generating a daily actionable briefing
5. Sending it via Gmail
6. Logging results into MySQL

---

## ⚙️ Tech Stack

- **n8n** — workflow automation  
- **FastAPI** — backend API layer  
- **MySQL (XAMPP)** — database  
- **Groq API (LLaMA 3.3 70B)** — AI reasoning  
- **Gmail API (OAuth2)** — notifications  
- **JavaScript (n8n Code nodes)** — data transformation  
- **Python** — backend logic  

---

## 🧠 Key Features

- Daily AI-generated briefing
- Lead prioritization
- Task prioritization
- Suggested follow-up messages
- Email delivery via Gmail
- MySQL logging (history)
- Manual trigger via API
- Fully automated scheduled execution
- Token-optimized AI input

---

## 🔄 System Architecture

```text
FastAPI (Backend Layer)
    ↓
n8n (Automation Engine)
    ↓
Groq (AI Reasoning)
    ↓
Gmail + MySQL Logs



🔁 Workflow (n8n):

Webhook Trigger / Schedule Trigger
↓
FastAPI HTTP Request (/operations/summary-data)
↓
Clean Code Node
↓
Groq Request Builder
↓
HTTP Request (Groq API)
↓
Extract AI Response
├── Gmail (Send Email)
└── MySQL (Save Briefing)


🔌 FastAPI Endpoints
GET /health/db → check DB connection
GET /leads → fetch active leads
GET /tasks → fetch pending tasks
GET /operations/summary-data → optimized AI input
GET /briefings → fetch recent AI briefings
POST /trigger-briefing → trigger n8n workflow
⚡ Token Optimization (Important)

The system reduces token usage by:

1. Backend Filtering (FastAPI)

Instead of sending full database records:
email, notes, ids ❌
We send only:
name, company, priority, dates, status ✅

2. Prompt Optimization (n8n)

Reduced verbose instructions to a concise structure:
Analyze data → return summary, priorities, follow-ups


Result:
Prompt tokens reduced:
947 → 488 (~49% reduction)


📊 Example Output:
Daily Briefing

1. Summary:
You have 4 leads and 4 tasks with pending follow-ups.

2. Top Priorities:
- Follow up with Maya Haddad
- Prepare demo script
- Update portfolio

3. Follow-ups:
- Maya Haddad — proposal
- Ahmad Nasser — demo
- Karim Saad — chatbot request

4. Suggested Messages:
"Hi Maya, following up on the proposal..."


🧠 Key Engineering Concepts Demonstrated
API-driven architecture
Service-to-service communication
Workflow orchestration
Backend + automation separation
LLM prompt engineering
Token optimization
Data filtering for AI efficiency
Webhook-based triggering
Production vs test environments


🧪 What I Learned
Building end-to-end AI systems
Connecting backend APIs with automation tools
Debugging real API issues
Designing scalable AI workflows
Optimizing LLM usage for cost and performance


🔮 Future Improvements
React dashboard for UI
Lead scoring system
Multi-user support
Slack / WhatsApp notifications
Error handling & retry logic
Deployment (Docker / cloud)


🧑‍💻 Author

Mohamad — CS Graduate (2026)
AI Developer / Automation Engineer


⭐ Summary

This project demonstrates how to move beyond simple AI demos and build a real AI-powered system with backend control, automation, and scalable architecture.

