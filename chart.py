import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

def prob_of_success(N,M,p):
	success = 1
	for i in range(N):
		fails = 1
		for r in range(M):
			fails *= 1 - p
		success *= 1 - fails
	return success


dimensions = 20
prob = 0.5
heatmap = []
for n in range(dimensions):
	heatmap.append([])
	for m in range(dimensions):
		heatmap[n].append(prob_of_success(n + 1, m + 1, prob))

# create legend
handles = [Rectangle((0, 0), 1, 1, color=c, ec="k") for c in ['white', 'black']]
labels = ['0%', '100%']
plt.legend(handles, labels)

plt.xlim([0, dimensions-1])
plt.ylim([0, dimensions-1])
plt.xlabel('M (nodes per key)')
plt.ylabel('N (number of keys)')
plt.title('Probability of Success for p = ' + str(prob))
# plt.imshow(heatmap, cmap=plt.cm.get_cmap('RdYlGn'), interpolation='nearest')
plt.imshow(heatmap, cmap=plt.cm.get_cmap('Greys'), interpolation='nearest')
# plt.imshow(heatmap, cmap=plt.cm.get_cmap('inferno'), interpolation='nearest')
plt.show()
