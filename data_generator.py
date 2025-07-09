import random, time, json
from datetime import  datetime
from itertools import cycle
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

patient_ids = cycle([101, 102, 103, 104, 105])

def generate_vitals():
    patient_id = next(patient_ids)
    temperature = round(random.uniform(96.5, 100.5), 1)
    heart_rate = random.randint(60, 125)
    oxygen_level = random.randint(85, 100)
    bp = f"{random.randint(100, 145)}/{random.randint(60, 90)}"
    timestamp = datetime.now().isoformat()

    return {
        "timestamp": timestamp,
        "temperature": temperature,
        "patient_id": patient_id,
        "heart_rate": heart_rate,
        "blood_pressure": bp,
        "oxygen_level": oxygen_level
    }

while True:
    data = generate_vitals()
    producer.send("patient-vitals", value=data)
    print(f"Sent : {data}")
    time.sleep(3)
