#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print('-' * len(Belgium))
print(Belgium.replace(',' , ':'))
bel_list = Belgium.split(',')
print(bel_list)
bel_pop = (int(bel_list[1]) + int(bel_list[3]))
print("The population of Belgium is " + str(bel_pop))

s = "{:s}: {:010d}".format("The population of Belgium is",bel_pop)
print(s)

listt = "The population of Belgium is"
s = f"{listt:s}: {bel_pop:010d}"
print(s)