# math_utils.py

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a}+{b}={result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a}*{b}={result}")
        return result

def utility_function(x):
    """Helper function"""
    return x * 2
