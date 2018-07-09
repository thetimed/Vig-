#This is a code to calculate vig in betting lines
#The higher the Vig, the lousier the odds are, and that is something gamblers must be aware of

#This is the number of odds there are available 

No_of_odds = raw_input("How many odds are there?Please Enter a number:")


#Convert the answer to the number of odds

No_of_bets = int(No_of_odds)

bets = []

for x in range(No_of_bets):
	odds = raw_input("What is the odds of the " + str(x+1) + " event?")	

#Add the new data into the list
	
	bets.insert(x,odds)
	
print bets

length = len(bets)

print length

vig = []
for i in range(length):
	new_odds = 1  / float(bets[i])
	vig.insert(i,new_odds)	
		
print vig

sum = sum(vig)
	
print sum

final_vig = sum - 1 


print "The sum is %s and the vig is %s ." %(sum,final_vig)
print "Good luck"
	
#Always remember, the smaller the vig, the better it is. 

	


	

