import pytest
from BalanceBraces import BalanceBraces
from BalanceBraces.Inputs import inputs as balance_braces_inputs

@pytest.fixture()
def balancer():
    return BalanceBraces.BalanceBraces()

def test_init(balancer: BalanceBraces.BalanceBraces):
    assert not balancer.stack
    assert balancer.braces == ['[', '{', '(', ')', '}', ']']

def test_are_braces_balanced(balancer: BalanceBraces.BalanceBraces):
    for step in balance_braces_inputs.test_cases:
        actual = balancer.are_braces_balanced(step[0])
        expected = step[1]
        assert actual == expected, "are_braces_balanced returned {} for {}, expected: {}".format(actual, step[0], expected)