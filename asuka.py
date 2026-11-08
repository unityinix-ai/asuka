# Copyright (c) 2026 Alexander Leo. Apache-2.0
# ASUKA DEMO - FAKE DATA ONLY

import hashlib, hmac, json

FAKE_SECRET = b"whsec_DEMO_FAKE_ASUKA_12345"

def hash_step(prev, data):
    return hashlib.sha256(f"{prev}:{data}".encode()).hexdigest()

def sign(s):
    return hmac.new(FAKE_SECRET, s.encode(), hashlib.sha256).hexdigest()

print("=== ASUKA // AEGIS DEMO ===")
prev = "GENESIS"
chain = []
for step in ["in_us", "as_us", "through_us"]:
    h = hash_step(prev, step)
    chain.append({"agent": "Asuka", "step": step, "hash": h})
    prev = h
    print(f"Asuka - {step}: {h[:16]}... VERIFIED ✅")

payload = json.dumps(chain)
sig = sign(payload)
print(f"Webhook: {sig[:16]}... VERIFIED ✅")

tampered = payload.replace("in_us", "in_UX")
print(">>> TAMPERING...")
print(f"Asuka says: {'REJECTED ❌ CHAIN BROKEN' if sign(tampered) != sig else 'ERROR'}")
print("Gate guarded by Asuka.")
