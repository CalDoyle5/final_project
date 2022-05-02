#Edit code to fit roster requirements
import abc
# import models 
import new_model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, player: new_model.Player):
        raise NotImplementedError

    # @abc.abstractmethod
    # def add_coach(self, coach: new_model.Coach):
    #     raise NotImplementedError

    @abc.abstractmethod
    def get(self, player_id) -> new_model.Player:
        raise NotImplementedError

    # @abc.abstractmethod
    # def get_coach(self, coach_id) -> new_model.Coach:
    #     raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, player):
        self.session.add(player)

    def get(self, player_id):
        return self.session.query(new_model.Player).filter_by(player_id=player_id).one()

    # def get_coach(self, coach_id):
    #     return self.session.query(new_model.Coach).filter_by(coach_id=coach_id).one()

    def list(self):
        return self.session.query(new_model.Player).all()


"""
Do I use rosters or players? or mutlitple here? 
"""