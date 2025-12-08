from lib.student import Student

class Coach:
    def __init__(self, name):
        self.name = name
        self.list_of_students = []
        self.list_of_student_submissions = []
        
    def add_student(self, student):
        student = Student(student)
        self.list_of_students.append(student.name)
    
    def count_submissions(self):
        for student in self.list_of_students:
            for submission in student.list_of_submissions:
              self.list_of_student_submissions.append(submission)
        return len(self.list_of_student_submissions)
      
    def print_student_names(self):
        if len(self.list_of_students) == 1:
            return self.list_of_students[0]
        if len(self.list_of_students) > 1:
            return ', '.join(self.list_of_students)
        return 'No students'