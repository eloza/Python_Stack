from data_structure.stack import Stack
import pytest

@pytest.fixture()
def stack():
    return Stack()

def test_constructor():
    s = Stack()
    assert len(s) == 0

def test_push(stack):
    stack.push(1995)
    assert len(stack) == 1
    stack.push(2001)
    assert len(stack) == 2

def test_pop(stack):
    stack.push("push barman")
    stack.push("to open old wounds")
    assert stack.pop() == "to open old wounds"
    assert stack.pop() == "push barman"
    assert stack.pop() is None

