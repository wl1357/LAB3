import LAB2.LAB2 as bmi #import <folder.file>

def test_over_weight():
    assert(bmi.calculate_bmi(1.73, 200) == 1)
def test_normal_weight():
    assert(bmi.calculate_bmi(1.73,60)==0) 

def test_under_weight():
    assert(bmi.calculate_bmi(1.73,40)==-1)

    



