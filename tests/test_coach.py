from lib.coach import Coach
from unittest.mock import Mock

def test_return_empty_list_after_being_initialised():
    coach = Coach('Nathan')
    student_len = len(coach.list_of_students)
    
    assert student_len == 0

def test_return_list_len_after_adding_a_student():
    coach = Coach('Nathan')
    Doug = Mock()
    Doug.name = 'Doug'
    coach.add_student(Doug)
    student_len = len(coach.list_of_students)
    
    assert student_len == 1
    
def test_return_list_len_after_adding_multiple_students():
    coach = Coach('Nathan')
    Doug = Mock()
    Doug.name = 'Doug'
    coach.add_student(Doug)
    Desmond = Mock()
    Desmond.name = 'Desmond'
    coach.add_student(Desmond)
    student_len = len(coach.list_of_students)
    
    assert student_len == 2

def test_return_count_without_students():
       coach = Coach('Nathan')
       count = coach.count_submissions()
       
       assert count == 0

def test_return_count_after_adding_a_student_with_no_submissions():
      coach = Coach('Nathan')
      mock_student = Mock()
      mock_student.list_of_submissions = []
      coach.list_of_student_submissions += mock_student.list_of_submissions
      count = coach.count_submissions()
       
      assert count == 0

def test_return_count_after_adding_a_student():
      coach = Coach('Nathan')
      mock_student = Mock()
      mock_student.list_of_submissions = ['submission']
      coach.list_of_student_submissions += mock_student.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 1
      
def test_return_count_after_adding_multiple_students():
      coach = Coach('Nathan')
      mock_student = Mock()
      mock_student.list_of_submissions = ['submission']
      mock_student2 = Mock()
      mock_student2.list_of_submissions = ['submission']
      coach.list_of_student_submissions += mock_student.list_of_submissions
      coach.list_of_student_submissions += mock_student2.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 2
      
def test_return_count_after_adding_a_student_with_multiple_submissions():
      coach = Coach('Nathan')
      mock_student = Mock()
      mock_student.list_of_submissions = ['submission1', 'submission2']
      coach.list_of_student_submissions += mock_student.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 2
      
def test_return_count_after_adding_multiple_students_with_multiple_submissions():
      coach = Coach('Nathan')
      mock_student = Mock()
      mock_student.list_of_submissions = ['submission1', 'submission2']
      mock_student2 = Mock()
      mock_student2.list_of_submissions = ['submission1', 'submission2']
      coach.list_of_student_submissions += mock_student.list_of_submissions
      coach.list_of_student_submissions += mock_student2.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 4
      
def test_returns_student_name_as_a_string():
    coach = Coach('Nathan')
    Doug = Mock()
    Doug.name = 'Doug'
    coach.add_student(Doug)
    student_string = coach.print_student_names()
    
    assert student_string == 'Doug'

def test_returns_students_names_as_a_string():
  
    coach = Coach('Nathan')
    Doug = Mock()
    Doug.name = 'Doug'
    coach.add_student(Doug)
    Desmond = Mock()
    Desmond.name = 'Desmond'
    coach.add_student(Desmond)
    student_string = coach.print_student_names()
    
    assert student_string == 'Doug, Desmond'
    
def test_returns_error_message_when_no_students():
    coach = Coach('Nathan')
    student_string = coach.print_student_names()
    
    assert student_string == 'No students'
    
# I couldn't think of a way of checking the upload_submission_for_students function using mock