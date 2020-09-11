import random
 
def story1():
 print("They say my school is haunted; my (adjective) friend (name) says (he or she) saw a (adjective) (noun) floating at the end of the hall near the cafeteria.Some say if you (verb) down that hallway at night you'll hear a (animal) (verb-ing) (adverb) my (adjective) friend (name) saw a (adjective) (noun) (verb-ing) I hope I never see any (plural noun) (verb-ing);eating lunch there is scary enough! ")
 print("")
 adjective = input("Enter adjective: ")
 he_or_she = input("Enter He or She: ")
 name = input("Enter freinds name: ")
 adjective2 = input("Enter a adjective: ")
 noun = input("Enter a noun: ")
 verb = input("Enter a verb: ")
 animal = input("Enter a animal: ")
 verb2 = input("Enter a verb: ")
 adverb = input("Enter a adverb: ")
 adjective3 = input("Enter a adjective: ")
 noun2 = input("Enter a noun: ")
 verb3 = input("Enter a verb: ")
 plural_noun = input("Enter a plural noun: ")
 verb4 = input("Enter a verb: ")

 print("")
 print("They say my school is haunted; my (" + adjective + ") friend (" + name + ") says (" + he_or_she + ") saw a (" + adjective2 + ") (" + noun + ") floating at the end of the hall near the cafeteria.Some say if you (" + verb + ") down that hallway at night you'll hear a ("+ animal + verb2 + adverb + ") my (" + adjective + ") freind (" + name + ") saw a (" + adjective3 + noun2 + verb3 + ") I hope I never see any (" + plural_noun + verb4 + "); eating lunch there is scary enough! ")
 
def story2():
 print("yesterday (person) and I went to the park.On our way to do the park (adjective) (noun) on a bike. We also saw (adjective5). ballons tied to a  (noun4) once we got the (adjective) park sky turned (adjective).It started to (verb) (person) and I all the way home.Tomorrow we will try to the (adjective)park again and hope it doesn't (verb) ")
 print("")
 person = input("Enter a person: ")
 adjective4 = input("Enter a adjective: ")
 noun3 = input("Enter a noun: ")
 adjective5 = input("Enter a adjective: ")
 noun4 = input("Enter a noun: ")
 adjective6 = input("Enter a adjective: ")
 adjective7 = input("Enter a adjective: ")
 verb = input("Enter a verb: ")
 adjective8 = input("Enter a adjective: ")
 verb2 = input("Enter a verb: ")
 print("")
 print("yesterday (" + person + ") and I went to the park.On our way to do the park  (" + adjective4 + noun3 + ") on a bike. We also saw (" + adjective5 + "). ballons tied to a  (" + noun4 + ") once we got the (" + adjective6 + ") park sky turned (" + adjective7 + ").It started to (" + verb + ") (" + person + ") and I all the way home.Tomorrow we will try to the (" + adjective8 + ") park again and hope it doesn't (" + verb2 + ") ")
def randomStory():
  randomNumber = random.randint(1,2)
  if randomNumber == 1:
   story1()
  else:
   story2()
 
def storyPicker(c):
 if c == "1":
   story1()
 elif c == "2":
   story2()
 elif c == "R" or c == "r":
   randomStory()
  
def main():
 print("Welcome to my Mad Lib stories!!")
 print("")
 print("Choose a story")
 print("")
 storyChoice = input("Enter 1, 2, or (R)andom: ")
 print("")
 storyPicker(storyChoice)
 
if __name__ == "__main__":
 main()

