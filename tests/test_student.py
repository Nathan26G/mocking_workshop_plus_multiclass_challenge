from lib.student import Student

def test_return_empty_list_after_being_initialised():
    student = Student('Nathan')
    submission_list = student.list_of_submissions
    
    assert submission_list == []

def test_return_list_after_adding_a_submission():
    student = Student('Nathan')
    student.add_submission('submission1')
    submission_list = student.list_of_submissions
    
    assert submission_list == ['submission1']

def test_return_list_after_adding_multiple_submissios():
    student = Student('Nathan')
    student.add_submission('submission1')
    student.add_submission('submission2')
    submission_list = student.list_of_submissions
    
    assert submission_list == ['submission1', 'submission2']

def test_return_count_before_submissions():
    student = Student('Nathan')
    count = student.count_submissions()
    
    assert count == 0

def test_return_count_after_adding_a_submission():
    student = Student('Nathan')
    student.add_submission('submission1')
    count = student.count_submissions()
    
    assert count == 1
    
def test_return_count_after_adding_multiple_submissios():
    student = Student('Nathan')
    student.add_submission('submission1')
    student.add_submission('submission2')
    count = student.count_submissions()
    
    assert count == 2