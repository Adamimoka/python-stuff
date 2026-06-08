"""
Solve the clock puzzle: given any time in the format "HH:MM",
can a true mathematical statement be made using basic operations?
Which times do and don't have true statements?
"""
possible_operations = ["+", "-", "*", "/", "**"]

def is_correct(statement):
    """
    Check if the given statement is correct by evaluating both sides of the equation.
    """
    try:
        p1, p2 = statement.split("==")
        return eval(p1) == eval(p2)
    except ZeroDivisionError:
        return False

def validate_statements(statements):
    """
    Validate and return the correct statements for a given time.
    """
    valid_statements = []
    for statement in statements:
        if is_correct(statement):
            valid_statements.append(statement)
    return valid_statements

def generate_times(possible_hours, possible_minutes):
    """
    Generate all possible times in the format "HH:MM" using the provided possible hours and minutes.
    """
    times = []
    for hour in possible_hours:
        for minute in possible_minutes:
            times.append(f"{hour}:{minute}")
    return times

def generate_statements(time):
    """
    Generate all possible statements for a given time by inserting operations and equality signs in different positions.
    """
    statements = []

    hour, minute = time.split(":")
    hr1 = hour[0]
    hr2 = hour[1]
    min1 = minute[0]
    min2 = minute[1]
    for eq_placement in [0, 1, 2]:
        for op1 in possible_operations:
            for op2 in possible_operations:
                if eq_placement == 0:
                    statement = f"{hr1}=={hr2}{op1}{min1}{op2}{min2}"
                elif eq_placement == 1:
                    statement = f"{hr1}{op1}{hr2}=={min1}{op2}{min2}"
                else:
                    statement = f"{hr1}{op1}{hr2}{op2}{min1}=={min2}"
                statements.append(statement)

    return statements


def main():
    possible_hours_ints = list(range(1, 13))
    possible_minutes_ints = list(range(0, 60))
    possible_hours = [f"{hour:02d}" for hour in possible_hours_ints]
    possible_minutes = [f"{minute:02d}" for minute in possible_minutes_ints]

    results = {}

    times = generate_times(possible_hours, possible_minutes)
    total_amount = len(times)
    counter = 0
    for time in times:
        # generate all statements for the given time
        statements = generate_statements(time)
        # validate the statements and save the correct ones
        valid_statements = validate_statements(statements)
        if valid_statements:
            results[time] = valid_statements
        else:
            results[time] = ["No valid statements"]
        
        counter += 1
        percent_done = (counter / total_amount) * 100
        print(f"Finished {time} - {percent_done:.2f}%", end="\r")
    # Save results to file
    print("Saving results to file...")
    with open("results.txt", "w") as f:
        for time, valid_statements in results.items():
            f.write(f"{time}: ")
            for statement in valid_statements:
                f.write(f"{statement} ")
            f.write("\n")
    print("Done. Saved to results.txt")
    
    print("-"*20)
    print("Summary:")
    print(f"Total times: {total_amount}")
    valid_times = sum(1 for statements in results.values() if statements != ["No valid statements"])
    print(f"Times with valid statements: {valid_times}")
    print(f"Percent of times with valid statements: {100 * valid_times / total_amount}%")

if __name__ == "__main__":
    main()