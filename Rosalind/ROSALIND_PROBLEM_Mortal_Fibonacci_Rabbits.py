numMonths = int(input("number of months n: "))
#numOffspring = int(input("number of offspring k: ")) 
life_expectancy = int(input("life expectancy in months: "))


def MortalFibR(numMonths, life_expectancy):
    living = [1,1]    
    for i in range(2, numMonths):
        temp = living[i - 1] + living[i - 2]
        if i == life_expectancy:
            temp = temp - 1 
        if i > life_expectancy:
            temp = temp - living[i - life_expectancy - 1]
        living.append(temp)
    return living[-1]

print(MortalFibR(numMonths, life_expectancy))







#def fibR(numMonths: int, numOffspring: int):
#    if numMonths == 1:
#        return 1
#    elif numMonths == 2:
#        return 1
#    elif numMonths == 3:
#        return numOffspring + 1
#    else:
#        oneGenback = fibR(numMonths - 1, numOffspring)
#        twoGenback = fibR(numMonths - 2, numOffspring)
#        return twoGenback*numOffspring + oneGenback
    

    
#def deadFibR(numMonths: int, life_expectancy: int):
#    if numMonths <= life_expectancy:
#        return 0
#    else:
#        dead_rabbits = 2**(numMonths - 4)
#        return dead_rabbits
#last: int = 0 
#    next: int = 1
#   for _ in range(1, n):
#       last = next
#       next = last*numOffspring + next
#   return next

#print(fibR(numMonths, numOffspring)-deadFibR(numMonths, life_expectancy))