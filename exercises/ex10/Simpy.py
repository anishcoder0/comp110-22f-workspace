"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730574592"


class Simpy:
    """This class is a NUMpy inspired copy cat."""
    values: list[float]

    def __init__(self, x) -> None:
        """Initializing Values."""
        self.values = x
    
    def __repr__(self) -> str:
        """Magic method that returns a str representation."""
        return f"Simpy({self.values})"
    
    def fill(self, val: float, num_val: int) -> None:
        """Fills the entire list with the num_val amount of val."""
        if len(self.values) != num_val:
            for x in range(len(self.values)):
                self.values.pop(0)
        for x in range(num_val):
            self.values.append(val)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Generates a list of numbers and has a start, stop(not included), and a fractional step function."""
        assert step != 0.0
        x: int = 0
        if step < x:
            while x < (stop / step + (step)):
                self.values.append(start)
                start += step
                x += 1
        else:
            while x < (stop / step - step):
                self.values.append(start)
                start += step
                x += 1

    def sum(self) -> float:
        """Adds numbers together and returns a float."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds either a float and Simpy or a Simpy and a Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                result.values.append(i + rhs)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
            return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Takes a number to a power of either a float or a Simpy."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for i in self.values:
                result.values.append(i ** rhs)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
            return result            

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Tests to see if 2 items are equal to each other."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i == rhs)
            return result
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
            return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Checks whether it is greater than the value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i > rhs)
            return result
        else:
            val: list[bool] = []
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                val.append(self.values[i] > rhs.values[i])
            return val
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gets the item that is asked by from the subscription operator."""
        new_list: Simpy = Simpy([])
        a: int = 0
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for i in rhs:
                if i: 
                    new_list.values.append(self.values[a])
                    a += 1
                else:
                    a += 1
            return new_list
    # TODO: Your constructor and methods will go here.