# from __future__ import annotations

# from models import registration, Coach, Player, Roster, Trade, Scout
from operator import ne
import new_model
from repository import AbstractRepository
from new_model import Player, Coach, Scout, Trade, Team
from typing import Optional, List, Set


class InvalidPlayer(Exception):
    pass


def is_valid_playerid(player_id, player):
    return player_id == player.player_id

def is_valid_coachid(coach_id, coach):
    return coach_id == coach.coach_id


def add_player_to_scout(player: Player, scout: Scout, repo: AbstractRepository, session) -> str:
    player = repo.get(player.player_id)
    if not is_valid_playerid(player.player_id, player):
        raise InvalidPlayer(f"Invalid player {player.player_id}")
    playerref = new_model.add_player_to_scout(player, scout)
    session.commit()
    return playerref
# def add_player_to_scout(trade: Trade, player: Player, scout: Scout, repo: AbstractRepository, session) -> str:
#     player = repo.get_player(player.player_id)
#     if not is_valid_playerid(player.player_id, player):
#         raise InvalidPlayer(f"Invalid player {player.player_id}")
#     traderef = new_model.add_player_to_scout(trade, player, scout)
#     session.commit()
#     return traderef

def acquiring_player_from_another_scout(trade: Trade, player: Player, scouts: List[Scout], repo: AbstractRepository, session) -> str:
    player = repo.get_player(player.player_id)
    if not is_valid_playerid(player.player_id, player):
        raise InvalidPlayer(f"Invalid player {player.player_id}")
    traderef = new_model.acquiring_player_from_another_scout(trade, player, scouts)
    session.commit()
    return traderef


# def add_coach_to_team(trade: Trade, coach: Coach, team: Team, repo: AbstractRepository, session) -> str:
#     coach = repo.get_coach(coach.coach_id)
#     if not is_valid_coachid(coach.coach_id, coach):
#         raise InvalidPlayer(f"Invalid coach {coach.coach_id}")
#     traderef = new_model.add_coach_to_team(trade, coach, team)
#     session.commit()
#     return traderef






# def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:
#     batches = repo.list()
#     if not is_valid_sku(line.sku, batches):
#         raise InvalidSku(f"Invalid sku {line.sku}")
#     batchref = model.allocate(line, batches)
#     session.commit()
#     return batchref


# class InvalidPlayer(Exception):
#     pass


# def is_valid_player(player_id, rosters):
#     return player_id in {r.player_id for r in rosters}

# #Change allocate function to register
# def register(player: Player, repo: AbstractRepository, session) -> bool:
#     rosters = repo.list()
#     if not is_valid_player(player.id, rosters):
#         raise InvalidPlayer(f"Invalid player {player}")
#     rosterref = registration(player, rosters)
#     session.commit()
#     return rosterref #Without ref what am i returning exactly





