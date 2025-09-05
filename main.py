import os
from smartapi import SmartConnect

API_KEY = os.getenv("API_KEY")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_PWD = os.getenv("CLIENT_PWD")
TOTP_PIN = os.getenv("TOTP_PIN")

obj = SmartConnect(api_key=API_KEY)
data = obj.generateSession(CLIENT_ID, CLIENT_PWD, TOTP_PIN)

print("✅ Connected to Angel SmartAPI")
