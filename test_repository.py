import pytest
# from models import Coach, Player, Roster, Scout
# import repository


# def test_repository_can_save_a_player(session):
#     roster = Player(1, "Callum", "Doyle", "Saints", "Forward", 10)

#     repo = repository.SqlAlchemyRepository(session)
#     repo.add(roster)
#     session.commit()

#     rows = session.execute(
#         'SELECT id, first_name, last_name, organization_name, position, age, FROM "players"'
#     )
#     assert list(rows) == [(1, "Callum", "Doyle", "Saints", "Forward", 10)]


# def insert_player(session):
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





    


