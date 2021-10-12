import random

class Card:
	
	def __init__(self, face, value):
		self.face = face
		self.value = value

	def getValue(self):
		return self.value


	def getFace(self):
		return self.face


# Number card inherit card
class NumberCard(Card):
	def __init__(self, face):
		super().__init__(face, value=int(face))



# Face card inherit card
class FaceCard(Card):
	def __init__(self, face):
		super().__init__(face, value=10)


# Ace card inherits Card
class AceCard(Card):
	def __init__(self, face):
		super().__init__(face, value=1)


	def getOtherValue(self):
		return 11




class Deck:

	def __init__(self):
		self.allCards = []
		self.createDeck()



	def createSuit(self):
		# create number cards
		for i in range(2, 11):
			self.allCards.append(NumberCard(str(i)))

		# create face cards
		for face in ("K", "Q", "J"):
			self.allCards.append(FaceCard(face))
		
		# create ace cards
		self.allCards.append(AceCard("Ace"))


	def createDeck(self):
		for i in range(4):
			self.createSuit()


	def dealCard(self):
		# shuffle card and return last (pop from behind)
		random.shuffle(self.allCards)
		return self.allCards.pop()


	def __str__(self):
		return f"Deck has {len(self.allCards)} in deck"






