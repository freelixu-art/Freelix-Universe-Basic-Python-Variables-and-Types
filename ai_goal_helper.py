import datetime

def run_student_helper():
    print("Welcome to the AI Goal Achievement Help Center!")
    print("I'm here to assist students in finding solutions and achieving their goals. Let's get started.")

    while True:
        print("\nMain Menu:")
        print("1. Academic Guidance")
        print("2. Career Advice")
        print("3. Time Management Tips")
        print("4. Personal Development")
        print("5. Exit")

        choice = input("\nEnter the number of the option you'd like help with: ")

        if choice == '1':
            print("\nAcademic Guidance:")
            print("1. Study Smarter: Identify your study goals and break them into manageable chunks.")
            print("2. Stay Consistent: Build a study schedule and stick to it.")
            print("3. Use Resources: Don't hesitate to reach out to tutors, mentors, or study forums.")
        elif choice == '2':
            print("\nCareer Advice:")
            print("1. Identify your Passion: Explore what excites you and aligns with your skills.")
            print("2. Gain Experience: Focus on internships, part-time jobs, or volunteer work.")
            print("3. Network: Attend events, seminars, and connect with professionals on LinkedIn.")
        elif choice == '3':
            print("\nTime Management Tips:")
            print("1. Prioritize: Use daily to-do lists and start with high-priority tasks.")
            print("2. Avoid Procrastination: Plan and start working ahead of deadlines.")
            print("3. Use Tools: Use calendars or apps to structure your day.")
        elif choice == '4':
            print("\nPersonal Development:")
            print("1. Read Books: Gain knowledge and improve your mindset.")
            print("2. Set Goals: Define your personal and professional goals.")
            print("3. Stay Healthy: Exercise regularly, eat well, and rest adequately.")
        elif choice == '5':
            print("\nThank you for using the AI Help Center! Have a great day achieving your goals!")
            break
        else:
            print("\nInvalid choice. Please select a number from the menu.")

        log_activity()

def log_activity():
    with open("student_activity_log.txt", "a") as log_file:
        log_file.write(f"User accessed help at {datetime.datetime.now()}\n")

if __name__ == "__main__":
    run_student_helper()