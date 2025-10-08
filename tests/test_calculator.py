import pytest
import pandas as pd
from datetime import datetime
from app.calculator import Calculator

class TestCalc:
    def __init__(self, operation, operand1, operand2, result, timestamp):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.timestamp = timestamp

def test_get_history_dataframe():
    calc = Calculator()
    timestamp = datetime.now()

    # Mock history data
    calc.history = [
        TestCalc("add", 2, 3, 5, timestamp),
        TestCalc("subtract", 5, 2, 3, timestamp)
    ]

    df = calc.get_history_dataframe()

    # Assertions
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["operation", "operand1", "operand2", "result", "timestamp"]
    assert len(df) == 2
    assert df.iloc[0]["operation"] == "add"
    assert df.iloc[1]["result"] == "3"

def test_show_history_with_entries():
    calc = Calculator()
    timestamp = datetime.now()
    
    # Add dummy history
    calc.history = [
        TestCalc("add", 2, 3, 5, timestamp),
        TestCalc("multiply", 4, 5, 20, timestamp)
    ]
    
    # Call the method
    history_list = calc.show_history()
    
    # Expected formatted output
    expected = [
        "add(2, 3) = 5",
        "multiply(4, 5) = 20"
    ]
    
    assert history_list == expected
