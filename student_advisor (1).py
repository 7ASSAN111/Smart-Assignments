print("=== Student Advisor Agent ===")

try:
    # Inputs
    gpa = float(input("Enter your GPA: "))
    attendance = float(input("Enter your attendance percentage: "))

    # Decision rules
    if gpa >= 3.5 and attendance >= 90:
        decision = "Excellent performance. Keep up the good work!"

    elif gpa >= 3.0 and attendance >= 80:
        decision = "Good performance. Try to improve slightly."

    elif gpa >= 2.5 and attendance >= 70:
        decision = "Average performance. Study more and attend classes."

    elif gpa < 2.5 and attendance >= 70:
        decision = "Your GPA is low. Focus on studying and ask for help."

    elif attendance < 70 and gpa >= 3.0:
        decision = "Your GPA is good but attendance is low. Attend more classes."

    else:
        decision = "Low GPA and low attendance. You must improve both."

    # Output
    print("\nAgent Recommendation:")
    print(decision)

except ValueError:
    print("Please enter valid numeric values!")