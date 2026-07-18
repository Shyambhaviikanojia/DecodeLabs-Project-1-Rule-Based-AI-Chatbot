import random

def show_help():
    print("\nAvailable Commands:")
    print("1. hello / hi")
    print("2. stressed")
    print("3. tired")
    print("4. good")
    print("5. plan")
    print("6. break")
    print("7. motivate")
    print("8. challenge")
    print("9. streak")
    print("10. tip")
    print("11. focus")
    print("12. progress")
    print("13. mood")
    print("14. about")
    print("15. help")
    print("Type 'exit' to leave.")

def study_plan():
    days = input("Days left for exam: ")

    if days.isdigit():
        days = int(days)

        if days <= 3:
            print("Revise important topics and solve previous questions.")
        elif days <= 7:
            print("Complete topics and practice questions.")
        else:
            print("Learn new topics and revise regularly.")
    else:
        print("Enter a valid number.")

def take_break():
    input("Press Enter after taking a deep breath...")
    print("Drink water and stretch for 2 minutes.")
    print("Rest is also part of progress!")

def motivate():
    print(random.choice([
        "Small progress leads to big results!",
        "One step at a time. You've got this!",
        "Focus on progress, not perfection!"
    ]))

def challenge():
    print(random.choice([
        "Solve one coding problem today!",
        "Revise one difficult topic!",
        "Study without your phone for 30 minutes!",
        "Learn one new concept today!"
    ]))

def streak():
    days = input("Your study streak (days): ")

    if days.isdigit():
        print("🔥 Your streak is", days, "days!")
    else:
        print("Enter a valid number.")

def tip():
    print(random.choice([
        "Revise difficult topics regularly.",
        "Practice coding instead of only watching tutorials.",
        "Make short notes for revision.",
        "Explain concepts in your own words."
    ]))

def focus():
    print("🎯 Keep your phone away and study for 25 minutes.")
    print("Then take a short break and repeat.")

def progress():
    p = input("Syllabus completed (%): ")

    if p.isdigit():
        p = int(p)

        if p >= 80:
            print("Excellent! Focus on revision!")
        elif p >= 50:
            print("Good progress! Keep going!")
        else:
            print("Start with one topic at a time.")
    else:
        print("Enter a valid percentage.")

def mood():
    m = input("How are you feeling? ").lower()

    if "happy" in m or "good" in m:
        print("That's great! Keep your positive energy!")
    elif "tired" in m:
        print("Take a short break and recharge.")
    elif "stress" in m or "sad" in m:
        print("Take things one step at a time.")
    else:
        print("Thanks for sharing. Take care!")

def about():
    print("\nCtrl + Alt + Rest is a rule-based chatbot.")
    print("It helps students with study planning, motivation,")
    print("productivity and healthy breaks.")

print("=" * 40)
print("      Ctrl + Alt + Rest")
print("     Rule-Based AI Chatbot")
print("=" * 40)

name = input("Enter your name: ").strip() or "User"
subject = input("Favourite subject: ").strip() or "Computer Science"

print("\nHello", name + "!")
print("Your favourite subject is", subject + ".")
print("Type 'help' for commands.")

while True:
    message = input("\nYou: ").lower().strip()

    if message in ["exit", "quit", "bye"]:
        print("Goodbye", name + "!")
        print("Keep learning", subject + ".")
        break

    elif message in ["hi", "hello", "hey"]:
        print("Hello", name + "! Hope your study is going well.")

    elif "stress" in message:
        print("Take one topic at a time.")
        print("Type 'break' if you need rest.")

    elif "tired" in message or "sleepy" in message:
        print("Take some rest, drink water and come back refreshed.")

    elif "good" in message or "happy" in message:
        print("That's great! Keep up the good work!")

    elif message in ["plan", "study plan"]:
        study_plan()

    elif message == "break":
        take_break()

    elif message in ["motivate", "motivation"]:
        motivate()

    elif message == "challenge":
        challenge()

    elif message == "streak":
        streak()

    elif message == "tip":
        tip()

    elif message == "focus":
        focus()

    elif message == "progress":
        progress()

    elif message == "mood":
        mood()

    elif message == "about":
        about()

    elif message in ["help", "commands"]:
        show_help()

    else:
        print("I didn't understand that.")
        print("Type 'help' for available commands.")