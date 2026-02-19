import json
import time # BUG: LINTING - Unused import

def get_config():
    # BUG: IMPORT error - referencing a library not in requirements.txt
    import requests_oauthlib 
    return {"status": "connected"}