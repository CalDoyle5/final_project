from sqlite3 import IntegrityError
from xmlrpc.client import Boolean
from charset_normalizer import models
from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, column, Boolean
from sqlalchemy.orm import mapper, relationship

import models
import new_model

metadata = MetaData()

coaches = Table(
    "coaches",  #Column('person_id', Integer, ForeignKey(tbl_person.c.id), primary_key=True)
    metadata,
    Column("coach_id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(30)),
    Column("last_name", String(30)),
    Column("organization_name", String(100)),
    Column("age", Integer)
)
# player_id, team_id, coach_id, scout_id, first_name, last_name, decision
players = Table(
    "players",  
    metadata,
    Column("player_id", Integer, primary_key=True, autoincrement=True),
    Column("team_id", Integer),
    Column("coach_id", Integer),
    Column("scout_id", Integer),
    Column("first_name", String(30)),
    Column("last_name", String(30)),
    Column("decision", Boolean),
    #Column("date_traded", Date),
)


teams = Table(
    "teams",  
    metadata,
    Column("team_id", Integer, primary_key=True, autoincrement=True),
    Column("organization_name", String(50)),
    Column("player_id", Integer), #ForeignKey("player.id")),
    Column("coach_id", Integer) #ForeignKey("coach.id")),
)

trades = Table(
    "trades",
    metadata,
    Column("trade_id", Integer, primary_key=True, autoincrement=True),
    Column("scout_id", Integer),
    Column("player_id", Integer),
    Column("coach_id", Integer),
    Column("team_id", Integer),
    Column("date", Date),
)


scouts = Table(
    "scouts",
    metadata,
    Column("scout_id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(30)),
    Column("last_name", String(30)),
    Column("organization_name", String(100)),
    Column("age", Integer),
)


# registrations = Table(
#     "registrations",
#     metadata,
#     Column("id", Integer, primary_key=True, autoincrement=True),
#     Column("player_id"), #ForeignKey("player.id")),
#     Column("roster_id") #ForeignKey("roster.id")),

# )

# def start_mappers():
#     scout_mapper = mapper(model.Scout, scouts)
#     roster_mapper = mapper(
#         model.Roster,
#         rosters,
#         properties={
#             "_registrations": relationship( #Adding relationship between registering players to roster
#                 scout_mapper,
#                 secondary=registrations,
#                 collection_class=set,
#             )
#         },
#     )
    

#

def start_mappers():
    player_mapper = mapper(new_model.Player, players)
    scout_mapper = mapper(new_model.Scout, scouts)
    coach_mapper = mapper(new_model.Coach, coaches)
    roster_mapper = mapper(new_model.Team, teams)
    trades_mapper = mapper(new_model.Trade, trades)
    #     model.Roster,
    #     rosters,
    #     properties={
    #         "_registrations": relationship( #Adding relationship between registering players to roster? the mapper binds the domain model and the database schema? Idea is domain model does not have to worry about the database
    #             player_mapper,
    #             secondary=registrations,
    #             collection_class=set,
    #         )
    #     },
    # )
    



"""
FAILED test_orm.py::test_retrieving_players - sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: players
FAILED test_orm.py::test_saving_player - sqlalchemy.orm.exc.UnmappedInstanceError: Class 'scoutlib.models.Player' is not mapped

Do i need another mapper function?
is not a mapper for player so create a new mapper for player

When changes to players:

ERROR test_orm.py::test_retrieving_players - sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'roster.player_id' could not find table ...
ERROR test_orm.py::test_saving_player - sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'roster.player_id' could not find table 'play..

keep scout id team id coach id inside a player as a cheat 
review barky -> simpler model 
"""
    