"""Offline password quality estimator. Never sends input to a network."""
import math

def estimate_password(password: str):
    if not password:
        return {"length":0,"entropy_bits":0.0,"score":0,"label":"empty"}
    pool=0
    if any(c.islower() for c in password): pool+=26
    if any(c.isupper() for c in password): pool+=26
    if any(c.isdigit() for c in password): pool+=10
    if any(not c.isalnum() for c in password): pool+=33
    entropy=len(password)*math.log2(max(pool,1))
    score=min(4, int(entropy/25))
    labels=["very weak","weak","fair","strong","very strong"]
    return {"length":len(password),"entropy_bits":round(entropy,1),"score":score,"label":labels[score]}
