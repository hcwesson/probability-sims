import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

games = 82

prbA = 0.7
prbB = 0.6
prbC = 0.5

shotsA = 30
shotsB = 20
shotsC = 10

historyA = []
historyB = []
historyC = []

gameTotalsA = []
gameTotalsB = []
gameTotalsC = []
gameTotalsAll = []

for i in range(0, games-1):
    gameTotalA = 0
    gameTotalB = 0
    gameTotalC = 0
    for j in range(0, shotsA-1):
        if prbA > random.uniform(0, 1):
            historyA.append(1)
            gameTotalA += 1
        else:
            historyA.append(0)
    for k in range(0, shotsB-1):
        if prbB > random.uniform(0, 1):
            historyB.append(1)
            gameTotalB += 1
        else:
            historyB.append(0)
    for l in range(0, shotsC-1):
        if prbC > random.uniform(0, 1):
            historyC.append(1)
            gameTotalC += 1
        else:
            historyC.append(0)

    gameTotalsA.append(gameTotalA)
    gameTotalsB.append(gameTotalB)
    gameTotalsC.append(gameTotalC)
    gameTotalsAll.append(gameTotalA+gameTotalB+gameTotalC)

fig, axs = plt.subplots(4, 1, constrained_layout=True)
n_bins = games
axs[0].hist(gameTotalsA, bins=n_bins)
axs[0].set_title("A: Total shots by game")
axs[1].hist(gameTotalsB, bins=n_bins)
axs[1].set_title("B: Total shots by game")
axs[2].hist(gameTotalsC, bins=n_bins)
axs[2].set_title("C: Total shots by game")
axs[3].hist(gameTotalsAll, bins=n_bins)
axs[3].set_title("All Players: Total shots by game")

plt.show()
