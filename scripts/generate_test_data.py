from faker import Faker
import json, random, uuid

f = Faker()
def make_user():
    return {
        "id": str(uuid.uuid4()),
        "name": f.name(),
        "email": f.email(),
        "currency": random.choice(["INR","USD","EUR","GBP"]),
        "amount": random.choice([999,1499,1999,2599,3499])
    }

if __name__ == "__main__":
    print(json.dumps([make_user() for _ in range(5)], indent=2))
