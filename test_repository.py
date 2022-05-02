import pytest
# from models import Coach, Player, Roster, Scout
import repository
import new_model


def test_repository_can_save_a_player(session):
    player = new_model.Player(1, 2, 2, 1, "Callum", "doyle", True)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(player)
    session.commit()

    rows = session.execute(
        'SELECT player_id, team_id, coach_id, scout_id, first_name, last_name, decision FROM "players"'
    )
    assert list(rows) == [(1, None, None, None, "Callum", "doyle", 1)]


# def insert_player(session):
    
#     repo = repository.SqlAlchemyRepository(session)
#     repo.add(Player)
#     session.commit()
#     session.execute(
#         "INSERT INTO players (id, first_name, last_name, organization_name, position, age)"
#         ' VALUES ("1, "Callum", "Doyle", "Saints", "Forward", 10)'
#     )
#     [[player_id]] = session.execute(
#         "SELECT id FROM players WHERE playerid=:playerid AND sku=:sku",
#         dict(playerid=1, last_name="Doyle"),
#     )
#     return player_id
    

# #Can this just be test rosters?





    


