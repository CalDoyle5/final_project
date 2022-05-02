#from models import Trade, Roster, Coach, Player, Scout



#Original class for trades
class Traded:
    def __init__(self, player_id: int, team_id: int, status: str = 'new'):
        self.user_id = player_id
        self.status = status
        self.team_id = team_id

    def set_status(self, new_status: str):
        if new_status not in ('traded', 'registered', 'confirmed'):
            raise ValueError(f'{new_status} is not a correct status!')

        self.status = new_status

#Refactored event sourcing classes
class PlayerAdded:
    def __init__(self, player_id: int, team_id: int):
        self.player_id = player_id
        self.team_id = team_id

class PlayerTrade:
    def __init__(self, player_id: int, team_id: int, new_status: str):
        self.player_id = player_id
        self.new_status = new_status
        self.team_id = team_id

#Trade mutations
trade = Traded(player_id=101, team_id = 201) # 1
trade.set_status('traded')  # 2
trade.set_status('registered')  # 3
trade.set_status('confirmed') # 4


#Corresponding event streams
events_stream = [
    PlayerAdded(player_id=101 , team_id = 201),  # 1
    PlayerTrade(player_id=101, team_id = 301, new_status = 'traded'),  # 2
    PlayerTrade(player_id=101, team_id = 301, new_status = 'registered'),  # 3
    trade.set_status('confirmed') # 4
]

# A way to restore order’s state using these events

class Traded_2:
    def __init__(self, events: list):  # 1 Now the only way to instantiate a trade is to give it a list of events it should be initialized with
        for event in events:
            self.apply(event)  # 2 Inside __init__, we apply every event, causing state mutation

        self.changes = []  # 3 We need to keep an append-only list of state mutations done after Order initialization, because to save changes we just need to persist new events. Old ones are already saved and we will never delete them

    def apply(self, event): # 4 A heart of an event sourcing aggregate is an apply method. Inside we mutate state. I will show a bit more clever implementation later, without  if-elif-else block.
        if isinstance(event, PlayerAdded):
            self.team_id = event.team_id
            self.status = 'new'
        elif isinstance(event, PlayerTrade):
            self.status = event.new_status
        else:
            raise ValueError('Unknown event!')

    def set_status(self, new_status: str):  # 5 Crucial change is inside set_status method. We still validate input, but instead of modifying object’s fields directly
        if new_status not in ('new', 'paid', 'confirmed', 'shipped'):
            raise ValueError(f'{new_status} is not a correct status!')

        event = PlayerTrade(new_status)  # 6 we prepare StatusChanged event, put it through apply
        self.apply(event)
        self.changes.append(event)  # 7 and finally append new event to our changes list




