"""Tests for `sanjayutil` package."""
import pytest
from sanjayutil import sanjayutil


def test_greet(capsys):
    """Correct name argument prints"""
    sanjayutil.greet("Sanjay")
    captured = capsys.readouterr()
    assert "Sanjay" in captured.out
