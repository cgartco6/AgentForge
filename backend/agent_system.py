from agents.director_agent import DirectorAgent
import time

def main():
    print("Starting AgentForge Ecosystem...")
    
    # Initialize director agent
    director = DirectorAgent()
    
    try:
        # Create initial agents
        print("\nCreating core agents...")
        marketing_agent = director.create_agent("marketing")
        social_agent = director.create_agent("social_media")
        security_agent = director.create_agent("security")
        healing_agent = director.create_agent("self_healing")
        training_agent = director.create_agent("training")
        compliance_agent = director.create_agent("compliance")
        payments_agent = director.create_agent("payments")
        
        print("\nAgent System Initialized. All agents are operational.")
        
        # Keep the system running
        while True:
            time.sleep(10)
            # System heartbeat
            print("System heartbeat: Agents active")
    except KeyboardInterrupt:
        print("\nShutting down AgentForge ecosystem...")
        director.shutdown()
        print("Ecosystem stopped.")

if __name__ == "__main__":
    main()
