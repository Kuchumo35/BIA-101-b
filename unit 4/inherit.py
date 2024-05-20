class Person:
    def __init__(self, name, age, cid):
        self.name = name
        self.age = age
        self.cid = cid

    def walk(self):
        print(self.name, "is walking")

    def talk(self):
        print(self.name, "is talking")

    def sleep(self):
        print(self.name, "is sleeping")

    def eat(self):
        print(self.name, "is eating")

class Teacher(Person):
    def __init__(self, name, age, cid, subject, salary, department, designation):
        super().__init__(name, age, cid)

        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(self.name, "is teaching")

    def grade_students(self):
        print(self.name, "is grading")

    def attend_meeting(self):
        print(self.name, "is attending meeting")

class Student(Person):
    def __init__(self, name, age, cid, std_id, course, year, gpa):
        super().__init__(name, age, cid)

        self.std_id = std_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(self.name, "is studing")

    def attend_class(self):
        print(self.name, "is attending class")

    def write_exam(self):
        print(self.name, "is writing exam")



t1 = Teacher("tashi", 23, 12345, "math", 30000, "commerce", "assistant")
t2 = Teacher("dorji", 33, 12745, "acc", 50000, "science", "full teacher")

s1 = Student("pema", 17, 1234, 11, "bbi", 2024, 9)
s2 = Student("karma", 19, 1274, 12, "ba", 2023, 8)

if s1.gpa > s2.gpa:
    print(s1.name, "is better than", s2.name)
    student_information = "year: ", + s1.year + "course: " + s1.course
    print(student_information)

else:
    print(s2.name, "is better than", s1.name)
    student_information = "year: ", + str(s2.year) + "course: " + s2.course
    print(student_information)




