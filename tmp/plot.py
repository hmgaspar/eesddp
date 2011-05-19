import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.broken_barh([ (0, 3) ] , (10, 9), facecolors='blue')
ax.broken_barh([ (3, 2)] , (20, 9),
            )
ax.set_ylim(5,35)
ax.set_xlim(0,6)
ax.set_xlabel('seconds since start')
ax.set_yticks([15,25])
ax.set_yticklabels(['Contract 2', 'Contract 1'])
ax.grid(True)

plt.show()
