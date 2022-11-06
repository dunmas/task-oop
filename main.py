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
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        
        super().__init__(self, name, surname)


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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student)

