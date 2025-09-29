# apps/fraud-consumer/fraud_consumer.py
import sys
import collections

if sys.version_info >= (3, 10):
    if not hasattr(collections, 'MutableMapping'):
        collections.MutableMapping = collections.abc.MutableMapping

from kafka import KafkaConsumer
import json

def main():
    print("🔍 Fraud Detection Consumer")
    print("👂 Listening for payment events...\n")
    
    consumer = KafkaConsumer(
        'user-payments',
        bootstrap_servers=['localhost:9094'],
        auto_offset_reset='latest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    
    for message in consumer:
        event = message.value
        amount = event['amount']
        
        # Simple fraud rule: flag transactions > $500
        if amount > 500:
            print(f"🚨 FRAUD ALERT! High-value transaction:")
            print(f"   User: {event['userId']}")
            print(f"   Amount: ${amount}")
            print(f"   Merchant: {event['merchant']}")
            print(f"   IP: {event['ipAddress']}\n")
        else:
            print(f"✅ Normal transaction: ${amount} for {event['userId']}")

if __name__ == "__main__":
    main()