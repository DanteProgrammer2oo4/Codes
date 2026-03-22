import numpy as np
# filtering = refers to the process of selecting elements from an array that match a given condition

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])

teenagers = ages[ages<18]
adults = ages[(ages >= 18) & (ages < 65)] # numpy written by C so its works with C operators
seniors = ages[ages >= 65]
evens = ages[ages %2 == 0]
odds = ages[ages %2 != 0]
print(seniors)
print()
adults = np.where(ages >= 18 , ages , 0)
#                condition    array  fill value also np.nan or -1 can be used
print(adults)