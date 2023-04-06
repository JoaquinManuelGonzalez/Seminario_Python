names = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 
'Nicolás',  'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
grades_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 
           12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 
           85, 73, 37, 42, 95, 18, 7,     74, 60, 9, 65, 93, 63, 74]
grades_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
           64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
           95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def creation(name, grades_1, grades_2):
    """This function receives a string of names and two lists of marks andcreates 
    and returns a dictionary called "students" whit the information of the students 
    names and the group of grades of each one."""

    grades_group = zip(names.split(","), grades_1, grades_2)
    students = {name: (mark1, mark2) for name, mark1, mark2 in grades_group}
    return students

def average_student(students):
    """This function receives the dictionary before created, makes and returns 
    a new one called "average_per_student" with the name of each student and the 
    average of their grades."""

    average_per_student = dict()
    for elem in students:
        average_per_student[elem] = sum(students[elem]) / len(students[elem]) if (len(students[elem]) > 0) else 0
    return average_per_student

def average_class(average_per_student):
    """This function receives the average of each student, calculates and return 
    the general average of the class."""

    return sum(average_per_student.values()) / len(average_per_student) if (len(average_per_student) > 0) else 0

def max_student(average_per_student):
    """This function receives the average notes of each student and returns the 
    name of the student with the highest average."""

    return max(average_per_student.items(), key=lambda student: student[1])[0]

def min_student(students):
    """This function receives the group of marks of each student and returns the 
    name of the student with the lowest grade."""

    return min(average_per_student.items(), key=lambda student: student[1])[0]

names = names.replace("\n", "")
students = creation(names, grades_1, grades_2)
average_per_student = average_student(students)
class_average = average_class(average_per_student)
max_average = max_student(average_per_student)
min_mark = min_student(students)
print(f'The class average is: {round(class_average, 2)}')
print(f"The studient with the highest average is: {max_average} with average: {average_per_student.get(max_average)}")
print(f"The studient with the lowest grade is: {min_mark} with the mark: {min(students.get(min_mark))}")

