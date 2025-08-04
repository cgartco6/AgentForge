import uuid
import time
import random
from datetime import datetime
from utils.payment_processor import PaymentProcessor

class PaymentsAgent:
    def __init__(self, params=None):
        self.agent_id = f"payments-{str(uuid.uuid4())[:8]}"
        self.params = params or {}
        self.payment_processor = PaymentProcessor()
        self.transactions = []
        print(f"Payments Agent {self.agent_id} initialized")
    
    def process_payment(self, amount, currency, recipient):
        # Validate parameters
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        # Process payment
        transaction = self.payment_processor.process(amount, currency, recipient)
        self.transactions.append(transaction)
        return transaction
    
    def distribute_payments(self, payments):
        results = []
        for payment in payments:
            result = self.process_payment(
                payment["amount"],
                payment.get("currency", "ZAR"),
                payment["recipient"]
            )
            results.append(result)
        return results
    
    def execute(self, task, params):
        if task == "process_payment":
            return self.process_payment(
                params.get("amount"),
                params.get("currency", "ZAR"),
                params.get("recipient")
            )
        elif task == "distribute_payments":
            return self.distribute_payments(params.get("payments", []))
        else:
            raise ValueError(f"Unknown task: {task}")
    
    def auto_upgrade_system(self):
        """Automatic system upgrades when funds available"""
        # Simulate upgrade check
        time.sleep(0.5)
        if random.random() < 0.4:  # 40% chance upgrade is available
            return {
                "status": "upgraded",
                "new_version": f"2.{random.randint(0, 9)}",
                "cost": round(random.uniform(50, 200), 2)
            }
        return {"status": "no_upgrade_available"}
    
    def generate_invoice(self, client, amount, services):
        """Generate professional invoices"""
        return {
            "invoice_id": f"INV-{str(uuid.uuid4())[:8]}",
            "date": datetime.now().date().isoformat(),
            "client": client,
            "amount": amount,
            "currency": "ZAR",
            "services": services,
            "due_date": (datetime.now() + timedelta(days=30)).date().isoformat()
        }
