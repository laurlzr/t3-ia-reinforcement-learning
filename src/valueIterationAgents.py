# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0

        # Write value iteration code here
        # versão em batch - valores da iteração k são calculados a partir da k-1

        for i in range(self.iterations):
            # copia os valores novos pra não alterar self.values enquanto ainda estamos calculando
            newValues = util.Counter() 

            for state in self.mdp.getStates():

                if self.mdp.isTerminal(state):
                    # se for terminal, não existe ação possível
                    newValues[state] = 0 
                    continue

                # coleta as ações possíveis do estado atual
                actions = self.mdp.getPossibleActions(state)

                if len(actions) == 0:
                    continue

                qValues = []
            
                for action in actions:
                    qValues.append(self.computeQValueFromValues(state, action))
                # pega o maior valor de Q (ótimo) dentre todos os calculados para o estado atual
                newValues[state] = max(qValues)

            # fim do batch - atualiza os valores do agente com os novos valores calculados
            self.values = newValues


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        qValue = 0
        # recupera as transições possíveis do estado atual e ação
        transitions = self.mdp.getTransitionStatesAndProbs(state, action)

        for nextState, probability in transitions:
            # recupera a recompensa da transição do estado atual para o próximo
            reward = self.mdp.getReward(state, action, nextState)
            
            # equação de Bellman 
            # Q(s,a) = Σ P(s'|s,a) * [R(s,a,s') + γ * V(s')]
            qValue += probability * (
                reward + self.discount * self.values[nextState]
            )
        return qValue

    
    
    def computeActionFromValues(self, state):
        # escolher a ação com maior Q

        if self.mdp.isTerminal(state):
            return None

        actions = self.mdp.getPossibleActions(state)

        if len(actions) == 0:
            return None

        bestAction = None
        # inicializa o melhor valor como infinito negativo 
        # garante que qualquer Q calculado será maior
        bestValue = float("-inf")

        # para evitar o problema do argMax
        for action in actions:

            qValue = self.computeQValueFromValues(state, action)

            if qValue > bestValue:
                bestValue = qValue
                bestAction = action

        return bestAction

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
