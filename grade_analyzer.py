def process_scores(students):
    """
    Task 1:
    Accepts a dictionary {name: [scores]} and returns {name: average_score}
    where average_score is rounded to 2 decimal places.
    """
    averages = {}

    for name, scores in students.items():
        if not scores:  # handle empty list safely
            avg = 0.0
        else:
            avg = sum(scores) / len(scores)

        averages[name] = round(avg, 2)

    return averages


def classify_grades(averages):
    """
    Task 2:
    Accepts {name: average_score} and returns {name: (average, grade)}.
    Grading thresholds are defined INSIDE this function (no globals).
    """
    A_MIN = 90
    B_MIN = 75
    C_MIN = 60

    classified = {}

    for name, avg in averages.items():
        if avg >= A_MIN:
            grade = "A"
        elif avg >= B_MIN:
            grade = "B"
        elif avg >= C_MIN:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


def generate_report(classified, passing_avg=70):
    """
    Task 3:
    Prints a formatted report and returns the total number of students who passed.
    PASS/FAIL is based on passing_avg (default 70).
    """
    print("===== Student Grade Report =====")

    total_students = len(classified)
    passed = 0

    # Print students in alphabetical order for neatness
    for name in sorted(classified.keys()):
        avg, grade = classified[name]
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1

        # Formatting similar to sample
        print(f"{name:<9} | Avg: {avg:>6.2f} | Grade: {grade} | Status: {status}")

    failed = total_students - passed

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


if __name__ == "__main__":
    # Sample data (replace with your actual classroom data)
    students = {
        "Alice": [85, 90, 80, 90],
        "Bob": [60, 65, 55, 70],
        "Clara": [95, 98, 96, 96]
    }

    # Call all three functions in sequence
    averages = process_scores(students)
    classified = classify_grades(averages)
    passed_count = generate_report(classified)  # passing_avg defaults to 70