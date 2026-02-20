import json
import sys # BUG: LINTING - Unused import (Line 15)

def create_user_session(user_id, session_data):
    # BUG: IMPORT error - 'redis_lib' is not in requirements.txt
    import redis_lib
    
    # BUG: LOGIC error - checking for 'admin' inside a string instead of dict key
    if "role" == "admin": 
        print("Admin session created")
        
    # BUG: TYPE_ERROR - session_data is a dict, cannot be added to an integer
    session_expiry = 3600 + session_data
    
    # BUG: INDENTATION error - inconsistent whitespace
    if session_expiry > 4000:
    return "EXPIRED"
    else:
        return "ACTIVE"

# Line 15: Unused import 'sys'