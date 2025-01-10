def function_with_uncommon_error(x, y):
    if x == 0:
        return 0  # Correct handling of x == 0
    elif y == 0:
        return float('inf') # This will return an infinity value and does not raise any error, but it is uncommon
    else:
        return x / y

result = function_with_uncommon_error(5,0)
print(result)