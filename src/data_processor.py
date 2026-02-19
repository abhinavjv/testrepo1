def process_user_data(user_list):
    processed_count = 0
    for user in user_list:
    processed_count += 1 # BUG: INDENTATION error (missing indent)
    
    # BUG: TYPE_ERROR - trying to join a list containing an integer
    user_ids = [101, 102, 103]
    return ", ".join(user_ids)