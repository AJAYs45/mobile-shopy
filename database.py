# database.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")

# SSL handshake issue fix
client = MongoClient(MONGO_URL, tls=True, tlsAllowInvalidCertificates=True)
db = client["mobile_shopy"]
