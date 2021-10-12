from card import Deck
from hand import Hand



class Game:
	UNKNOWN = "?"

	def __init__(self):		
		self.deck = Deck()
		self.player = Hand()
		self.dealer = Hand()
		self.endGame = False


	# initiate cards to both player and dealer
	def initCards(self):

		# dealer is hit by two cards
		self.dealer.hit(self.deck.dealCard())
		self.dealer.hit(self.deck.dealCard())

		# player is hit by two cards
		self.player.hit(self.deck.dealCard())
		self.player.hit(self.deck.dealCard())


	def showInit(self):
		d1, d2 = self.dealer.cards[0], self.dealer.cards[1]
		p1, p2 = self.player.cards[0], self.player.cards[1]
		print(f"Dealer has: {d1.getFace()} {self.UNKNOWN} = {self.UNKNOWN}")
		print(f"Player has: {p1.getFace()} {p2.getFace()} = {self.player.getTotalPoints()}")
		


	# character is of type Hand
	def showCards(self, characterName, character):
		print(f"{characterName} has: ", end = "")
		for card in character.getCards():
			print(card.getFace(), end = " ")

		print(f"= {character.getTotalPoints()}")


	# run until stand, won, or busted
	def playerMove(self):
		
		# if player is lucky and just wins right away
		if self.player.checkWin():
			print("Player Wins")
			print("Blackjack")
			hasWon = True
			self.endGame = True  # whole game has ended
			return

		hasStand = False
		hasWon = False
		hasBusted = False
		MESSAGE = "Would you like to (H)it or (S)tand? "
		while not hasStand and not hasWon and not hasBusted:
			# prompt user
			usrInput = input(MESSAGE)

			# if HIT
			if usrInput == "H":
			
				self.player.hit(self.deck.dealCard())

				# show cur situation 
				self.showCards("Player", self.player)


				# check busted
				if self.player.checkBusted():
					print(f"Player busts with {self.player.getTotalPoints()}")
					print("Dealer Wins")
					hasBusted = True
					self.endGame = True

				# check won
				if self.player.checkWin():
					print("Player Wins")
					print("Blackjack")
					hasWon = True
					self.endGame = True  # whole game has ended
			# If STAND, break out while loop
			elif usrInput == "S":
				hasStand = True

			else:
				print("Invalid Input. Input (H)it or (S)tand! ")


	def revealDealerHidden(self):
		###### show players score ######
		print()
		self.showCards("Player", self.player)
		print()
		###### show dealer score ######
		self.showCards("Dealer", self.dealer)


	# dealer hits until score >= 17 --> end
	# if bust game over, player wins
	def dealerMove(self):
		while self.dealer.getTotalPoints() < 17:
			print("Dealer hits")
			
			self.dealer.hit(self.deck.dealCard())
			
			if self.dealer.checkBusted():
				self.showCards("Dealer", self.dealer)
				print("Player Wins!")
				self.endGame = True
				break

			self.showCards("Dealer", self.dealer)


		if not self.endGame:
			print("Dealer stands")


	def revealResult(self):
		self.showCards("Player's", self.player)
		self.showCards("Dealer's", self.dealer)
		
		
	def reportWinner(self):
		player_total = self.player.getTotalPoints()
		dealer_total = self.dealer.getTotalPoints()

		if  player_total > dealer_total:
			print("Player Wins!")
		
		elif player_total == dealer_total:
			print("Game is a tie")

		else:
			print("Dealer wins")


		# print result
		self.revealResult()



	def mainProcess(self):
		# deal init cards
		self.initCards()
		

		# display hands
		self.showInit()


		# player moves
		self.playerMove()


		# dealer moves
		if not self.endGame:
			self.dealerMove()

		# report winner
		if not self.endGame:
			self.reportWinner()














