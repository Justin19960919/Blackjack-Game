### Blackjack ###

For my project setup, I've used main.py as my project entry point.
To start the game, simply type:
```
python3 main.py
```

and the program will start prompting user input.


##### Main #####

For this project, I only used the random module to sample data, which simulates 
shuffling of cards in a deck. In addition, I feel like the project instructions
were fairly straightforward, and it was a joy to program through this little game.


In this project, I tried to decouple the logic as much as possible, so that every 
class had its one purpose, and either used composition or inheritance to structure
my components.

If you take a quick look, you will realize I created a Cards class, which has several
classes inheriting from it, like NumberCards, FaceCards...etc. To represent a deck,
I created a Deck class to put Cards in it, which upon instantiation, generates 52 cards
in the Deck. Then, getting a card out, is just simply shuffling it, and popping out the 
last card.

For Game, it was a bit more trickier. Since I wanted my main to be as clean as possible,
I put most of the logic flow of the black jack game into Game, and used main to call it.

Game represents a class where we walk through the blackjack game step by step, and 
determine if the game has ended in every step using a class variable. In the process,
I tried to separate out the logic as much as I could, but due to the time constraints,
it could have maybe be more concise using the DRY principle.


One particular interesting aspect was to get optimized total values of all the cards,
if a hand of cards had aces in it. With that said, I took a greedy approach, while also
checking if the total value of the cards was initially 21. if that was the case, we didn't 
need to hit a card, since the player has already won. (sometimes ppl just get lucky)

This algo is a O(n) approach, so it shouldn't take much time.
Also, if we have 3 aces, then the min addition was 3, 13, 23, 33.
Similarly, if we have 4 aces, it was 4, 14, 24 ,34, 44
All a diff of 10, which makes sense, and would save additional computing time.


I wrote some small tests to test out the getTotalPoints() function in the Hands class,
which represents a Hand of cards. Given more time, I would probably go about testing the code
more, maybe via simulation or unit testing, but given 2 hours, I could only complete
the general structure and a few unit tests for the project.


##### Running Tests #####
To run tests, simply run:
```
py.test hand_test.py

```
and it will run tests on hand.getTotalPoints()

Time took:
2021 - 10 - 03
14:46 - 17:05


I took a little bit over an hour, because I had to write tests and my readme file.







