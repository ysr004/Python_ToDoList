import random 
import sys 

class NumberGuessingGame: 
  def __init__(self, min_num=1, max_num=100):
    self.min_num = min_num
    self.max_num = max_num
    self.secret_number = None 
    self.attempts = 0 
    self.high_score = float('inf')
  
  def generate_number(self):
      """Generate a new random number"""
      return random.randint(self.min_num, self.max_num)
  
  def show_welcome(self):
     """Display ewelcome message and instructions"""
     print(f"\n{'⭐'* 10} NUMBER GUESSING GAME {'⭐' * 10}")
     print(f"I'm thinking of a number {self.min_num} to {self.max_num} and {self.max_num}")
     print("Can you guess what it is ?\n")

  def play_game(self):
     """Main game loop""" 
     self.secret_number = self.generate_number()
     self.attempts = 0 

     while True:
        try:
           guess = int(input(f"Guess #{self.attempts + 1}: "))
        except ValueError:
           print("Please enter a valid number!")
           continue 

        self.attempts += 1 

        if guess < self.secret_number:
           print("Too low! Try higher number.")
        elif guess > self.secret_number:
           print("Too high! Try a lower number.")
        else:
           print(f"\n 🎆 Congratulation ! You guessed it in {self.attempts} attempts!")

           if self.attempts < self.high_score: 
              self.high_score = self.attempts
              print("🏆 New High Score!")

           break

  def play_again(self):
     """Ask if player wants to play again"""
     while True:
        choice = input("\nWould you like to play again ?  (y/n): ").lower()
        if choice == 'y': 
           return True
        elif choice == 'n':
           return False
        else: 
           print("Please enter 'y' or 'n' ")

  def show_score(self):
     """Display the current high score"""
     if self.high_score == float('inf'):
        print(f"\nYour best score this session: {self.high_score} attempts")
     else:
        print("\nYou haven't set a high score yet!")

  def run(self):
     """Main game controller"""
     self.show_welcome()
     self.play_game()
     self.show_score()


     if not self.play_again():
        print("\nThanks for playing! Goodbye!")
        sys.exit()

if __name__=="__main__":
   game = NumberGuessingGame()
   game.run()
