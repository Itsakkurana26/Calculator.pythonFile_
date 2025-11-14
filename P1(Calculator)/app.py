import os
import time

# --------- Basic Arithmetic Functions ----------
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error! Division by zero."
    return x / y

# --------- Display History ----------
def show_history(history):
    if not history:
        print("\n📜 No calculations yet.")
    else:
        print("\n📜 Calculation History:")
        for i, record in enumerate(history, 1):
            print(f"{i}. {record}")

# --------- Main Program ----------
def main():
    history = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears screen for neatness
        print("=" * 40)
        print("       🧮  PYTHON CALCULATOR  🧮")
        print("=" * 40)
        print("1️⃣  Add")
        print("2️⃣  Subtract")
        print("3️⃣  Multiply")
        print("4️⃣  Divide")
        print("5️⃣  View History")
        print("6️⃣  Clear History")
        print("7️⃣  Exit")
        print("-" * 40)

        choice = input("👉 Enter your choice (1-7): ").strip()

        if choice == '7':
            print("\n👋 Exiting Calculator... Goodbye!")
            time.sleep(1)
            break

        elif choice == '5':
            show_history(history)
            input("\nPress Enter to continue...")

        elif choice == '6':
            history.clear()
            print("\n🧹 History cleared!")
            time.sleep(1)

        elif choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❗ Invalid input! Please enter numeric values.")
                time.sleep(1.5)
                continue

            if choice == '1':
                result = add(num1, num2)
                op = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op = '/'

            record = f"{num1} {op} {num2} = {result}"
            history.append(record)

            print(f"\n✅ Result: {record}")
            input("\nPress Enter to continue...")

        else:
            print("❗ Invalid choice! Please select a valid option.")
            time.sleep(1.5)

# --------- Run the Program ----------
if __name__ == "__main__":
    main()
