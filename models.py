from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set
from typing import NamedTuple
from collections import namedtuple

#from sqlalchemy import Date


class FullRoster(Exception):
    pass


def registration(player, rosters: List[Roster]) -> str:
    try:
        roster = next(r for r in sorted(rosters) if r.can_allocate(player))
        roster.allocate(player)
        return rosters.reference
    except StopIteration:
        raise FullRoster(f"Roster is full for {rosters.reference}")


class Person:
    def __init__(self, id: int, first_name: str, last_name: str, age: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Coach(Person):
    def __init__(
        self, id: int, first_name: str, last_name: str, organization_name: str, age: int, roster: Roster
    ):
        super().__init__(id, first_name, last_name, age)

        self.organization_name = organization_name
        self.roster = roster
        self.validated = False

    def get_roster(self):
        return self.roster

    def check_age(self, age: int) -> bool:
        return age > 21


class Player(Person):
    def __init__(
        self, id: int, first_name: str, last_name: str, organization_name: str, position: str, age: int
    ):
        super().__init__(id, first_name, last_name, age)

        self.position = position
        self.organization_name = organization_name

    def check_age(self, age: int) -> bool:
        return age < 15


class Roster:
    def __init__(self, team_id: int): #qty: int): #SHould i add a rosterref(Check services.allocate)

        self.roster = []
        self.team_id = team_id
        #self.qty = qty
    def remove_players(self, id: int):
        pass

    def add_player(self, player: Player):
        self.roster.append(player)

    def get_roster_quantity(self):
        return len(self.roster)
    
    def check_roster_size(self) -> bool:
        return self.roster.__len__ > 2 and self.roster.__len__ < 10



class Scout(Person, Roster):
    def __init__(
        self, id: int, first_name: str, last_name: str, organization_name: str, age: int, scout_id: int
    ):
        super().__init__(id, first_name, last_name, age)

        self.roster = []
        self.organization_name = organization_name
        self.validated = False
        self.scout_id = scout_id

    def check_age(self, age: int) -> bool:
        return age > 21


class Trade(Player, Roster):
    def __init__(self, id: int, first_name: str, last_name: str, organization_name: str, age: int, scout_id: int, team_id: int, date: date):
        
        super().__init__(id, first_name, last_name, organization_name, age, scout_id)

        self.team_id = team_id
        self.date = date

    def add_player(self, player: Player): #What goes here instead of player class 
        self.roster.append(player)
    
    def remove_players(self, id: int):
        pass
