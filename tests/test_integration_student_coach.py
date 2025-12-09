from lib.student import Student
from lib.coach import Coach

def test_return_count_after_adding_a_student_with_no_submissions():
      coach = Coach('Nathan')
      student = Student('Fergus')
      coach.list_of_student_submissions += student.list_of_submissions
      count = coach.count_submissions()
       
      assert count == 0

def test_return_count_after_adding_a_student():
      coach = Coach('Nathan')
      student = Student('Fergus')
      student.add_submission('submission')
      coach.list_of_student_submissions += student.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 1
     
def test_return_count_after_adding_multiple_students():
      coach = Coach('Nathan')
      student = Student('Fergus')
      student2 = Student('Craig')
      student.add_submission('submission')
      student2.add_submission('submission')
      coach.list_of_student_submissions += student.list_of_submissions
      coach.list_of_student_submissions += student2.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 2
      
def test_return_count_after_adding_a_student_with_multiple_submissions():
      coach = Coach('Nathan')
      student = Student('Fergus')
      student.add_submission('submission')
      student.add_submission('submission2')
      coach.list_of_student_submissions += student.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 2
      
def test_return_count_after_adding_multiple_students_with_multiple_submissions():
      coach = Coach('Nathan')
      student = Student('Fergus')
      student2 = Student('Craig')
      student.add_submission('submission')
      student.add_submission('submission2')
      student2.add_submission('submission')
      student2.add_submission('submission2')
      coach.list_of_student_submissions += student.list_of_submissions
      coach.list_of_student_submissions += student2.list_of_submissions
      count = coach.count_submissions()
      
      assert count == 4
      
def test_return_empty_submission_list_of_student():
    coach = Coach('Nathan')
    Fergus = Student('Fergus')
    coach.add_student(Fergus)
    list = Fergus.list_of_submissions
    
    assert list == []
    
def test_return_submission_list_of_student_after_adding_a_submission():
    coach = Coach('Nathan')
    Fergus = Student('Fergus')
    coach.add_student(Fergus)
    coach.upload_submission_for_students('submission')
    list = Fergus.list_of_submissions
    
    assert coach.list_of_students == ['submission'] 