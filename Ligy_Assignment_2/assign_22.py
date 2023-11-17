def filter_marks(marks):
    new_dict = {subject: mark for subject, mark in marks.items() if mark > 50}
    return new_dict

# Given dictionary
marks = {'English': 40, 'Maths': 60, 'Hindi': 30, 'Chemistry': 46, 'Physics': 70}

# Create and display the new dictionary with subjects having marks more than 50
filtered_marks = filter_marks(marks)
print("Original Dictionary:", marks)
print("Filtered Dictionary:", filtered_marks)