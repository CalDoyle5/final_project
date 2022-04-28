from __future__ import annotations

from models import *

from repository import AbstractRepository


class InvalidPlayer(Exception):
    pass


def is_valid_player(player, rosters):
    return player in {r.player for r in rosters}

#Change allocate function to register
def registration(player, repo: AbstractRepository, session) -> str:
    rosters = repo.list()
    if not is_valid_player(player, rosters):
        raise InvalidPlayer(f"Invalid player {player}")
    rosterref = registration(player, rosters)
    session.commit()
    return rosterref #Without ref what am i returning exactly