input = """
Time:        41     96     88     94
Distance:   214   1789   1127   1055"""

input2 = """Time:      7  15   30
Distance:  9  40  200"""


#time,distance
def getTimeCombos(timePair):
	times = []
	for i in range(timePair[0]):
		#as the time held is increased, calc total dist traveled
		#i = current speed. timePair[0]-i = time travel
		dist = i * (timePair[0]-i)
		print(dist)
		if dist > timePair[1]:
			times.append(i)
	print(">",times)
	return times

#manually entered
timelist = [[41,214],[96,1789],[88,1127],[94,1055]]
print(timelist)


total = 1
for t in timelist:
	times = getTimeCombos(t)
	total = total * len(times)
print (total)


