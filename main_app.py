# main_app.py
from math_utils import Calculator, utility_function

class App:
    def __init__(self):
        self.calc = Calculator()
    
    def run_demo(self):
        # Test calculator
        result1 = self.calc.add(3, 4)
        result2 = self.calc.multiply(5, 6)
        
        # Test utility
        doubled = utility_function(10)
        
        print(f"Results: {result1}, {result2}, {doubled}")

if __name__ == "__main__":
    app = App()
    app.run_demo()
