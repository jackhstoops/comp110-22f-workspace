"""Utility class for numerical operations."""

from __future__ import annotations
from typing import Union

__author__ = "730489241"


class Simpy:
    """NumPy impersonator."""
    values: list[float]

    def __init__(self, num: list[float]):
        """Constructor function."""
        self.values = num

    def __repr__(self) -> str:
        """Creates a string representation."""
        return f"Simpy({self.values})"
    
    def fill(self, float_fill: float, int_fill: int) -> None:
        """Creates repeated values in Simpy."""
        i: int = 0
        while i < int_fill:
            self.values.append(float_fill)
            i += 1
            if len(self.values) == int_fill:
                break
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in values attributes within range of values."""
        i: float = start
        assert step != 0
        if start < 0:
            while i > stop:
                self.values.append(i)
                i += step
        while i < stop:
            self.values.append(i)
            i += step

    def sum(self) -> float:
        """Sums the list of values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Sums values and creates a new Simpy."""
        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item + rhs) 
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.values.append(self.values[item] + rhs.values[item])
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Applies an exponent and makes a new Simpy."""
        result: Simpy = Simpy([])

        if isinstance(rhs, float):
            for item in self.values:
                result.values.append(item ** rhs) 
        else:
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                result.values.append(self.values[item] ** rhs.values[item])
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask."""
        result: list[bool] = []
        i: int = 0

        if isinstance(rhs, float):
            for item in self.values:
                result.append(item == rhs)
        else:   
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask."""
        result: list[bool] = []
        i: int = 0

        if isinstance(rhs, float):
            for item in self.values:
                result.append(item > rhs)
        else:   
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Add subscription notation."""
        result: Simpy = Simpy([])

        if isinstance(rhs, int):
            if rhs < len(self.values):
                return self.values[rhs]
        else:
            for i, item in enumerate(rhs):
                if item is True:
                    result.values.append(self.values[i])
            return result