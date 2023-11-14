class Student:
    student_list = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # пройденные курсы
        self.courses_in_progress = []  # курсы в процессе изучения
        self.grades = {}  # словарь оценки
        Student.student_list.append(self)

    # Студенты ставят оценки лекторам за провденеие лекции
    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def grades_average(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('ошибка')
            return
        return self.grades_average() < other.grades_average()

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {(self.grades_average())}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    lecturer_list = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # словарь оценкой за лекции
        Lecturer.lecturer_list.append(self)

    def grades_average(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades:
            grades_count += len(self.grades[grade])
            grades_sum += sum(self.grades[grade])
        if grades_count > 0:
            return grades_sum / grades_count
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('ошибка')
            return
        return self.grades_average() < other.grades_average()

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {(self.grades_average())}\n")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Выставление оценок за домашную работу студентам
    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


def courses_average_students(student_list, course):
    for student in student_list:
        for cours_name, average in student.grades.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Студент: {student.name} {student.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Cредняя оценка за домашние задания: {(sum_average)}\n")


def courses_average_lecturer(lecturer_list, course):
    for lecturer in lecturer_list:
        for cours_name, average in lecturer.grades.items():
            if course == cours_name:
                sum_average = sum(average) / len(average)
                print(f"Лектор: {lecturer.name} {lecturer.surname}\n"
                      f"Курс: {cours_name}\n"
                      f"Cредняя оценка по лекциям: {(sum_average)}\n")


student_1 = Student('Иван', 'Сафронов', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['GIT']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Петр', 'Сергеев', 'your_gender')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['GIT']
student_2.finished_courses += ['Введение в программирование']

mentor_reviewer_1 = Reviewer('Василий', 'Фальковский')
mentor_reviewer_1.courses_attached += ['Python']
mentor_reviewer_1.courses_attached += ['Git']

mentor_reviewer_2 = Reviewer('Евгений', 'Милославский')
mentor_reviewer_2.courses_attached += ['Python']
mentor_reviewer_2.courses_attached += ['Git']

mentor_reviewer_1.rate_hw_student(student_1, 'Python', 10)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 8)
mentor_reviewer_1.rate_hw_student(student_1, 'Python', 6)
mentor_reviewer_1.rate_hw_student(student_1, 'Git', 7)

mentor_reviewer_2.rate_hw_student(student_2, 'Python', 5)
mentor_reviewer_2.rate_hw_student(student_2, 'Python', 3)
mentor_reviewer_2.rate_hw_student(student_2, 'Python', 7)
mentor_reviewer_2.rate_hw_student(student_2, 'Git', 6)

mentor_lecturer_1 = Lecturer('Бориc', 'Молчанин')
mentor_lecturer_1.courses_attached += ['Python']
mentor_lecturer_1.courses_attached += ['Git']

mentor_lecturer_2 = Lecturer('Владимир', 'Вливанов')
mentor_lecturer_2.courses_attached += ['Python']
mentor_lecturer_2.courses_attached += ['Git']

student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Python', 7)
student_1.rate_hw_lecturer(mentor_lecturer_1, 'Git', 8)

student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Python', 7)
student_2.rate_hw_lecturer(mentor_lecturer_2, 'Git', 8)

mentor_reviewer_1 = Reviewer('Арсений', 'Полещук')
mentor_reviewer_1.courses_attached += ['Python']
mentor_reviewer_1.courses_attached += ['Git']

mentor_reviewer_2 = Reviewer('Владлен', 'Жубарев')
mentor_reviewer_2.courses_attached += ['Python']
mentor_reviewer_2.courses_attached += ['Git']

print(mentor_reviewer_1)
print(mentor_reviewer_2)
print(mentor_lecturer_1)
print(mentor_lecturer_2)
print(student_1)
print(student_2)

if student_1 > student_2:
    print(f'Студент {student_1.name}а {student_1.surname} учится лучше, чем {student_2.name}а {student_2.surname}')
elif student_1 < student_2:
    print(f'тудент {student_1.name}а {student_1.surname} учится хуже, чем {student_2.name}а {student_2.surname}')
else:
    print(f'тудент {student_1.name}а {student_1.surname}  учится так же как {student_2.name}а {student_2.surname}')

if mentor_lecturer_1 > mentor_lecturer_2:
    print(
        f'Лектор {mentor_lecturer_1.name}а {mentor_lecturer_1.surname} преподатет лучше, чем {mentor_lecturer_2.name} {mentor_lecturer_2.surname}а')
elif mentor_lecturer_1 < mentor_lecturer_2:
    print(
        f'Лектор {mentor_lecturer_1.name}а {mentor_lecturer_1.surname} преподает уже, чем  {mentor_lecturer_2.name} {mentor_lecturer_2.surname}а')
else:
    print(
        f'Лектор {mentor_lecturer_1.name}а {mentor_lecturer_1.surname} преподает так же как {mentor_lecturer_2.name} {mentor_lecturer_2.surname}а')
print()

print(f'Оценки студента {student_1.name} {student_1.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in student_1.grades.items()])
print(f'Оценки студента {student_2.name} {student_2.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in student_2.grades.items()])

print(f'Оценки лектора {mentor_lecturer_1.name} {mentor_lecturer_1.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in mentor_lecturer_1.grades.items()])
print(f'Оценки лектора {mentor_lecturer_2.name} {mentor_lecturer_2.surname}: ',
      *[f"{key}: {', '.join(map(str, value))}" for key, value in mentor_lecturer_2.grades.items()])
print()

courses_average_students(Student.student_list, 'Python')
courses_average_lecturer(Lecturer.lecturer_list, 'Python')

