import pytest
from custom_stack.custom_stack_class import CustomStack, StackEmptyException, StackFullException, NumberAscOrder

@pytest.fixture
def stack():
    return CustomStack(6)

def test_stack_operations(stack):
    # Testa as operações básicas da pilha: push, pop, peek, is_empty e size
    # Testa push e peek
    stack.push(1)
    assert stack.peek() == 1

    # Testa push e size
    stack.push(2)
    assert stack.size() == 2

    # Testa pop
    assert stack.pop() == 2

    # Testa peek após pop
    assert stack.peek() == 1

    # Testa pop e size
    assert stack.pop() == 1
    assert stack.size() == 0

    # Testa is_empty após operações
    assert stack.is_empty() == True

    # Testa exceção de pilha vazia ao tentar pop
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_sort_with_empty_stack(stack, mocker):
    # Testa ordenação com pilha vazia
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == []

def test_sort_with_six_numbers(stack, mocker):
    # Testa ordenação com seis números aleatórios
    for num in [15, 7, 23, 40, 10, 3]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[3, 7, 10, 15, 23, 40])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [3, 7, 10, 15, 23, 40]

def test_sort_with_sorted_numbers(stack, mocker):
    # Testa ordenação com números já ordenados
    for num in [1, 2, 3, 4, 5, 6]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[1, 2, 3, 4, 5, 6])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [1, 2, 3, 4, 5, 6]

def test_sort_with_reverse_sorted_numbers(stack, mocker):
    # Testa ordenação com números em ordem reversa
    for num in [6, 5, 4, 3, 2, 1]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[1, 2, 3, 4, 5, 6])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [1, 2, 3, 4, 5, 6]

def test_sort_with_duplicate_numbers(stack, mocker):
    # Testa ordenação com números duplicados
    for num in [3, 7, 23, 7, 10, 2]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[2, 3, 7, 7, 10, 23])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [2, 3, 7, 7, 10, 23]

def test_sort_with_negative_numbers(stack, mocker):
    # Testa ordenação com números negativos
    for num in [-6, -5, -4, -3, -2, -1]:
        stack.push(num)
    mocker.patch.object(NumberAscOrder, 'sort', return_value=[-6, -5, -4, -3, -2, -1])
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [-6, -5, -4, -3, -2, -1]