// Animation on scroll
document.addEventListener('DOMContentLoaded', function() {
    const animatedElements = document.querySelectorAll('.animated');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, {
        threshold: 0.1
    });
    
    animatedElements.forEach(element => {
        observer.observe(element);
    });
});

// Agent creation functions
function createAgent(agentType, fromTerminal = false) {
    const agentNames = {
        'director': 'Director Agent',
        'marketing': 'Marketing Agent',
        'social_media': 'Social Media Agent',
        'security': 'Security Agent',
        'self_healing': 'Self-Healing Agent',
        'training': 'Training Agent',
        'compliance': 'Compliance Agent',
        'payments': 'Payments Agent'
    };
    
    const terminal = document.getElementById('terminal-output');
    if (fromTerminal) {
        terminal.innerHTML += `<div class="terminal-line">> Creating ${agentNames[agentType]}...</div>`;
        terminal.scrollTop = terminal.scrollHeight;
    }
    
    // In a real implementation, this would call the backend API
    // For now, we'll simulate the response
    setTimeout(() => {
        const agentId = `AG-${Math.floor(1000 + Math.random() * 9000)}`;
        const message = `> ${agentNames[agentType]} created! Agent ID: ${agentId}`;
        
        if (fromTerminal) {
            terminal.innerHTML += `<div class="terminal-line success">${message}</div>`;
        } else {
            alert(message);
        }
        
        terminal.scrollTop = terminal.scrollHeight;
    }, 1000);
}

function showAgentInfo(agentType) {
    const agentInfo = {
        'director': 'The Director Agent manages all other agents in the ecosystem. It can create new agents, assign tasks, and coordinate complex projects.',
        'marketing': 'The Marketing Agent creates and manages digital marketing campaigns across all channels. It analyzes performance and optimizes strategies.',
        'social_media': 'This agent posts content to all social platforms (Facebook, Instagram, Twitter, TikTok, etc.) and engages with your audience.',
        'security': 'Security Agent provides military-grade protection with encryption, threat detection, and anti-cloning measures.',
        'self_healing': 'This agent continuously monitors the system, automatically fixing issues and applying updates without downtime.',
        'training': 'Training Agent manages model training and retraining processes using the latest data and techniques.',
        'compliance': 'Ensures all operations comply with South African (POPI) and international regulations. Automates compliance reporting.',
        'payments': 'Handles all financial transactions, distributions to owners, and automatic upgrades to paid services.'
    };
    
    alert(agentInfo[agentType]);
}

// Terminal command processing
function processCommand() {
    const input = document.getElementById('terminal-input');
    const command = input.value.trim().toLowerCase();
    const terminal = document.getElementById('terminal-output');
    
    if (!command) return;
    
    terminal.innerHTML += `<div class="terminal-line">> ${command}</div>`;
    
    if (command === 'help') {
        terminal.innerHTML += `<div class="terminal-line">Available commands:</div>`;
        terminal.innerHTML += `<div class="terminal-line">- create [agent_type] - Creates a new agent (e.g., create marketing_agent)</div>`;
        terminal.innerHTML += `<div class="terminal-line">- list_agents - Shows all active agents</div>`;
        terminal.innerHTML += `<div class="terminal-line">- run_task [agent_id] [task] - Executes a task on an agent</div>`;
        terminal.innerHTML += `<div class="terminal-line">- generate_code [language] [description] - Generates code based on description</div>`;
        terminal.innerHTML += `<div class="terminal-line">- clear - Clears the terminal</div>`;
    }
    else if (command.startsWith('create ')) {
        const agentType = command.split(' ')[1];
        createAgent(agentType, true);
    }
    else if (command === 'list_agents') {
        terminal.innerHTML += `<div class="terminal-line">Active agents:</div>`;
        terminal.innerHTML += `<div class="terminal-line">- Director Agent (AG-1001)</div>`;
        terminal.innerHTML += `<div class="terminal-line">- Marketing Agent (AG-2004)</div>`;
        terminal.innerHTML += `<div class="terminal-line">- Security Agent (AG-3007)</div>`;
    }
    else if (command === 'clear') {
        terminal.innerHTML = '';
    }
    else if (command.startsWith('generate_code ')) {
        const parts = command.split('"');
        if (parts.length < 2) {
            terminal.innerHTML += `<div class="terminal-line error">Usage: generate_code [language] "description"</div>`;
        } else {
            const lang = parts[0].split(' ')[1];
            const desc = parts[1];
            generateCodeFromTerminal(lang, desc);
        }
    }
    else {
        terminal.innerHTML += `<div class="terminal-line error">Unknown command: ${command}. Type 'help' for available commands.</div>`;
    }
    
    input.value = '';
    terminal.scrollTop = terminal.scrollHeight;
}

// Code generation
function generateCode() {
    const language = document.getElementById('language').value;
    const description = document.getElementById('description').value;
    const output = document.getElementById('code-output');
    
    if (!description) {
        alert('Please enter a description of what you want to build');
        return;
    }
    
    output.innerHTML = '<div class="terminal-line">Generating code... Please wait</div>';
    
    // Simulate code generation
    setTimeout(() => {
        let code = '';
        
        if (language === 'python') {
            code = `# ${description}\n\ndef main():\n    print("Hello from AgentForge!")\n\nif __name__ == "__main__":\n    main()`;
        }
        else if (language === 'javascript') {
            code = `// ${description}\n\nfunction main() {\n    console.log("Hello from AgentForge!");\n}\n\nmain();`;
        }
        else if (language === 'html') {
            code = `<!-- ${description} -->\n<!DOCTYPE html>\n<html>\n<head>\n    <title>AgentForge App</title>\n</head>\n<body>\n    <h1>Hello from AgentForge!</h1>\n</body>\n</html>`;
        }
        else {
            code = `// Generated ${language} code\n// ${description}\n\n// Code generation for ${language} is supported`;
        }
        
        output.textContent = code;
    }, 1500);
}

function generateCodeFromTerminal(language, description) {
    const terminal = document.getElementById('terminal-output');
    
    terminal.innerHTML += `<div class="terminal-line">> Generating ${language} code for: "${description}"</div>`;
    
    // Simulate code generation
    setTimeout(() => {
        let code = '';
        
        if (language === 'python') {
            code = `# ${description}\n\ndef main():\n    print("Hello from AgentForge!")\n\nif __name__ == "__main__":\n    main()`;
        }
        else if (language === 'javascript') {
            code = `// ${description}\n\nfunction main() {\n    console.log("Hello from AgentForge!");\n}\n\nmain();`;
        }
        else {
            code = `// Generated ${language} code\n// ${description}\n\n// Code generation for ${language} is supported`;
        }
        
        terminal.innerHTML += `<div class="terminal-line">> Code generated successfully:</div>`;
        terminal.innerHTML += `<div class="terminal-line code">${code}</div>`;
        terminal.scrollTop = terminal.scrollHeight;
    }, 1500);
}

// Handle Enter key in terminal
document.getElementById('terminal-input').addEventListener('keyup', function(e) {
    if (e.key === 'Enter') {
        processCommand();
    }
});
