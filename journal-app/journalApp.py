date = input("Enter today's date: ")
mood = input("Please rate your mood from 1 to 10: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"journal-app/journal-files/journal.txt{date}.txt", 'w') as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)