import hashlib


def hashing(s: str):
    """FUNCTION: hashes strings"""
    return hashlib.sha256(s.encode()).hexdigest()


def verify(plain, hashed):
    if hashing(plain) == hashed:
        return True
    return False
