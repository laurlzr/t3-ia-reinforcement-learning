# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

""""
BridgeGrid é um mapa em grade com um estado terminal de baixa recompensa 
e um estado terminal de alta recompensa separados por uma "ponte" estreita, 
em cada lado da qual há um abismo de recompensa altamente negativa.
"""

# alterar só 1 parâmetro
""" 
com os valores  
answerDiscount = 0.9
answerNoise = 0.2

obs.: o agente não atravessa a ponte, pq tem 20% de chance de cair no abismo
prefere a opção mais segura (saída próxima) com menor recompensa

solução: reduzir o ruído - assim o agente passa a confiar que realmente vai pra onde quer
"""


def question2():
    answerDiscount = 0.9
    answerNoise = 0.0 # agora atravessar a ponte é seguro
    return answerDiscount, answerNoise

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
