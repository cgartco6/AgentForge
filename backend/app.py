from flask import Flask, request, jsonify
from agents.director_agent import DirectorAgent
from utils.security_utils import SecurityManager
import threading
import os
import sys

app = Flask(__name__)
security_manager = SecurityManager()
director = DirectorAgent()

# Create core agents on startup
core_agents = [
    "marketing", "social_media", "security",
    "self_healing", "training", "compliance", "payments"
]

for agent_type in core_agents:
    director.create_agent(agent_type)

@app.route('/')
def home():
    return "AgentForge AI Ecosystem is running"

@app.route('/create-agent', methods=['POST'])
def create_agent():
    if not security_manager.verify_request(request):
        return jsonify({"error": "Security verification failed"}), 403
    
    data = request.json
    agent_type = data.get('agent_type')
    params = data.get('params', {})
    
    try:
        new_agent = director.create_agent(agent_type, params)
        return jsonify({
            "status": "success",
            "agent_id": new_agent.agent_id,
            "agent_type": agent_type
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/execute-task', methods=['POST'])
def execute_task():
    if not security_manager.verify_request(request):
        return jsonify({"error": "Security verification failed"}), 403
    
    data = request.json
    agent_id = data.get('agent_id')
    task = data.get('task')
    params = data.get('params', {})
    
    agent = director.get_agent(agent_id)
    if not agent:
        return jsonify({"error": "Agent not found"}), 404
    
    try:
        # Run in background thread
        def task_runner():
            try:
                result = agent.execute(task, params)
                print(f"Task completed: {task} by {agent_id}")
            except Exception as e:
                print(f"Task failed: {e}")
        
        thread = threading.Thread(target=task_runner)
        thread.daemon = True
        thread.start()
        
        return jsonify({"status": "task_started", "task": task})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/generate-code', methods=['POST'])
def generate_code():
    if not security_manager.verify_request(request):
        return jsonify({"error": "Security verification failed"}), 403
    
    data = request.json
    language = data.get('language', 'python')
    description = data.get('description')
    
    if not description:
        return jsonify({"error": "Description is required"}), 400
    
    try:
        code = director.generate_code(language, description)
        return jsonify({
            "status": "success",
            "language": language,
            "code": code
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/system-status', methods=['GET'])
def system_status():
    return jsonify({
        "status": "operational",
        "agents_count": len(director.agents),
        "resource_usage": {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
