import random
import logging
from gameMechanicsBackend import Game

class AI:
    _instance = None
    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            logging.basicConfig(filename='battleships.log', level=logging.INFO, filemode='w', force=True)
            logging.info('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._instance.initialise()
        return cls._instance

    def initialise(self, game: Game):
        self.targets = []

    def AIRandomAttack(self):
        guessRow = random.randint(0, 6)
        guessCol = random.randint(0, 6)
        if [guessRow, guessCol] in self.targets

    def AISmartAttack(self):