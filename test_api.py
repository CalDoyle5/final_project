# import uuid
# import pytest
# import requests

# import config


# def random_suffix():
#     return uuid.uuid4().hex[:6]


# def random_player(name=""):
#     return f"player-{name}-{random_suffix()}"


# def random_roster(name=""):
#     return f"batch-{name}-{random_suffix()}"


# def random_playerid(name=""):
#     return f"order-{name}-{random_suffix()}"


# @pytest.mark.usefixtures("restart_api")
# def test_happy_path_returns_201_and_allocated_batch(add_player):
#     player, otherplayer = random_player(), random_player("other")
#     firstplayer = random_playerref(1)
#     secondplayer = random_playerref(2)
#     thirdplayer = random_playerref(3)
#     add_player(
#         [
#             (firstplayer, player, 100, "2011-01-02"),
#             (secondplayer, player, 100, "2011-01-01"),
#             (thirdplayer, player, 100, None),
#         ]
#     )
#     data = {"playerid": random_playerid(), "player": player, "qty": 3}
#     url = config.get_api_url()

#     r = requests.post(f"{url}/allocate", json=data)

#     assert r.status_code == 201
#     assert r.json()["playerref"] == firstplayer


# @pytest.mark.usefixtures("restart_api")
# def test_unhappy_path_returns_400_and_error_message():
#     unknown_player, orderid = random_player(), random_playerid()
#     data = {"orderid": orderid, "sku": unknown_player, "qty": 20} #What neeeds to change in here
#     url = config.get_api_url()
#     r = requests.post(f"{url}/allocate", json=data)
#     assert r.status_code == 400
#     assert r.json()["message"] == f"Invalid sku {unknown_player}"

