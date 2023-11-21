k = int(input("Input number of homozygous dominant individuals k: "))
m = int(input("Input number of heterozygous individuals m: "))
n = int(input("Input number of homozygous recessive individuals n: "))
pop_size = k + m + n
print("Population size: ", pop_size)

prob_XX_XX = (k/pop_size) * ((k - 1)/(pop_size - 1))
prob_XX_Xx = (k/pop_size) * (m/(pop_size - 1))
prob_XX_xx = (k/pop_size) * (n/(pop_size - 1))

prob_Xx_XX = (m/pop_size) * (k/(pop_size - 1))
prob_Xx_Xx = (m/pop_size) * ((m - 1)/(pop_size - 1))
prob_Xx_xx = (m/pop_size) * (n/(pop_size - 1))

prob_xx_XX = (n/pop_size) * (k/(pop_size - 1))
prob_xx_Xx = (n/pop_size) * (m/(pop_size - 1))
prob_xx_xx = (n/pop_size) * ((n - 1)/(pop_size - 1))

prob1 = prob_XX_XX + prob_XX_Xx + prob_XX_xx
prob2 = prob_Xx_XX + prob_Xx_Xx*0.75 + prob_Xx_xx*0.5
prob3 = prob_xx_XX + prob_xx_Xx*0.5 + prob_xx_xx*0


print(prob1 + prob2 + prob3)
