import dotp

def test_dot_product():
    assert dotp.dot_product([1, 2, 3], [1, 2, 3]) == 14
    assert dotp.dot_product([],[]) == 0 

test_dot_product()