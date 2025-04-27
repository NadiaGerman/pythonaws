# College Application Simulator
# This script simulates a college application process and determines acceptance based on GPA and SAT score.

def evaluate_application(gpa, sat_score):
    # Accept if GPA(Grade Point Average) is at least 3.0 AND SAT(Scholastic Assessment Test) is at least 1200
    if gpa >= 3.0 and sat_score >= 1200:
        return "Congratulations! You have been accepted."
    else:
        return "We regret to inform you that you were not accepted."

# Ask user for GPA and SAT score
try:
    gpa = float(input("Enter your GPA (on a 4.0 scale): "))
    sat_score = int(input("Enter your SAT score (out of 1600): "))

    result = evaluate_application(gpa, sat_score)
    print(result)

except ValueError:
    print("Please enter valid numbers for GPA and SAT.")
