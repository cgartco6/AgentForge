import uuid
import threading
import time
import psutil
from agents.marketing_agent import MarketingAgent
from agents.social_media_agent import SocialMediaAgent
from agents.security_agent import SecurityAgent
from agents.self_healing_agent import SelfHealingAgent
from agents.training_agent import TrainingAgent
from agents.compliance_agent import ComplianceAgent
from agents.payments_agent import PaymentsAgent
from utils.security_utils import SecurityManager
from utils.compliance_checker import ComplianceChecker

class DirectorAgent:
    def __init__(self):
        self.agent_id = f"director-{str(uuid.uuid4())[:8]}"
        self.agents = {}
        self.security_manager = SecurityManager()
        self.compliance_checker = ComplianceChecker()
        self.lock = threading.Lock()
        self.resource_monitor_active = True
        print(f"Director Agent {self.agent_id} initialized")
        
        # Start resource monitoring
        self.monitor_thread = threading.Thread(target=self.monitor_system_resources)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()
    
    def create_agent(self, agent_type, params=None):
        agent_classes = {
            "marketing": MarketingAgent,
            "social_media": SocialMediaAgent,
            "security": SecurityAgent,
            "self_healing": SelfHealingAgent,
            "training": TrainingAgent,
            "compliance": ComplianceAgent,
            "payments": PaymentsAgent
        }
        
        if agent_type not in agent_classes:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        # Security and compliance check
        if not self.security_manager.verify_agent_creation(agent_type, params):
            raise PermissionError("Security policy violation in agent creation")
        
        if not self.compliance_checker.check_agent_compliance(agent_type, params):
            raise ValueError("Agent creation violates compliance rules")
        
        with self.lock:
            agent = agent_classes[agent_type](params)
            self.agents[agent.agent_id] = agent
            print(f"Created new {agent_type} agent: {agent.agent_id}")
            return agent
    
    def get_agent(self, agent_id):
        with self.lock:
            return self.agents.get(agent_id)
    
    def generate_code(self, language, description):
        # In production, this would connect to an LLM
        if language.lower() == 'python':
            return f"# {description}\n\ndef main():\n    print('Hello from AgentForge!')\n\nif __name__ == '__main__':\n    main()"
        elif language.lower() == 'javascript':
            return f"// {description}\n\nfunction main() {{\n    console.log('Hello from AgentForge!');\n}}\n\nmain();"
        else:
            return f"# Generated {language} code\n# {description}\n\n# Language support coming soon"
    
    def execute(self, task, params):
        if task == "create_agent":
            return self.create_agent(params.get('agent_type'), params.get('params', {}))
        elif task == "generate_code":
            return self.generate_code(params.get('language', 'python'), params.get('description', ''))
        else:
            raise ValueError(f"Unknown task: {task}")
    
    def monitor_system_resources(self):
        """Monitor system resources and scale agent activity"""
        while self.resource_monitor_active:
            cpu_percent = psutil.cpu_percent(interval=1)
            mem = psutil.virtual_memory()
            
            # Adjust agent activity based on resources
            if cpu_percent > 80 or mem.percent > 80:
                print(f"High resource usage! CPU: {cpu_percent}%, Mem: {mem.percent}%")
                self.throttle_agents()
            
            time.sleep(10)
    
    def throttle_agents(self):
        """Reduce agent activity during high resource usage"""
        for agent_id, agent in list(self.agents.items()):
            if isinstance(agent, (TrainingAgent, SelfHealingAgent)):
                print(f"Throttling resource-intensive agent: {agent_id}")
    
    def shutdown(self):
        """Clean shutdown of all agents"""
        self.resource_monitor_active = False
        print("Shutting down all agents...")
        for agent_id in list(self.agents.keys()):
            self.remove_agent(agent_id)
    
    def remove_agent(self, agent_id):
        """Remove an agent from the system"""
        with self.lock:
            if agent_id in self.agents:
                agent = self.agents.pop(agent_id)
                print(f"Removed agent: {agent_id}")
                # Perform any cleanup needed for the agent
