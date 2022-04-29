from __future__ import annotations

from models import registration, Coach, Player, Roster, Trade, Scout

from repository import AbstractRepository


class InvalidPlayer(Exception):
    pass


def is_valid_player(player_id, rosters):
    return player_id in {r.player_id for r in rosters}

#Change allocate function to register
def register(player: Player, repo: AbstractRepository, session) -> bool:
    rosters = repo.list()
    if not is_valid_player(player.id, rosters):
        raise InvalidPlayer(f"Invalid player {player}")
    rosterref = registration(player, rosters)
    session.commit()
    return rosterref #Without ref what am i returning exactly

# def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:
#     batches = repo.list()
#     if not is_valid_sku(line.sku, batches):
#         raise InvalidSku(f"Invalid sku {line.sku}")
#     batchref = model.allocate(line, batches)
#     session.commit()
#     return batchref


def trade(player, roster, repo: AbstractRepository, session) -> str:
    rosters = repo.list()

    session.commit()



