from equations import(
    add,
    sub,
    mult,
    div
)

def test_add():
    assert add(2,10) == 12
    assert add(3,5) == 8
    assert add(4,6) == 10

def test_sub():
    assert sub(10,5) == 5
    assert sub(8,4) == 4
    assert sub(3,1) == 2

def test_mult():
    assert mult(1,2) == 2
    assert mult(5,5) == 25
    assert mult(7,3) == 21

def test_div():
    assert div(10,2) == 5
    assert div(100,25) == 4
    assert div(8,4) == 2