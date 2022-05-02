import pytest
# from models import Roster, Player
import new_model
import repository
import services


class FakeRepository(repository.AbstractRepository):
    def __init__(self, players):
        self._players = set(players)
        # self._coaches = set(coaches)

    def add(self, player):
        self._players.add(player)
        # self._coaches.add(coach)

    def get(self, reference):
        return next(p for p in self._players if p.player_id == reference)

    # def get_coach(self, reference):
    #     return next(c for c in self._coaches if c.coach_id == reference)

    def list(self):
        return list(self._players)


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_adding_player_to_scout():
    player = new_model.Player(1, 1, 1, None, "Callum", "Doyle", True)
    player2 = new_model.Player(2, 1, 1, None, "Stevie", "Doyle", False)
    player3 = new_model.Player(3, 1, 1, None, "Liam", "Doyle", False)
    player4 = new_model.Player(4, 1, 1, None, "Arnold", "Doyle", False)
    players = [player2, player3, player4]
    coach = new_model.Coach("Frank", "Lampard", 1, 1, [], True)
    scout = new_model.Scout(1, "Mino", "Raiola", players)
    repo = FakeRepository([player])

    # result = services.add_player_to_scout(1, player, scout, repo, FakeSession())
    result = services.add_player_to_scout(player, scout, repo, FakeSession())
    assert result == 1

# def test_adding_coach_to_team():
#     coach = new_model.Coach("Frank", "Lampard", 1, 1, [], True)
#     team = new_model.Team(1, None, None)
#     repo = FakeRepository([coach])

#     # result = services.add_player_to_scout(1, player, scout, repo, FakeSession())
#     result = services.add_coach_to_team(1, coach, team, repo, FakeSession())
#     assert result == 1

# #id: int, first_name: str, last_name: str, organization_name: str, position: str, age: int
# def test_returns_allocation():
#     player = Player(1, "Callum", "Doyle", "Saints", "Forward", 10) 
#     #roster.add_player(player)
#     #Do I have to manually add players to roster?
#     roster = Roster() #Are you supposed to format this into a list? [1, "Callum", "Doyle", "Saints", "Forward", 10]
#     repo = FakeRepository([roster])
#     roster.add_player(player)

#     result = services.registration(player, repo, FakeSession())
#     assert result == 1


# def test_error_for_invalid_player():
#     player = models.Player(1, "Callum", "Doyle", "Saints", "Forward", 10)
#     roster = models.Roster([1, "Callum", "Doyle", "Saints", "Forward", 10])
#     repo = FakeRepository([roster])

#     with pytest.raises(services.InvalidPlayer, match="Invalid player NONEXISTENTPLAYER"):
#         services.allocate(player, repo, FakeSession())


# def test_commits():
#     player = models.Player(1, "Callum", "Doyle", "Saints", "Forward", 10)
#     #roster = models.Roster([1, "Callum", "Doyle", "Saints", "Forward", 10])
#     repo = FakeRepository([player])
#     session = FakeSession()

#     services.registration(player, repo, session)
#     assert session.committed is True


# def test_returns_registration():
#     player = Player(1, "Callum", "Doyle", "Saints", "Forward", 10)
#     #roster.add_player(player)
#     #Do I have to manually add players to roster?
#     roster1 = Roster(100) #Are you supposed to format this into a list? [1, "Callum", "Doyle", "Saints", "Forward", 10]
#     # roster2 = Roster(101)
#     # rosters = [roster1, roster2]
#     repo = FakeRepository([roster1])
#     roster1.add_player(player)

#     result = services.register(player, repo, FakeSession())
#     assert result is True


# def test_returns_allocation():
#     line = model.OrderLine("o1", "COMPLICATED-LAMP", 10)
#     batch = model.Batch("b1", "COMPLICATED-LAMP", 100, eta=None)
#     repo = FakeRepository([batch])

#     result = services.allocate(line, repo, FakeSession())
#     assert result == "b1"