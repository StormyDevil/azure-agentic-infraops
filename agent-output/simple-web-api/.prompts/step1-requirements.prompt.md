---
name: step1-requirements
description: Generate Step 1 requirements document for simple web API project
agent: project-planner
model: claude-opus-4.5
tools:
  - read_file
  - create_file
---

Create requirements for a simple web API project with these specifications:

**Architecture Components:**

- Static web frontend hosted on Azure Static Web Apps (Free tier)
- Backend REST API using Azure Functions (Consumption plan)
- Data persistence with Azure Cosmos DB (Serverless, <100 requests/sec)
- Application monitoring with Application Insights

**Constraints:**

- Region: swedencentral
- Budget: $100/month
- No special compliance requirements
- Expected load: 10 concurrent users, 1000 requests/day
- SLA target: 99.9%
- RTO: 4 hours, RPO: 1 hour

**Output Requirements:**

Follow the template structure at [01-requirements.template.md](../../../.github/templates/01-requirements.template.md).
After approval, save to `agent-output/simple-web-api/01-requirements.md`

**Workflow:**

1. Research template structure and constraints
2. Generate draft requirements document
3. User reviews and provides feedback (iterate as needed)
4. User approves final version
5. Create `01-requirements.md` file in correct location
