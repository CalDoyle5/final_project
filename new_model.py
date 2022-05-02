from __future__ import annotations
from calendar import c
from dataclasses import dataclass
from datetime import date
from typing import Optional, List, Set
from typing import NamedTuple
from collections import namedtuple

class InvalidPlayer(Exception):
    pass


class InvalidCoach(Exception):
    pass


def add_player_to_scout(players: List[Player], scout: Scout) -> str:
    try:
        player = next(p for p in sorted(players) if p.scout_id is False and p.want_trade())
        scout.add_player(player)
        return scout.player_id
    except StopIteration:
        raise InvalidPlayer(f"Can't trade {player.player_id}")

# def add_player_to_scout(trade: Trade, players: List[Player], scout: Scout) -> str:
#     try:
#         player = next(p for p in sorted(players) if p.scout_id is False and p.want_trade())
#         scout.add_player(player)
#         return trade.trade_id
#     except StopIteration:
#         raise InvalidPlayer(f"Can't trade {player.player_id}")


def acquiring_player_from_another_scout(trade: Trade, player: Player, scouts: List[Scout]) -> str:
    try:
        current_scout = next(s for s in sorted(scouts) if s.scout_id == player.scout_id)
        new_scout = next(s for s in sorted(scouts) if s.request_player(player) == player.scout_id)
        current_scout.remove_player(player)
        new_scout.add_player(player)
        return trade.trade_id
    except StopIteration:
        raise InvalidPlayer(f"Can't trade {player.player_id}")


def add_coach_to_team(trade: Trade, coaches: List[Coach], team: Team):
    try:
        coach = next(c for c in sorted(coaches) if c.team_id is False and c.want_trade())
        team.add_coach(coach)
        return trade.trade_id
    except StopIteration:
        raise InvalidCoach(f"Can't trade {coach.coach_id}")


def acquiring_coach_from_another_team(trade: Trade, coach: Coach, teams: List[Team]) -> str:
    try:
        current_team = next(t for t in sorted(teams) if t.coach_id == coach.coach_id)
        new_team = next(t for t in sorted(teams) if t.request_coach(coach) == coach.coach_id) #Request player? for coach
        current_team.remove_coach(coach)
        new_team.add_coach(coach)
        return trade.trade_id
    except StopIteration:
        raise InvalidCoach(f"Can't trade {coach.coach_id}")




class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        


class Player(Person):
    def __init__(self, player_id: int, team_id: int, coach_id: int, scout_id: int, first_name: str, last_name: str, decision: bool):
        
        super().__init__(first_name, last_name)
        
        self.player_id = player_id
        self.team = team_id
        self.coach = coach_id
        self.scout = scout_id
        self.decision = decision
        #self._trades = set()

    def check_age(self, age: int) -> bool:
        return age < 15

    def can_trade(self) -> bool:
        return self.player_id

    def want_trade(self) -> bool:
        if self.can_trade():
            return self.decision is True
    
    

class Scout(Person):
    def __init__(self, scout_id: int, first_name: str, last_name: str, players: List[Player]):
        
        super().__init__(first_name, last_name)
        self.scout_id = scout_id
        self._players = players

    def check_age(self, age: int) -> bool:
        return age > 21

    def add_player(self, player: Player):
        if player.can_trade:
            if player.want_trade:
                self._players.add(player)
    
    def remove_player(self, player: Player):
        if player.can_trade:
            if player.want_trade:
                self._players.remove(player)

    def request_player(self, player: Player):
        return player.player_id
       

    
class Coach(Person):
    def __init__(self, first_name: str, last_name: str, coach_id: int, team_id: int, players: List[Player], decision: bool):
        
        super().__init__(first_name, last_name)
        self.coach = coach_id
        self.team = team_id
        self._players = players
        self.decision = decision


    def check_age(self, age: int) -> bool:
        return age > 21

    
    def can_trade(self) -> bool:
        return self.coach
    
    
    def add_player(self, player: Player):
        if player.can_trade:
            if player.want_trade:
                self._players.add(player)
    
    def remove_player(self, player: Player):
        if player.can_trade:
            if player.want_trade:
                self._players.remove(player)


    def want_trade(self) -> bool:
        if self.can_trade():
            return self.decision is True


class Team():
    def __init__(self, team_id: int, coach_id: int, player_id: int):
        
        self.team = team_id
        self.current_coach = coach_id
        self.player = player_id

    def add_coach(self, coach: Coach):
        if coach.can_trade:
            if coach.want_trade:
                self.current_coach.add(coach)

    def change_coach(self, new_coach: Coach):
        if self.current_coach.want_trade:
            return self.current_coach == new_coach

    def request_coach(self, coach: Coach):
        return coach.coach_id



class Trade():
    def __init__(self, trade_id: int, scout_id: Scout, player_id: Player, coach_id: Coach, team_id: Team, date: date):

        self.trade = trade_id
        self.scout = scout_id
        self.player = player_id
        self.coach = coach_id
        self.team = team_id
        self.date = date

    
    



