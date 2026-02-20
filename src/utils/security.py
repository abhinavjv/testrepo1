import hashlib

def hash_password(password):
    # BUG: TYPE_ERROR - hashlib requires bytes, but string is passed
    # Fix: password.encode()
    return hashlib.sha256(password).hexdigest()

def validate_api_key(key):
    # BUG: SYNTAX error - missing closing parenthesis
    if len(key < 16:
        return False
        
    # BUG: INDENTATION error - nested block mismatch
    if key.startswith("TEST_"):
    print("Warning: Using test key")
        return True
        
    # BUG: LOGIC error - checking length instead of content
    if key == 16:
        return True
        
    return False