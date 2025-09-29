# apps/payment-producer/payment_producer.py
import sys
import collections

# Python 3.10+ compatibility fix
if sys.version_info >= (3, 10):
    if not hasattr(collections, 'MutableMapping'):
        collections.MutableMapping = collections.abc.MutableMapping

from kafka import KafkaProducer
import json
import time
import uuid
import random

def create_producer():
    """Create Kafka producer with error handling"""
    try:
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9094'],  # Your external listener port
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            request_timeout_ms=10000,
            api_version_auto_timeout_ms=5000
        )
        print("✅ Kafka producer ready")
        return producer
    except Exception as e:
        print(f"❌ Producer creation failed: {e}")
        sys.exit(1)

def generate_payment_event(user_id=None):
    """Generate realistic payment event"""
    if user_id is None:
        user_id = f"user-{random.randint(1000, 9999)}"
    
    return {
        "txnId": str(uuid.uuid4()),
        "userId": user_id,
        "amount": round(random.uniform(10.00, 1000.00), 2),
        "currency": "USD",
        "merchant": random.choice(["Amazon", "Netflix", "Starbucks", "Apple", "Walmart"]),
        "cardLast4": str(random.randint(1000, 9999)),
        "ipAddress": f"203.0.{random.randint(1, 254)}.{random.randint(1, 254)}",
        "deviceType": random.choice(["mobile", "desktop", "tablet"]),
        "timestamp": time.time()
    }

def main():
    print("💳 Payment Event Producer")
    print("📡 Sending realistic payment events to Kafka...")
    print("⏹️  Press Ctrl+C to stop\n")
    
    producer = create_producer()
    event_count = 0
    
    try:
        while True:
            # Generate payment for same user (to simulate potential fraud pattern)
            user_id = f"user-{random.randint(1000, 1005)}"
            event = generate_payment_event(user_id)
            
            future = producer.send('user-payments', event)
            result = future.get(timeout=10)
            
            event_count += 1
            print(f"📤 [{event_count}] User: {event['userId']} | "
                  f"Amount: ${event['amount']} | "
                  f"Merchant: {event['merchant']} | "
                  f"Partition: {result.partition}")
            
            time.sleep(3)  # Send every 3 seconds
            
    except KeyboardInterrupt:
        print(f"\n🛑 Stopped after {event_count} events")
    finally:
        producer.close()
        print("👋 Producer closed")

if __name__ == "__main__":
    main()