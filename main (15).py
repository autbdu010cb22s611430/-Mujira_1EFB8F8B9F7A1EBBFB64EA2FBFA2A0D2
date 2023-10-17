#2.2 Implement a class called player that represents a  cricket player. the player class should have a method called play() which prints "the player is playing cricket.Derive two classes,Batsman and Bowler, from the player class. Overide the play() method in each derived class to print "the batsman is bating "and" the bowler is bowling", respectively  write a program to create objectsbof both the Batsman and Bowler classes and call the play() method for each object
# Define the player class
class player:
  def play(self):
      print("The player is playing cricket.")
# Define the Batsman class, derived from player
class Batsman(player) :
  def play (self) :
    print("The batsman is batting. ")
# Define the Bowler class, derived from player
class Bowler(player) :
  def play (self) :
    print ("The bowler is bowling.") 
# create objects of Batsman and Bowler classes
batsman=Batsman() 
bowler=Bowler() 
# call the play() method for object 
batsman. play () 
bowler. play() 
    
    
    

