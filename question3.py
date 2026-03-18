# Name: Udbhav Ghimire
# Student ID: s395644

def get_grade(mark):
    """
    Determines the grade category based on the score.
    
    Parameters:
        mark (int): Student's score (0-100)
    
    Returns:
        str: Grade category (HD, D, C, P, or F)
    """
    if mark >= 85:
        return 'HD'
    elif mark >= 75:
        return 'D'
    elif mark >= 65:
        return 'C'
    elif mark >= 50:
        return 'P'
    else:
        return 'F'


def validate_student_count():
    """
    Prompts for and validates the number of students.
    Ensures the input is a positive integer.
    
    Returns:
        int: Valid number of students
    """
    while True:
        try:
            num_students = int(input('How many students? '))
            if num_students <= 0:
                print('Error: Number of students must be positive. Please try again.')
            else:
                return num_students
        except ValueError:
            print('Error: Please enter a valid integer.')


def validate_score(student_name):
    """
    Prompts for and validates a student's score.
    Ensures the score is an integer between 0 and 100.
    
    Parameters:
        student_name (str): Name of the student
    
    Returns:
        int: Valid score (0-100)
    """
    while True:
        try:
            score = int(input(f"{student_name}'s score: "))
            if score < 0 or score > 100:
                print('Error: Score must be between 0 and 100. Please try again.')
            else:
                return score
        except ValueError:
            print('Error: Please enter a valid integer.')


def get_students(number):
    """
    Collects student names and scores with validation.
    
    Parameters:
        number (int): Number of students to collect data for
    
    Returns:
        list: List of tuples containing (name, score) for each student
    """
    students = []
    for n in range(number):
        name = input(f'Student {n + 1} name: ')
        score = validate_score(name)
        students.append((name, score))
    return students


def calculate_statistics(students):
    """
    Calculates comprehensive statistics for all students.
    
    Parameters:
        students (list): List of tuples containing (name, score)
    
    Returns:
        dict: Dictionary containing various statistics
    """
    scores = [student[1] for student in students]
    
    # Calculate basic statistics
    average = sum(scores) / len(scores)
    highest_student = max(students, key=lambda x: x[1])
    lowest_student = min(students, key=lambda x: x[1])
    
    # Calculate grade distribution
    grade_counts = {'HD': 0, 'D': 0, 'C': 0, 'P': 0, 'F': 0}
    for student in students:
        grade = get_grade(student[1])
        grade_counts[grade] += 1
    
    return {
        'average': average,
        'highest': highest_student,
        'lowest': lowest_student,
        'grade_distribution': grade_counts
    }


def display_results(students, stats):
    """
    Displays student results and statistics in a well-formatted manner.
    
    Parameters:
        students (list): List of tuples containing (name, score)
        stats (dict): Dictionary containing calculated statistics
    """
    print('\n' + '=' * 50)
    print('STUDENT RESULTS')
    print('=' * 50)
    
    # Display individual student results
    for student in students:
        name, score = student
        grade = get_grade(score)
        print(f'{name:20s}: {score:3d} ({grade})')
    
    # Display statistics
    print('\n' + '=' * 50)
    print('STATISTICS')
    print('=' * 50)
    print(f'Average score:        {stats["average"]:.2f}')
    print(f'Highest score:        {stats["highest"][0]} ({stats["highest"][1]})')
    print(f'Lowest score:         {stats["lowest"][0]} ({stats["lowest"][1]})')
    
    # Display grade distribution
    print('\n' + '-' * 50)
    print('GRADE DISTRIBUTION')
    print('-' * 50)
    total_students = len(students)
    for grade in ['HD', 'D', 'C', 'P', 'F']:
        count = stats['grade_distribution'][grade]
        percentage = (count / total_students) * 100
        print(f'{grade:2s}: {count:2d} student(s) ({percentage:5.1f}%)')
    print('=' * 50)


def main():
    """
    Main program execution function.
    Coordinates the flow of the grade management system.
    """
    # Validate and get number of students
    num_students = validate_student_count()
    
    # Collect student information with validation
    students = get_students(num_students)
    
    # Calculate all statistics
    statistics = calculate_statistics(students)
    
    # Display formatted results and statistics
    display_results(students, statistics)


# Program entry point
if __name__ == '__main__':
    main()