from collections.abc import Iterable, Iterator

def add_matter_4(cls):
    original_init = cls.__init__

    def new_init(self, name, matter_1, matter_2, matter_3, matter_4=0):
        original_init(self, name, matter_1, matter_2, matter_3)
        self.matter_4 = matter_4

    cls.__init__ = new_init
    return cls

def add_iter_matter_4(cls):
    def iter_matter_4(self):
        return SchoolClassIteratorMatter4(self.students)

    cls.iter_matter_4 = iter_matter_4
    return cls

@add_matter_4
class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3

class SchoolClassIterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_1, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration

class SchoolClassIteratorMatter2(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_2, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration

class SchoolClassIteratorMatter3(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_3, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration

class SchoolClassIteratorMatter4(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda s: s.matter_4, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index < len(self.students):
            student = self.students[self.index]
            self.index += 1
            return student
        raise StopIteration

@add_iter_matter_4
class SchoolClass(Iterable):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "students"):
            self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return SchoolClassIterator(self.students)

    def iter_matter_2(self):
        return SchoolClassIteratorMatter2(self.students)

    def iter_matter_3(self):
        return SchoolClassIteratorMatter3(self.students)

if __name__ == "__main__":
    school_class = SchoolClass()
    school_class_2 = SchoolClass()

    school_class.add_student(Student('J', 10, 12, 13, 15))
    school_class.add_student(Student('A', 8, 2, 17, 9))
    school_class.add_student(Student('V', 9, 14, 14, 11))

    print(school_class is school_class_2)

    for student in school_class:
        print(student.name, student.matter_1)

    for student in school_class.iter_matter_2():
        print(student.name, student.matter_2)

    for student in school_class.iter_matter_3():
        print(student.name, student.matter_3)

    for student in school_class.iter_matter_4():
        print(student.name, student.matter_4)