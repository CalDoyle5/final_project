from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from models import Roster
import orm
import repository
import services

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri())) #get_sqlite_file_url  return f"sqlite:///bookmarks.db"
app = Flask(__name__)


@app.route("/roster", methods=["GET"]) #test if a list of players comes back, steal from their list.
def roster_endpoint():
    session = get_session()
    repo = repository.SqlAlchemyRepository(session)
    line = Roster(
        request.json["id"], request.json["organization_name"], request.json["player_id"], request.json["coach_id"])
#     ) #Based off the class created or the table created?

#     try:
#         batchref = services.allocate(line, repo, session)
#     except (models.OutOfStock, services.InvalidSku) as e: #What goes in services.py to make this work not out of stock byt a version of what i have
#         return {"message": str(e)}, 400

    # return {"batchref": batchref}, 201

"""What do i do"""

