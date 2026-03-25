from collections.abc import Iterable, Iterator


class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3


# Iterator pour matière 1
class SchoolClassIterator(Iterator):
    def __init__(self, students):
        self.students = sorted(
            students,
            key=lambda student: student.matter_1,
            reverse=True
        )
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration


# Iterator pour matière 2
class SchoolClassIteratorMatter2(Iterator):
    def __init__(self, students):
        self.students = sorted(
            students,
            key=lambda student: student.matter_2,
            reverse=True
        )
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration


# Iterator pour matière 3
class SchoolClassIteratorMatter3(Iterator):
    def __init__(self, students):
        self.students = sorted(
            students,
            key=lambda student: student.matter_3,
            reverse=True
        )
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    # Iterator par défaut → matière 1
    def __iter__(self):
        return SchoolClassIterator(self.students)

    # Iterator matière 2
    def iter_matter_2(self):
        return SchoolClassIteratorMatter2(self.students)

    # Iterator matière 3
    def iter_matter_3(self):
        return SchoolClassIteratorMatter3(self.students)


if __name__ == "__main__":
    school_class = SchoolClass()
    school_class.add_student(Student('J', 10, 12, 13))
    school_class.add_student(Student('A', 8, 2, 17))
    school_class.add_student(Student('V', 9, 14, 14))

    print("Matière 1 :")
    for student in school_class:
        print(student.name, student.matter_1)

    print()

    print("Matière 2 :")
    for student in school_class.iter_matter_2():
        print(student.name, student.matter_2)

    print()

    print("Matière 3 :")
    for student in school_class.iter_matter_3():
        print(student.name, student.matter_3)