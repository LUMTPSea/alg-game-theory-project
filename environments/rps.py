import random
import enum

class Choice(enum.Enum):
	ROCK = 1
	PAPER = 2
	SCISSORS = 3


class RPS:

	def __init__(self, history_length):
		self.p1_overall_payoff = 0
		self.p2_overall_payoff = 0
		self.game_history = collections.deque(maxlen=history_length)
		self.history_length = history_length

	
	def get_payoff(player1, player2):
		
		if player1 == Choice.ROCK:
			if player2 == Choice.PAPER:
				return -1, 1
			if player2 == Choice.SCISSORS:
				return 1, -1

		elif player1 == Choice.PAPER:
			if player2 == Choice.ROCK:
				return 1, -1
			if player2 == Choice.SCISSORS:
				return -1, 1

		else:
			if player2 == Choice.ROCK:
				return -1, 1
			if player2 == Choice.PAPER:
				return 1, -1

		return 0, 0

	def play():
		player1 = Choice(random.randint(1, 4))
		player2 = Choice(random.randint(1, 4))

		p1_payoff, p2_payoff = get_payoff(player1, player2)

		game_history.append((player1, player2))

		p1_overall_payoff = p1_overall_payoff + p1_payoff
		p2_overall_payoff = p2_overall_payoff + p2_payoff
