import pytest

from monkey_function_demo import divide

def test_divide():
    with pytest.raises(ZeroDivisionError) as er:
        divide(12, 0)
    assert str(er.value) == "Cannot divide by zero"