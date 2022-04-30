import unittest
from event import *

class Order:
    
    @classmethod
    def create(cls, player_id: int, team_id: int):
        initial_event = PlayerAdded(player_id, team_id)
        instance = cls([initial_event])
        instance.changes = [initial_event]
        return instance


class OrderAggregateTest(unittest.TestCase):

    def test_should_create_order(self):
        order = Order.create(player_id=101, team_id= 301)

        self.assertEqual(order.changes, [PlayerAdded(player_id=101, team_id=301)])

    def test_should_emit_set_status_event(self):
        order = Order([PlayerAdded(player_id=101, team_id= 301)])

        order.set_status('confirmed')

        self.assertEqual(order.changes, [StatusChanged('confirmed')])

class StatusChanged:
    def __init__(self, new_status: str):
        self.new_status = new_status

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False


