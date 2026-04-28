\# OpsPilot AI — AI Personal Operations Manager



OpsPilot AI is an AI-powered automation system that analyzes leads and tasks from a MySQL database, generates a daily operational briefing using Groq LLM, sends the briefing via Gmail, and logs the results back into MySQL.



\---



\## 🚀 Problem



Freelancers and small teams often manage:

\- leads

\- follow-ups

\- deadlines

\- tasks



manually or across scattered tools.



This leads to:

\- missed opportunities

\- poor prioritization

\- inconsistent follow-ups



\---



\## 💡 Solution



OpsPilot AI acts as a \*\*daily AI assistant\*\* that:



\- reads your operational data

\- analyzes it using an LLM

\- generates actionable insights

\- delivers them automatically



\---



\## ⚙️ Tech Stack



\- \*\*n8n\*\* — automation orchestration  

\- \*\*MySQL (XAMPP)\*\* — data storage  

\- \*\*Groq API (LLaMA 3.3 70B)\*\* — AI reasoning  

\- \*\*Gmail OAuth2 API\*\* — notifications  

\- \*\*JavaScript (Code nodes)\*\* — data transformation  

\- \*\*Google Cloud Console\*\* — OAuth setup  



\---



\## 🧠 Features



\- Automated daily AI briefing

\- Lead prioritization

\- Task prioritization

\- Suggested follow-up messages

\- Gmail delivery

\- MySQL logging (history tracking)

\- Fully automated with schedule trigger



\---



\## 🔄 Workflow Architecture



```text

Schedule Trigger

↓

MySQL Leads + MySQL Tasks

↓

Merge Node

↓

Clean Data Code Node

↓

Groq Request Builder Code Node

↓

HTTP Request (Groq API)

↓

Briefing Extract Code Node

├── Gmail (Send Email)

└── MySQL (Insert Logs)




\---



\## 📊 Example Output

Daily Briefing



1.Summary:

You have 4 leads and 4 tasks with multiple pending follow-ups.

2.Top Priorities:

\-Follow up with Maya Haddad

\-Prepare AI receptionist demo script

\-Update portfolio README

3.Leads Requiring Follow-up:

\-Maya Haddad — proposal follow-up

\-Ahmad Nasser — demo preparation

\-Rana Khoury — initial contact

4\.Suggested Messages:

"Hi Maya, following up on the proposal..."




\---



\## 🛠️ Key Challenges Solved



\- Handling n8n node execution behavior

\- Fixing invalid JSON in API requests

\- Structuring data before sending to LLM

\- Managing OAuth2 authentication with Gmail

\- Designing a reliable automation pipeline



\---



\## 🧪 What I Learned



\- End-to-end AI automation design

\- API integration and debugging

\- Prompt engineering with structured data

\- Workflow orchestration with n8n

\- Building production-like systems



\---



\## 🔮 Future Improvements



\- React dashboard for briefing history

\- Error handling and retries

\- Lead scoring

\- Slack/Telegram integration

\- Multi-user support



\---



\## 🧑‍💻 Author



Mohamad — CS Graduate (2026)  

AI Developer / Automation Engineer  



\---



\## ⭐ Summary



This project demonstrates how AI can be integrated into automation pipelines to produce real business value.

