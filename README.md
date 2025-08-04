# AgentForge - AI Agent Ecosystem

AgentForge is a revolutionary AI ecosystem that enables the creation of specialized AI agents to handle complex projects. The Director Agent creates and manages sub-agents for tasks like marketing, social media, security, self-healing, compliance, and payments, all while ensuring military-grade security and automatic compliance with South African regulations.

## Key Features

- **Director Agent**: Creates and coordinates specialized agents
- **Marketing Agent**: Runs digital marketing campaigns
- **Social Media Agent**: Posts to all platforms 24/7
- **Security Agent**: Military-grade anti-cloning protection
- **Self-Healing Agent**: Auto-updates and repairs system
- **Training Agent**: Continuous model training and retraining
- **Compliance Agent**: Ensures POPI Act and GDPR compliance
- **Payments Agent**: Handles financial transactions
- **Code Generator**: Creates apps and scripts from descriptions
- **Terminal Interface**: Command-line control of agents

## System Requirements

AgentForge runs efficiently on these Windows configurations:
- **Minimum**: 
  - Windows 10 Pro
  - Intel i3 processor
  - 8GB RAM
  - 256GB SSD
- **Recommended**:
  - Windows 10/11 Pro
  - Intel i5/i7 processor
  - 16GB RAM
  - 512GB SSD

## Setup Instructions

### 1. Install Prerequisites
- Install [Python 3.10+](https://www.python.org/downloads/)
  - Check "Add Python to PATH" during installation
- Install [Git](https://git-scm.com/download/win)

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/AgentForge.git
cd AgentForge
```

### 3. Run the Ecosystem
Double-click the `run.bat` file to:
- Create a Python virtual environment
- Install required dependencies
- Start the backend server
- Open the web interface in your default browser

## Using the System

1. Access the web interface at http://localhost:5000
2. Explore the agent ecosystem:
   - Create new agents using the cards
   - Generate code with natural language descriptions
   - Use the terminal for advanced commands
3. Key terminal commands:
   - `create marketing_agent` - Creates marketing agent
   - `list_agents` - Shows active agents
   - `generate_code python "description"` - Generates Python code
   - `help` - Shows all commands

## Agent Capabilities

| Agent | Key Functions |
|-------|--------------|
| **Director** | Creates agents, coordinates tasks |
| **Marketing** | Campaign creation, performance analysis |
| **Social Media** | Post scheduling, content generation |
| **Security** | Encryption, threat monitoring, anti-cloning |
| **Self-Healing** | Health checks, auto-repair, updates |
| **Training** | Model training, retraining, optimization |
| **Compliance** | POPI/GDPR checks, audit reports |
| **Payments** | Transaction processing, auto-upgrades |

## Security and Compliance

- **Military-Grade Security**:
  - Anti-cloning and anti-theft protection
  - Data encryption at rest and in transit
  - Runtime integrity checks
- **Regulatory Compliance**:
  - South Africa POPI Act compliant
  - GDPR compatible
  - Financial sector regulations

## Troubleshooting

- **Port conflict**: If port 5000 is in use:
  - Edit `run.bat` and change `--port=5000` to an available port
- **Missing dependencies**:
  - Run `pip install -r backend/requirements.txt` manually
- **Firewall issues**: Allow Python through Windows Defender Firewall

## Support

For assistance, contact our support team:
- Email: support@agentforge.co.za
- Phone: +27 21 123 4567
- Hours: Mon-Fri, 9AM-5PM SAST

## License

AgentForge is licensed under the [Apache 2.0 License](LICENSE). Commercial use requires special permission for enterprise deployments.

---

**AgentForge** - Creating intelligent agents that build more intelligent agents to solve your most complex challenges.
