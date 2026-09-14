import math

f = lambda x: max(math.sin(x), 0)

def test_f():
    test_values = [math.pi/2, -math.pi/2]
    expected = [math.sin(test_values[0]), 0]
    tol = 1E-14
    success = all(abs(expected_value-f(test_value))<=tol for test_value, expected_value in zip(test_values, expected))
    msg = "Failure!"
    assert success, msg
test_f()
