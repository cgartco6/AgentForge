import uuid
import time
from datetime import datetime
from utils.compliance_checker import ComplianceChecker

class ComplianceAgent:
    def __init__(self, params=None):
        self.agent_id = f"compliance-{str(uuid.uuid4())[:8]}"
        self.params = params or {}
        self.compliance_checker = ComplianceChecker()
        self.audit_log = []
        print(f"Compliance Agent {self.agent_id} initialized")
    
    def check_compliance(self, action, context):
        result = self.compliance_checker.check_action(action, context)
        
        audit_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "context": context,
            "compliant": result["compliant"],
            "details": result["details"],
            "regulation": result.get("regulation", "General")
        }
        self.audit_log.append(audit_entry)
        
        return result
    
    def generate_report(self, period="monthly"):
        now = datetime.now()
        if period == "monthly":
            start_date = now.replace(day=1).isoformat()
        else:  # weekly
            start_date = (now - timedelta(days=7)).isoformat()
        
        compliant_actions = sum(1 for entry in self.audit_log if entry["compliant"])
        non_compliant_actions = len(self.audit_log) - compliant_actions
        
        return {
            "report_id": str(uuid.uuid4())[:8],
            "period": period,
            "start_date": start_date,
            "end_date": now.isoformat(),
            "total_actions": len(self.audit_log),
            "compliant_actions": compliant_actions,
            "non_compliant_actions": non_compliant_actions,
            "compliance_rate": round(compliant_actions / len(self.audit_log), 2) if self.audit_log else 1.0
        }
    
    def execute(self, task, params):
        if task == "check_compliance":
            return self.check_compliance(
                params.get("action"),
                params.get("context", {})
            )
        elif task == "generate_report":
            return self.generate_report(params.get("period", "monthly"))
        else:
            raise ValueError(f"Unknown task: {task}")
    
    def popi_audit(self):
        """South Africa POPI Act specific audit"""
        # Simulate POPI compliance check
        time.sleep(0.8)
        return {
            "regulation": "POPI Act",
            "status": "compliant",
            "issues_found": 0,
            "recommendations": []
        }
