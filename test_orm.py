from charset_normalizer import models
from models import Player
# test mapper

# test retireving players
# id: int, first_name: str, last_name: str, organization_name: str, position: str, age: int


def test_retrieving_players(session):
    session.execute(
        "INSERT INTO players (id, first_name, last_name, organization_name, position, age)"
        ' VALUES (1, "Callum", "Doyle", "Saints", "striker", 24)'
    )
    session.execute(
        "INSERT INTO players (id, first_name, last_name, organization_name, position, age)"
        ' VALUES (2, "Stefan", "Andjelic", "Gooners", "striker", 34)'
    )
    expected = [
        Player(1, "Callum", "Doyle", "Saints", "striker", 24),
        Player(2, "Stefan", "Andjelic", "Gooners", "striker", 34),
    ]
    
    assert len(session.query(Player).all()) == 2


#def test_player_is_not_the_same(session):

    
    #Test that players are not __eq__
    #local variable that says: are the same= False


def test_saving_player(session):
    player = Player(3, "Liam", "Doyle", "Saints", "defender", 22)
    session.add(player)
    session.commit()
    rows = session.execute(
        'SELECT id, first_name, last_name, organization_name, position, age FROM "players"'
    )
    assert list(rows) == [(3, "Liam", "Doyle", "Saints", "defender", 22)]


"""
Do i need more tests or are these sufficient?
"""
