import math
import random
import statistics
import os
import sys

# ==========================================
#        MATH TOOLBOX LOGIC CLASSES
# ==========================================

class NumberTheory:
    @staticmethod
    def is_prime(n):
        if n <= 1: return False
        if n <= 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i += 6
        return True

    @staticmethod
    def generate_fibonacci(n):
        if n <= 0: return []
        if n == 1: return [0]
        seq = [0, 1]
        while len(seq) < n:
            seq.append(seq[-1] + seq[-2])
        return seq

    @staticmethod
    def factorial(n):
        if n < 0: return "Undefined for negative numbers"
        return math.factorial(n)

    @staticmethod
    def is_armstrong(n):
        num_str = str(n)
        power = len(num_str)
        return sum(int(digit) ** power for digit in num_str) == n

class Converter:
    @staticmethod
    def decimal_to_all(n):
        return {
            "Binary": bin(n)[2:],
            "Octal": oct(n)[2:],
            "Hexadecimal": hex(n)[2:].upper()
        }

class Geometry:
    @staticmethod
    def circle_area(radius):
        return math.pi * (radius ** 2)
        
    @staticmethod
    def rectangle_area(length, width):
        return length * width

class StatisticsCalc:
    @staticmethod
    def calculate_all(data):
        if not data: return "No data provided."
        return {
            "Mean": statistics.mean(data),
            "Median": statistics.median(data),
            "Mode": statistics.mode(data) if len(set(data)) < len(data) else "No mode",
            "Variance": statistics.variance(data) if len(data) > 1 else 0,
            "Max": max(data),
            "Min": min(data)
        }


# ==========================================
#          USER INTERFACE & APP
# ==========================================

class MathToolboxApp:
    def __init__(self):
        # Dictionary mapping for clean menu execution (avoids massive if/else)
        self.menu_options = {
            '1': self.handle_prime,
            '2': self.handle_fibonacci,
            '3': self.handle_factorial,
            '4': self.handle_armstrong,
            '5': self.handle_conversion,
            '6': self.handle_geometry,
            '7': self.handle_statistics,
            '8': self.exit_app
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self):
        self.clear_screen()
        print("╔══════════════════════════════════════════════╗")
        print("║          PYTHON MATH TOOLBOX v1.0            ║")
        print("╠══════════════════════════════════════════════╣")
        print("║                                              ║")
        print("║ 1. Prime Number Checker                      ║")
        print("║ 2. Fibonacci Generator                       ║")
        print("║ 3. Factorial Calculator                      ║")
        print("║ 4. Armstrong Number Checker                  ║")
        print("║ 5. Number System Converter                   ║")
        print("║ 6. Geometry Calculator                       ║")
        print("║ 7. Statistics Calculator                     ║")
        print("║ 8. Exit                                      ║")
        print("║                                              ║")
        print("╚══════════════════════════════════════════════╝")

    # --- Handler Methods ---
    def handle_prime(self):
        n = int(input("\nEnter a number to check if it's prime: "))
        if NumberTheory.is_prime(n):
            print(f"✅ {n} is a Prime Number.")
        else:
            print(f"❌ {n} is NOT a Prime Number.")

    def handle_fibonacci(self):
        n = int(input("\nHow many Fibonacci terms? "))
        print(f"Sequence: {NumberTheory.generate_fibonacci(n)}")

    def handle_factorial(self):
        n = int(input("\nEnter a number for factorial: "))
        print(f"{n}! = {NumberTheory.factorial(n)}")

    def handle_armstrong(self):
        n = int(input("\nEnter a number to check for Armstrong: "))
        if NumberTheory.is_armstrong(n):
            print(f"✅ {n} is an Armstrong Number.")
        else:
            print(f"❌ {n} is NOT an Armstrong Number.")

    def handle_conversion(self):
        n = int(input("\nEnter a decimal number to convert: "))
        results = Converter.decimal_to_all(n)
        for base, val in results.items():
            print(f"{base}: {val}")

    def handle_geometry(self):
        print("\n1. Circle Area\n2. Rectangle Area")
        sub_choice = input("Choose shape: ")
        if sub_choice == '1':
            r = float(input("Enter radius: "))
            print(f"Area: {Geometry.circle_area(r):.2f}")
        elif sub_choice == '2':
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            print(f"Area: {Geometry.rectangle_area(l, w):.2f}")

    def handle_statistics(self):
        print("\nEnter numbers separated by spaces (e.g., 5 10 15 20):")
        data = list(map(float, input("> ").split()))
        stats = StatisticsCalc.calculate_all(data)
        print("\n--- Statistics Results ---")
        for key, value in stats.items():
            if isinstance(value, float):
                print(f"{key}: {value:.2f}")
            else:
                print(f"{key}: {value}")

    def exit_app(self):
        print("\nExiting Math Toolbox. Have a great day!")
        sys.exit()

    # --- Main Application Loop ---
    def run(self):
        while True:
            self.display_header()
            choice = input("\nEnter your choice (1-8): ").strip()
            
            action = self.menu_options.get(choice)
            if action:
                try:
                    action()
                except ValueError:
                    print("\n❌ Invalid input! Please enter numbers only.")
                except Exception as e:
                    print(f"\n❌ An error occurred: {e}")
            else:
                print("\n❌ Invalid choice! Please select a valid menu option.")
                
            input("\nPress Enter to return to the main menu...")

# ==========================================
#               ENTRY POINT
# ==========================================
if __name__ == "__main__":
    app = MathToolboxApp()
    app.run()
