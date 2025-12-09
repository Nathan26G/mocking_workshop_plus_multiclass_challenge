from lib.student import Student

class Coach:
    def __init__(self, name):
        self.name = name
        self.list_of_students = []
        self.list_of_student_submissions = []
        
    def add_student(self, student):
        self.list_of_students.append(student)
    
    def count_submissions(self):
        for student in self.list_of_students:
            for submission in student.list_of_submissions:
              self.list_of_student_submissions.append(submission)
        return len(self.list_of_student_submissions)
      
    def print_student_names(self):
        if len(self.list_of_students) > 0:
            list_of_students_names = []
            for student in self.list_of_students:
              list_of_students_names.append(student.name)
            return ', '.join(list_of_students_names)
        return 'No students'

    def upload_submission_for_students(self, submission):
        for student in self.list_of_students:
            student.add_submission(submission)