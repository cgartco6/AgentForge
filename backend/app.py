from flask import Flask, request, jsonify
from agents.director_agent import DirectorAgent
from utils.security_utils import SecurityManager
import threading
import os
import sys

app = Flask(__name__, static_folder='../frontend', template_folder='../frontend')
security_manager = SecurityManager()
director = DirectorAgent()

@app.route('/')
def home():
    return app.send_static_file('index.html')

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
        # Run in a separate thread to avoid blocking
        thread = threading.Thread(target=agent.execute, args=(task, params))
        thread.start()
        return jsonify({"status": "task started", "task": task})
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

if __name__ == '__main__':
    # Check if we're running in a PyInstaller bundle
    if getattr(sys, 'frozen', False):
        template_folder = os.path.join(sys._MEIPASS, 'templates')
        app.template_folder = template_folder
        static_folder = os.path.join(sys._MEIPASS, 'static')
        app.static_folder = static_folder
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
