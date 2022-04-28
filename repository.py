#Edit code to fit roster requirements
import abc
import models as model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, roster: model.Roster):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Roster:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, roster):
        self.session.add(roster)

    def get(self, reference):
        return self.session.query(model.Roster).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Roster).all()


"""
Do I use rosters or players? or mutlitple here? 
"""