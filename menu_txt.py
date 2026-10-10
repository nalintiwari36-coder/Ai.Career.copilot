
def analyze_career():
    print("Career analysis started!")

def compare_careers():
    print("Career comparison started!")

while True:
    print("\n===== AI CAREER COPILOT =====")
    print("1. Analyze Career Skills")
    print("2. Compare Careers")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        analyze_career()

    elif choice == "2":
        compare_careers()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
