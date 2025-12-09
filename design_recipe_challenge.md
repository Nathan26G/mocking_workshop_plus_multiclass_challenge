# Multi-Class Planned Design Recipe: Coach & Student Management

## 1. Describe the Problem

As a **Coach**, I want to manage a class by being able to:
1.  **Add** new **Student** objects to my class.
2.  Get a **total count** of all challenge **submissions** made by all students in my class.
3.  **Print a formatted list** of all the student names.
4.  **Upload a new submission** for every student in the class simultaneously.

As a **Student**, I need to be able to:
1.  **Add** a new **submission**.
2.  **Report** my personal **count** of submissions.

---

## 2. Design the Class System

The `Coach` class **has a list of** `Student` objects (composition/aggregation), where the `Coach` delegates the submission counting and submission adding tasks to the `Student` objects.

```
┌─────────────────────────────────────────────────┐
│ Coach(name)                                     │
│                                                 │
│ - self.name                                     │
│ - self.students                                 │
│ - add_student(student)                          │
│ - count_submissions()                           │
│   => total submission count                     │
│ - print_student_names()                         │
│   => "Xiao, Rodrigo, Janna"                     │
│ - upload_submission_for_students('tdd-a-class') │
└───────────┬─────────────────────────────────────┘
            │
            │ owns a list of
            ▼
┌────────────────────────────┐
│ Student(name)              │
│                            │
│ - self.name                │
│ - self.submissions         │
│ - add_submission(sub)      │
│ - count_submissions()      │
│   => count of submissions  │
└────────────────────────────┘
```
```python
class Student:
    # User-facing properties:
    #   name: string
    #   submissions: list of strings (submission names)

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Returns:
        #   None
        # Side-effects:
        #   None
        # Notes:
        #   Sets the name property and initializes submissions to an empty list
        pass

    def add_submission(self, submission):
        # Parameters:
        #   submission: string (name of the assignment/challenge)
        # Returns:
        #   None
        # Side-effects:
        #   Adds the submission to the submissions list
        # Nones:
        #   None
        pass

    def count_submissions(self):
        # Parameters:
        #   None
        # Returns:
        #   The integer count of all submissions made by the student.
        # Side-effects:
        #   None
        # Notes:
        #   None
        pass

class Coach:
    # User-facing properties:
    #   name: string
    #   students: list of instances of Student

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Returns:
        #   None
        # Side-effects:
        #   None
        # Notes:
        #   Sets the name property and initializes students to an empty list
        pass

    def add_student(self, student):
        # Parameters:
        #   student: an instance of Student
        # Returns:
        #   None
        # Side-effects:
        #   Adds the student to the students property
        # Notes:
        #   None
        pass

    def count_submissions(self):
        # Parameters:
        #   None
        # Returns:
        #   The integer sum of submissions from all students the coach manages. (Delegation)
        # Side-effects:
        #   None
        # Notes:
        #   None
        pass

    def print_student_names(self):
        # Parameters:
        #    None
        # Returns:
        #   A string of all student names, separated by ", "
        # Side-effects:
        #   None
        # Notes:
        #   None
        pass
    
    def upload_submission_for_students(self, submission):
        # Parameters:
        #   submission: string (name of the assignment/challenge)
        # Returns:
        #   None
        # Side-effects:
        #   Calls student.add_submission(submission) on every student the coach manages. (Delegation)
        # Notes:
        #   None
        pass
```
## 3. Test Examples
```python

test_student.py

def test_return_empty_list_after_being_initialised():
  #initalise the class
  #then return the list
  #assert that list is empty 

def test_return_list_after_adding_a_submission():
  #initalise the class
  # add a submission 
  #then return the list
  #assert that list has submission

def test_return_list_after_adding_multiple_submissios():
  #initalise the class
  # add multiple submissions 
  #then return the list
  #assert that list has submissions

def test_return_count_before_submissions():
  # initalise the class
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_a_submission():
  # initalise the class
  # add a submission 
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_multiple_submissios():
  # initalise the class
  # add multiple submissions 
  # run the count_submission func
  # assert that count is correct


test_coach.py

def test_return_empty_list_after_being_initialised():
    #initalise the class
    #then return the student list
    #assert that list is empty 

def test_return_list_len_after_adding_a_student():
  #initalise the class
  # add a student 
  #then return the len of student list
  #assert that list len is 1

def test_return_list_len_after_adding_multiple_students():
  #initalise the class
  # add multiple students 
  #then return the len of student list
  #assert that list len has amount students

def test_return_count_without_students():
  # initalise the class
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_a_student_with_no_submissions():
  # initalise the class
  # add a student (without submisions)
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_a_student():
  # initalise the class
  # add a student (with submisions)
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_multiple_students():
  # initalise the class
  # add multiple students (with submisionss)
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_a_student_with_multiple_submissions():
  # initalise the class
  # add a student (with submisions)
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_multiple_students_with_multiple_submissions():
  # initalise the class
  # add multiple students (with submisionss)
  # run the count_submission func
  # assert that count is correct


def test_returns_student_name_as_a_string():
    # initalise the class
    # add one student
    # run the print_student_names func
    # assert the string is returned correctly

def test_returns_students_names_as_a_string():
    # initalise the class
    # add multiple students
    # run the print_student_names func
    # assert the string is returned correctly

def test_returns_error_message_when_no_students():
    # initalise the class
    # run the print_student_names func
    # assert the error message is returned correctly

test_intergration_student_coach.py

def test_return_count_after_adding_a_student_with_no_submissions():
  # initalise the class
  # add a student (without submisions)
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_a_student():
  # initalise the class
  # add a student (with submisions)
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_multiple_students():
  # initalise the class
  # add multiple students (with submisionss)
  # run the count_submission func
  # assert that count is correct

def test_return_count_after_adding_a_student_with_multiple_submissions():
  # initalise the class
  # add a student (with submisions)
  # run the count_submission func
  # assert that count is correct

def test_return_empty_submission_list_of_student():
  # return the submission lists, combined of all students
  # assert that list is empty 

def test_return_submission_list_of_student_after_adding_a_submission():
  # add a submission to the students lists
  # return the submission lists, combined of all students
  # assert that list has the submission

def test_return_submission_list_of_student_after_adding_multiple_submissions():
  # add multiple submissions to a students lists
  # return the submission lists, combined of all students
  # assert that list has the submissions 
```