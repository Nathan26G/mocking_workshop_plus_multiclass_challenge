class Student:
    def __init__(self, name):
        self.name = name
        self.list_of_submissions = []
    def add_submission(self, submission):
        self.list_of_submissions.append(submission)
    def count_submissions(self):
        return len(self.list_of_submissions)