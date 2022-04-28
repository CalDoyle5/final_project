import pytest
from models import Roster, Player
import repository
import services


class FakeRepository(repository.AbstractRepository):
    def __init__(self, roster):
        self._roster = set(roster)

    def add(self, roster):
        self._roster.add(roster)

    def get(self, reference):
        return next(r for r in self._roster if r.reference == reference)

    def list(self):
        return list(self._roster)


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True

#id: int, first_name: str, last_name: str, organization_name: str, position: str, age: int
def test_returns_allocation():
    player = Player(1, "Callum", "Doyle", "Saints", "Forward", 10) 
    #roster.add_player(player)
    #Do I have to manually add players to roster?
    roster = Roster() #Are you supposed to format this into a list? [1, "Callum", "Doyle", "Saints", "Forward", 10]
    repo = FakeRepository([roster])
    roster.add_player(player)

    result = services.registration(player, repo, FakeSession())
    assert result == 1


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