# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#assignment 1
scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"

#assignment 2 
goal_0 = 32
goal_1 = 54

#asssigment 3
scorers = scorer_1 + " " + str(goal_0) + "," + " " + scorer_2 + " " + str(goal_1)
print(scorers)

report = f"{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute"
print(report)

#PART 2

#assignment 1
player ="Frank Rijkaard"

#assignmnet 2

first_name_player = player.find(" ")
first_name = player[:first_name_player]
print(first_name)

#assignment 3
last_name_player = player.find(" ")
last_name= player[last_name_player+1:]
last_name_len= len(last_name)
print(last_name_len)
 

#assignment 4
name_short = (first_name[0] + "." + " " + last_name)
print(name_short)

#assignment 5
chant_name = (first_name + "! ") * len(first_name) #chant + ! and space
chant = chant_name.rstrip()
print(chant)

#assignment 6
good_chant= chant[-1] != " "
print(good_chant)


