def function_with_improved_error_handling(x, y):
    try:
        if x == 0:
            return 0
        else:
            return x / y
    except ZeroDivisionError:
        return float('nan') # Return NaN to indicate invalid result 
        # or raise a more specific exception like ValueError("Division by zero")

result = function_with_improved_error_handling(5,0)
print(result) #Output: nan