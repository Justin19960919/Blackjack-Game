class Hand:
	BUST_LIMIT = 21
	
	def __init__(self):
		self.totalPoints = 0
		self.aceCount = 0
		self.cards = []


	def getCards(self):
		return self.cards


	# add card to hand
	def hit(self, card):
		if card.getFace() == "Ace":
			self.aceCount += 1
		else:
			self.totalPoints += card.getValue()

		# add card to list
		self.cards.append(card)


	# test func
	# get optimal value
	# only executes this function if hand has aces
    # creates the greatest non-busted hand value
	def getOptimalValue(self):
		
		# inner function
		# if ace: 3 --> 3, 13, 23, 33
		def getAllPossibilities(numberOfAces):
			return range(self.aceCount, self.aceCount + 10 * 5, 10)

		
		# check initial (if even if we add minimum it will bust, then just return )
		if self.totalPoints + self.aceCount > self.BUST_LIMIT:
			return self.totalPoints + self.aceCount
		
		# get closest value to 21
		# otherwise
		maxPoints = self.totalPoints
		for p in getAllPossibilities(self.aceCount):
			if self.totalPoints + p > self.BUST_LIMIT:
				break

			else:
				maxPoints = max(self.totalPoints + p, maxPoints)


		return maxPoints


	def getTotalPoints(self):
		if self.aceCount == 0:
			return self.totalPoints
		else:
			return self.getOptimalValue()


	def checkBusted(self):
		return self.getTotalPoints() > self.BUST_LIMIT


	def checkWin(self):
		return self.getTotalPoints() == self.BUST_LIMIT


	# for tests
	def setter(self, tp, ac):
		self.totalPoints = tp
		self.aceCount = ac




