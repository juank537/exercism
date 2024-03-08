"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    # Solution with list comprehension
    # return [round(x) for x in student_scores]

    for index, number in enumerate(student_scores):
        student_scores[index] = round(number)
    return student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    # Solution with list comprehension
    # return len([x for x in student_scores if x <= 40])
    
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count



def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    # Solution with list comprehension
    # return len([x for x in student_scores if x >= threshold])

    list_over = []
    for score in student_scores:
        if score >= threshold:
            list_over.append(score)
    return list_over


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    scores = []
     # se calcula la diferencia entre el máximo y el mínimo, luego se divide en 4 grupos iguales y se redondea el valor
    jump = round((highest - 40)/4)
    for value in range(41, highest, jump):
        scores.append(value)
    return scores


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    new_list = [] 
    for index, value in enumerate(student_scores):
        new_list.insert(index, f"{index + 1}. {student_names[index]}: {value}" ) 
    return new_list



def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        if student[1] == 100:
            return student
    return []

# print(round_scores([90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
# print(count_failed_students([90.33, 40, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]))
# print(above_threshold([90,40,55,70,30,68,70,75,83,96], 75))

# print(letter_grades(100))

# student_scores = [100, 99, 90, 84, 66, 53, 47]
# student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
# print(student_ranking(student_scores, student_names))

print(perfect_score([["Charles", 90], ["Tony", 80], ["Alex", 100]]))