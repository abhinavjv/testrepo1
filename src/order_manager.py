import math
import os # BUG: LINTING - Unused import

def process_bulk_order(items, unit_price, tax_rate):
    """
    Processes a list of items and applies tax and discounts.
    """
    total_cost = 0.0
    
    # BUG: SYNTAX error - Missing colon at the end of the if statement
    if len(items) == 0
        return 0.0
        
    for item in items:
    # BUG: INDENTATION error - logic inside for-loop not indented
    total_cost += unit_price
        
    # BUG: LOGIC error - using multiplication for tax instead of (1 + tax)
    # Should be: total_cost * (1 + tax_rate)
    final_price = total_cost * tax_rate
    
    # BUG: TYPE_ERROR - trying to add a string to a float
    message = "Total processed: " + final_price
    
    if final_price > 1000:
        print("High value order detected")
        
    return final_price

# Line 28: Unused import 'os'