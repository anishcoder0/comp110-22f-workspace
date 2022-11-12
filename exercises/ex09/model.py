"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
import math


__author__: str = "730574592"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x: float = x
        self.y: float = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, cell: Point) -> float:
        """Calculates the distance between the 2 points."""
        return math.sqrt((self.x - cell.x)**2 + ((self.y - cell.y)**2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location: Point = location
        self.direction: Point = direction

    def contract_disease(self) -> None:
        """Makes the cell infected."""
        self.sickness: int = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """This tells if the cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """This tells if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False   
    
    def tick(self) -> None:
        """Updates the cell location and direction."""
        self.location: Point = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize() 

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "orange"
        else:
            return "blue"
            
    def contact_with(self, other: Cell) -> None:
        """Tells if cell is in contact and infects disease."""
        if (other.is_infected()) and (self.is_vulnerable()):
            self.contract_disease()
        elif (self.is_infected()) and (other.is_vulnerable()):
            other.contract_disease()
    
    def immunize(self) -> None:
        """Makes the cell immune to sickness."""
        self.sickness: int = constants.IMMUNE

    def is_immune(self) -> bool:
        """Checks if the constant is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False
    

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Must have x number of cells infected at start.")
        if (infected + immune) > cells:
            raise ValueError("Improper number of immune or infected cells in the call to model's constructor.")
        if immune >= cells or immune < 0:
            raise ValueError("Improper number of immune or infected cells in the call to model's constructor.")
        self.population: list = []
        for _ in range(immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.immunize()
            self.population.append(cell)
        for _ in range(infected):
            start_location = self.random_location()
            start_direction = self.random_direction(speed)
            cell = Cell(start_location, start_direction)
            cell.contract_disease()
            self.population.append(cell)
        for _ in range(cells - infected - immune):
            start_location = self.random_location()
            start_direction = self.random_direction(speed)
            cell = Cell(start_location, start_direction)
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
    
    def check_contacts(self) -> None:
        """Checks to see if each cell is infected."""
        i: int = 0
        while i < len(self.population):
            k: int = i + 1
            while k < len(self.population):
                if self.population[i].location.distance(self.population[k].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[k])
                k += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        counter: int = 0
        for cell in self.population:
            if cell.is_immune() or cell.is_vulnerable():
                counter += 1
            if cell.is_infected():
                return False
            if counter == len(self.population):
                return True   
        else:
            return False