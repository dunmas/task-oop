class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_rate = 0

    def __str__(self):
        courses_in_progress = ""
        finished_courses = ""

        # Делаем красивые списки курсов в одну строку
        for pos, course in enumerate(self.courses_in_progress):
            courses_in_progress += course

            if pos != len(self.courses_in_progress) - 1:
                courses_in_progress += ", "

        for pos, course in enumerate(self.finished_courses):
            finished_courses += course

            if pos != len(self.finished_courses) - 1:
                finished_courses += ", "

        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка: {self.avg_rate}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}\n")

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate > other.avg_rate
        else:
            return "Ошибка"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_rate == other.avg_rate
        else:
            return "Ошибка"

    def calculate_avg_rate(self):
        grades_count = 0
        grades_sum = 0

        for course in self.grades:
            grades_count += len(self.grades[course])
            grades_sum += sum(self.grades[course])

        self.avg_rate = round(grades_sum / grades_count, 2)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and \
                course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

            lecturer.calculate_avg_rate()
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        self.avg_rate = 0
        
        super().__init__(name, surname)

    def __str__(self):
        super().__str__()
        return f"{super().__str__()}" \
               f"Средняя оценка: {self.avg_rate}\n"\


    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate > other.avg_rate
        else:
            return "Ошибка"

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate == other.avg_rate
        else:
            return "Ошибка"

    def calculate_avg_rate(self):
        grades_count = 0
        grades_sum = 0

        for course in self.grades:
            grades_count += len(self.grades[course])
            grades_sum += sum(self.grades[course])

        self.avg_rate = round(grades_sum / grades_count, 2)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

            student.calculate_avg_rate()
        else:
            return 'Ошибка'


def calc_avg_course_rate_stud(students_list, course):
    grades_sum = 0
    grades_count = 0

    for student in students_list:
        grades_count += len(student.grades[course])
        grades_count += sum(student.grades[course])


def calc_avg_course_rate_lect(lecturers_list, course):
    grades_sum = 0
    grades_count = 0

    for lecturer in lecturers_list:
        grades_count += len(lecturer.grades[course])
        grades_count += sum(lecturer.grades[course])

# ------- начало тестов -------


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Delphi']
student_1.courses_in_progress += ['Git']

student_2 = Student('Dan', 'Pustovgar', 'male')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Git']
student_2.finished_courses += ['C++']

students_list = [student_1, student_2]

mentor_1 = Reviewer('Some', 'Buddy')
mentor_1.courses_attached += ['Python']

mentor_2 = Reviewer('Once', 'Toldme')
mentor_2.courses_attached += ['Git']
mentor_2.courses_attached += ['Python']

lecturer_1 = Lecturer('Vova', 'Vovin')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Peter', 'Parker')
lecturer_2.courses_attached += ['Python']

lecturers_list = [lecturer_1, lecturer_2]

mentor_1.rate_hw(student_2, 'Python', 9)
mentor_1.rate_hw(student_2, 'Python', 8)
mentor_2.rate_hw(student_1, 'Git', 7)
mentor_2.rate_hw(student_1, 'Python', 8)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 5)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 6)

print(student_2)
print(student_1)
print(mentor_1)
print(lecturer_1)
print(lecturer_2)
print('--------------')

if student_1 < student_2:
    print("stud_1_lt_2")
elif student_1 > student_2:
    print("stud_1_gt_2")
else:
    print("stud_eq")

if lecturer_1 < lecturer_2:
    print("lec_1_lt_2")
elif lecturer_1 > lecturer_2:
    print("lec_1_gt_2")
else:
    print("lec_eq")

