from game import Agent
from game import Directions
import random


# class DumbAgent(Agent):
#     "An agent that goes East until it can't"
#     def getAction(self, state):
#         "The agent always goes East"
#         return Directions.EAST

class DumbAgent(Agent):
    "An agent that goes East until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.EAST in state.getLegalPacmanActions():
            print("Going East.")
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP


class RandomAgent(Agent):
    def __int__(self):
        pass

    def getAction(self, state):
        possibleActions = state.getLegalPacmanActions()
        return random.choice(possibleActions)


class BetterRandomAgent(Agent):
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        legalActions.pop()
        for legalAction in legalActions:
            successorState = state.generatePacmanSuccessor(legalAction)
            if successorState.getNumFood() < state.getNumFood():
                return legalAction
        return random.choice(legalActions)

class ReflexAgent(Agent):
    def getAction(self, state):
        legalActions = state.getLegalPacmanActions()
        legalActions.pop()
        for legalAction in legalActions:
            successorState = state.generatePacmanSuccessor(legalAction)
            if successorState.getNumFood() < state.getNumFood():
                return legalAction
        return random.choice(legalActions)