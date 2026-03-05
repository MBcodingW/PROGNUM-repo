#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

#Choise player
player = input(r"Put in 'R' (rock), 'P' (paper) or 'S' (scissors):")

#Choise program
RPSlist = np.array(['R', 'P', 'S'])
indx = np.random.randint(0, len(RPSlist))
program = (RPSlist[indx])
print(f"The program chose:", program)
               
#Deciding who wins and who loses:
if player == program:
    print(f"It's a tie.")
elif (player == 'R' and program == 'S') or (player == 'P' and program == 'R') or (player == 'S' and program == 'P'):
    print(f"You win!")
else:
    print(f"The program wins.")

