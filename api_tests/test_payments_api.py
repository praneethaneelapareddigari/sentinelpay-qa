import os, pytest, time, uuid

pytestmark = pytest.mark.api

def test_create_intent(base_url, session):
    payload = {"amount": 2599, "currency": os.getenv("CURRENCY","INR"), "idempotency_key": str(uuid.uuid4())}
    r = session.post(f"{base_url}/post", json=payload, timeout=10)
    assert r.status_code == 200
    j = r.json()
    assert j["json"]["amount"] == 2599
    assert "idempotency_key" in j["json"]

def test_confirm(base_url, session):
    r = session.post(f"{base_url}/status/200", json={}, timeout=10)
    assert r.status_code == 200

@pytest.mark.parametrize('reason', ['customer_request','fraud_suspected'])
def test_refund(base_url, session, reason):
    r = session.post(f"{base_url}/anything/refund", json={"reason":reason}, timeout=10)
    assert r.status_code == 200
    assert r.json()["json"]["reason"] == reason
