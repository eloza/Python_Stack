from data_structure.stack import Stack
import pytest

@pytest.fixture()
def stack():
    return stack()
def test_constructor():
    s = Stack()
    assert len(s) == 0

def test_push():
    stack.push(3)
    assert len(stack) == 1

