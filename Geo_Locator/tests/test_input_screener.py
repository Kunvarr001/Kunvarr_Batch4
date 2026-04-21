import pytest
from input_screener import InputScreener

class TestInputScreener:

    def test_given_valid_input_when_checked_then_returns_true(self):
        screener = InputScreener()
        assert screener.is_valid("Delhi") is True

    def test_given_short_input_when_checked_then_returns_false(self):
        screener = InputScreener()
        assert screener.is_valid("ab") is False

    def test_given_empty_input_when_checked_then_returns_false(self):
        screener = InputScreener()
        assert screener.is_valid("") is False

    def test_given_none_input_when_checked_then_returns_false(self):
        screener = InputScreener()
        assert screener.is_valid(None) is False