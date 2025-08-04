import time
import random
from datetime import datetime

class PaymentProcessor:
    def __init__(self):
        self.currencies = ["ZAR", "USD", "EUR", "GBP"]
        self.transaction_count = 0
        print("Payment Processor initialized")
    
    def validate_currency(self, currency):
        return currency in self.currencies
    
    def validate_amount(self, amount):
        return amount > 0
    
    def process(self, amount, currency, recipient):
        if not self.validate_currency(currency):
            raise ValueError(f"Unsupported currency: {currency}")
        if not self.validate_amount(amount):
            raise ValueError("Amount must be positive")
        
        # Simulate payment processing
        time.sleep(0.5)
        
        self.transaction_count += 1
        transaction_id = f"TX-{str(self.transaction_count).zfill(6)}"
        
        return {
            "transaction_id": transaction_id,
            "amount": amount,
            "currency": currency,
            "recipient": recipient,
            "status": "completed",
            "fee": round(amount * 0.02, 2),  # 2% transaction fee
            "timestamp": datetime.now().isoformat()
        }
    
    def get_exchange_rate(self, from_currency, to_currency):
        """Get currency exchange rate"""
        # Simulated exchange rates
        rates = {
            "USD": {"ZAR": 18.5, "EUR": 0.85, "GBP": 0.75},
            "ZAR": {"USD": 0.054, "EUR": 0.046, "GBP": 0.041},
            "EUR": {"USD": 1.18, "ZAR": 21.74, "GBP": 0.88},
            "GBP": {"USD": 1.33, "ZAR": 24.39, "EUR": 1.14}
        }
        
        if from_currency == to_currency:
            return 1.0
        if from_currency in rates and to_currency in rates[from_currency]:
            return rates[from_currency][to_currency]
        return None
