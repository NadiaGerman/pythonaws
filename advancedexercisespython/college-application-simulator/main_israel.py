# Israeli College Application Simulator

def evaluate_application(bagrut, psychometric):
    if bagrut >= 85 and psychometric >= 620:
        return "Congratulations! You have been accepted to the university."
    else:
        return "Sorry, your scores do not meet the requirements for admission."

try:
    bagrut = float(input("Enter your Bagrut average (out of 100): "))
    psychometric = int(input("Enter your Psychometric score (out of 800): "))

    result = evaluate_application(bagrut, psychometric)
    print(result)

except ValueError:
    print("Please enter valid numeric scores for Bagrut and Psychometric.")
