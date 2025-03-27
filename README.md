# 🧠 BaseOne Crew – Email Automation Agents

Welcome to the **BaseOne Email Automation Agents Crew** project, powered by [Sensai](https://sensai-consulting.com).  
This template is built to **automate email campaigns, responses, and communication** across various modalities using agentic AI workflows.

---

## 🚀 Installation

> **Requirements**: Python `>=3.10` and `<3.13`

This project uses [**UV**](https://docs.astral.sh/uv/) for fast dependency management and environment handling.

### 1. Install `uv` (if not already installed)

```bash
pip install uv
```

### 2. Navigate to the project directory

```bash
cd baseone-crew
```

### 3. Install project dependencies

```bash
crewai install
```

> _This will lock and install the required packages automatically._

---

## ⚙️ Configuration & Customisation

Before running, ensure you've set up your `.env` file with the required API keys.

### 🔑 Add API Keys

- Add your `OPENAI_API_KEY` to the `.env` file at the root of the project.

### 🛠️ Define Your Agents and Tasks

You can customise agents, tasks, logic, tools, and input configurations:

| File | Purpose |
|------|---------|
| `src/baseone_agents/analyst_crew/config/agents.yaml` | Define Analyst Crew agents |
| `src/baseone_agents/email_crew/config/agents.yaml` | Define Email Crew agents |
| `src/baseone_agents/analyst_crew/config/tasks.yaml` | Define Analyst Crew tasks |
| `src/baseone_agents/email_crew/config/tasks.yaml` | Define Email Crew tasks |
| `src/baseone_agents/crew.py` | Define overall logic, custom tools, and arguments |
| `src/baseone_agents/main.py` | Add your own CLI or input logic |
| `src/baseone_agents/tools/custom_tool.py` | Add custom tools (e.g., GHL BaseTool, BaseModel) |

> We're using [**Pydantic**](https://docs.pydantic.dev/latest/) for consistent, validated data ingestion and flow between agents.

---

## ▶️ Running the Project

Once configured, start the automation flow from the root directory:

```bash
crewai run
```

This will launch the `baseone_agents` flow and activate your defined agents and tasks.

---

## 👥 Understanding Your Crew

The **BaseOne Crew** is a set of autonomous AI agents, each assigned a specific role and goal. These agents collaborate through a defined set of tasks to execute complex workflows.

### 🧩 Components Overview

- **Agents Config:**  
  `src/baseone_agents/analyst_crew/config/agents.yaml`  
  `src/baseone_agents/email_crew/config/agents.yaml`

- **Tasks Config:**  
  `src/baseone_agents/analyst_crew/config/tasks.yaml`  
  `src/baseone_agents/email_crew/config/tasks.yaml`

- **Custom Logic & Tools:**  
  `src/baseone_agents/tools/custom_tool.py` includes initial tools like **GHL BaseTool** and **BaseModel**.

---

## 📞 Support

Need help or have feedback?

- 📧 Email: [support@sensai-consulting.com](mailto:support@sensai-consulting.com)  
- 📚 Documentation: [CrewAI Docs](https://docs.crewai.com)

---

## ✅ Final Notes

Make sure to:

- Regularly update the agent/task configurations as your workflow evolves.
- Keep dependencies up to date with `crewai install` as needed.
- Reach out to the Sensai team for strategic improvements or bespoke automation needs.

---

**Built with 💡 by Sensai**  
_Elevating enterprise efficiency through agentic intelligence_