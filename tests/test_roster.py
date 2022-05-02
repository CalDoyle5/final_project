# import pytest
# from models import Coach, Player, Roster, Scout



# def test_roster_quantity():
#     # arrange
#     roster = Roster(1)
#     coach = Coach(1, "super", "coach", 40, roster)
#     player1 = Player(1, "super", "center", "all blacks", "center", 12)
#     player2 = Player(2, "super", "forward", "all blacks", "forward", 13)
#     # act
#     coach.roster.add_player(player1)
#     coach.roster.add_player(player2)

#     # assert
#     assert coach.roster.get_roster_quantity() == 2


# # def test_scout_roster_quantity():
# #     # arrange
# #     roster = Roster(1)
# #     scout = Scout(1, "super", "scout", 40, 21)
# #     player1 = Player(1, "super", "center", "all blacks", "center", 12)

# #     # act
# #     scout.add_player(player1)

# #     # assert
# #     assert scout.get_roster_quantity() == 1


# def test_player_age():

#     # arrange
#     roster = Roster(1)
#     coach = Coach(1, "super", "coach", 40, roster)
#     player = Player(1, "super", "center", "all blacks", "center", 12)

#     # act
#     coach.roster.add_player(player)

#     # assert
#     assert player.check_age(12)


# def test_scout_validation():

#     # arrange
#     scout = Scout(1, "super", "scout", 40, 22,)

#     # act
#     scout.check_age(22)
#     scout.validated = True

#     # assert
#     assert scout.validated
#     assert scout.check_age(22)


# def test_coach_validation():

#     # arrange
#     roster = Roster(1)
#     coach = Coach(1, "super", "scout", 40, roster)

#     # act
#     coach.check_age(22)
#     coach.validated = True

#     # assert
#     assert coach.validated
#     assert coach.check_age(22)
