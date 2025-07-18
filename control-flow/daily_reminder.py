task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()


match priority:
    case "high":
        priority_text = "high priority task"
    case "medium":
        priority_text = "medium priority task"
    case "low":
        priority_text = "low priority task"
    case _:
        priority_text = "task with an unknown priority level"


if time_bound == "yes":
    print(f"\nReminder: '{task}' is a {priority_text} that requires immediate attention today!")
else:
    print(f"\nNote: '{task}' is a {priority_text}. Consider completing it when you have free time.")