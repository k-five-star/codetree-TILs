class Agent:
    def __init__(self, codename, score):
        self.codename = str(codename)
        self.score = int(score)

    def agentInfo(self):
        return self.codename, self.score

    def agentScore(self):
        return self.score

agentList = [Agent(*input().split()) for _ in range(5)]

_min = 999
least = 0

for agent in agentList:
    if agent.agentScore() < _min:
        _min = agent.agentScore()
        least = tuple(agent.agentInfo())

print(*least)