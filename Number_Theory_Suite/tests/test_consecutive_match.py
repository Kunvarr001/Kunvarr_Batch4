import pytest
from consecutive_match import ConsecutiveMatch
from divisor_count import DivisorCount

class TestConsecutiveMatch:

    def setup_method(self):
        self.matcher = ConsecutiveMatch()

    def test_given_15_then_returns_2(self):
        result = self.matcher.get_valid_count(15)
        assert result == 2

    def test_given_2_then_returns_0(self):
        result = self.matcher.get_valid_count(2)
        assert result == 0

    def test_given_10_then_result_non_negative(self):
        result = self.matcher.get_valid_count(10)
        assert result >= 0

    def test_given_negative_number_then_returns_0(self):
        result = self.matcher.get_valid_count(-5)
        assert result == 0

    def test_given_zero_in_divisor_then_exception(self):
        counter = DivisorCount()

        with pytest.raises(ValueError):
            counter.get_count(0)