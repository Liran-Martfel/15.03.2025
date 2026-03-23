grades = {"Tom":80, "Anna":95, "John":70, "Sara":85}

# 82.5


def get_average_grade(grades: dict) -> float:
    '''

    :param grades: {<name>: <grade>}
    :return: average grade of all students
    '''
    return sum(grades.values()) / len(grades)

print(get_average_grade(grades))