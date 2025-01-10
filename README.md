# Uncommon Python Error: Silent Infinity Return

This repository demonstrates an uncommon error in Python: silently returning infinity (inf) instead of raising an exception for division by zero.  The code includes an example of this behavior and a solution that provides better error handling.

**The Problem:**
The `function_with_uncommon_error` function handles division by zero by returning `float('inf')`. While this avoids a `ZeroDivisionError`, it can lead to unexpected behavior, especially if the calling code doesn't explicitly check for and handle infinity values.  The silent nature of this error makes it harder to debug.

**The Solution:**
The solution demonstrates how to replace this uncommon behavior with a more standard and robust error-handling mechanism, using a `try-except` block to catch and explicitly handle the `ZeroDivisionError`.