import matplotlib.pyplot as plt
import random

players_count = int(input('Total number of players: '))
count_of_trades = int(input('Total number of trades: '))
initial_money = int(input('Initial money: '))

# players_count = 20
# count_of_trades = 1_000_000
# initial_money = 10


class Player:
    def __init__(self, initial_money) -> None:
        self.money = initial_money
        self.historyMoney = [initial_money]
        self.historyMoney.append(initial_money)
        self.initial_money = initial_money
        # self.money_life = [0] * ((initial_money * players_count-1) + 20 + 1)
        self.money_life = [0] * (initial_money * players_count + 1)
        self.money_life[initial_money] = 1


def trade(players_in_trades):
    if len(players_in_trades) < 2:
        print("Not enough players to trade.")
        return

    player1, player2 = random.sample(players_in_trades, 2)

    player1.money -= 1
    player2.money += 1

    # add history
    player1.historyMoney.append(player1.money)
    player2.historyMoney.append(player2.money)

    player1.money_life[player1.money] += 1
    player2.money_life[player2.money] += 1

    # remove player if he is out of money
    if player1.money <= 0:
        players_in_trades.remove(player1)


# create players
players = [Player(initial_money) for _ in range(players_count)]
# players.append(Player(20))

players_in_trades = players.copy()

for i in range(count_of_trades):
    trade(players_in_trades)
    if len(players_in_trades) == 1:
        print("Only one player left.")
        break


def display_money_changes(players):
    plt.figure(figsize=(10, 5))

    for player in players:
        plt.plot(player.historyMoney)

    plt.title("Money Changes for All Players")
    plt.xlabel("Time")
    plt.ylabel("Money")
    plt.show()


def display_money_lifes(players):
    plt.figure(figsize=(10, 5))

    for player in players:
        plt.plot(player.money_life)

    plt.title("Money Changes for All Players")
    plt.xlabel("Money")
    plt.ylabel("Count")
    plt.show()


display_money_changes(players)
display_money_lifes(players)
