# 3077번 _ 임진왜란
import time
import sys
sys.stdin.readline
result = 0
hyunu_fight_twochoice = []
num = int(sys.stdin.readline())
correct_fight = sys.stdin.readline().split()
hyunu_fight = sys.stdin.readline().split()

for i in range(num):
  for j in hyunu_fight[i + 1:]:
    hyunu_fight_twochoice.append((hyunu_fight[i],j))

for k in range(len(hyunu_fight_twochoice)):
  nm = (hyunu_fight_twochoice[k][0])
  
  ng = correct_fight.index(nm)
  if hyunu_fight_twochoice[k][1] in correct_fight[ng:]:
    result += 1 
n= int(num*(num-1)/2)

print(result,"/",n)

