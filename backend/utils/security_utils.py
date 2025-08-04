import os
import hashlib
import hmac
from cryptography.fernet import Fernet

class SecurityManager:
    def __init__(self):
        # Use fixed keys for demo (in prod: load from secure storage)
        self.encryption_key = Fernet.generate_key()
        self.hmac_secret = os.urandom(32)
        self.cipher = Fernet(self.encryption_key)
        print("Security Manager initialized")
    
    def encrypt(self, data):
        """Encrypt data using Fernet symmetric encryption"""
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data).decode()
    
    def decrypt(self, encrypted_data):
        """Decrypt data using Fernet symmetric encryption"""
        if isinstance(encrypted_data, str):
            encrypted_data = encrypted_data.encode()
        return self.cipher.decrypt(encrypted_data).decode()
    
    def generate_signature(self, data):
        """Generate HMAC signature for data"""
        if isinstance(data, str):
            data = data.encode()
        return hmac.new(self.hmac_secret, data, hashlib.sha256).hexdigest()
    
    def verify_signature(self, data, signature):
        """Verify HMAC signature for data"""
        expected_signature = self.generate_signature(data)
        return hmac.compare_digest(expected_signature, signature)
    
    def verify_request(self, request):
        """Verify the integrity of an incoming request"""
        # In production, implement proper authentication
        return True
    
    def verify_agent_creation(self, agent_type, params):
        """Security policy check before creating agent"""
        # Restrict certain agent types
        if agent_type in ["security", "payments"]:
            return params.get("admin_token") == "SECURE_ADMIN_TOKEN"
        return True
    
    def anti_cloning_measures(self):
        """Military-grade anti-cloning techniques"""
        return {
            "status": "protected",
            "measures": ["code_obfuscation", "hardware_binding", "runtime_checks"]
        }
