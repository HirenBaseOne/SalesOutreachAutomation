# BaseOne Crew

Welcome to the BaseOne Email Automation Agents Crew project, powered by [SenAI](https://sensai-consulting.com). This template is designed to automate email campaigns, responses and communication across different modalities

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/baseone_agents/analyst_crew/config/agents.yaml` and `src/baseone_agents/email_crew/config/agents.yaml` to define your agents
- Modify `src/baseone_agents/analyst_crew/config/tasks.yaml` and `src/baseone_agents/email_crew/config/tasks.yaml` to define your tasks
- Modify `src/baseon_agents/crew.py` to add your own logic, tools and specific args
- Modify `src/baseon_agents/main.py` to add custom inputs for your agents and tasks
- Modify `src/baseon_agents/tools/custom_tool.py` to add custom tools to the agents.  I have started by adding the GHL Basetool and Basemodel.  We are using [pydantic](https://docs.pydantic.dev/latest/) to standardise data ingestion and data flow throughout the agents coolaboration.
## Running the Project

To kickstart your flow and begin execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the baseon_agents Flow as defined in your configuration.


## Understanding Your Crew

The baseon_agents Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in the following files:

**Tasks:** `src/baseone_agents/analyst_crew/config/tasks.yaml`and `src/baseone_agents/email_crew/config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. 

**Agents:** `src/baseone_agents/analyst_crew/config/agents.yaml` and `src/baseone_agents/email_crew/config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the BaseOne Crew or crewAI.

- Contact Sensai support team direct on our dedicated emai support@sensai-consulting.com
- Visit CrewAI documentation [documentation](https://docs.crewai.com)


