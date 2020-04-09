import matplotlib.pyplot as plt


fig = plt.figure(figsize=[15, 15])
fig.patch.set_facecolor((.8, 1, 1))

ax = fig.add_subplot(111)

#img = plt.imread('bgi.png')
#ax.imshow(img)
# draw the grid
for x in range(4):
    ax.plot([100 + x * 400, 100 + x * 400], [100, 1300], color = '#08445D', linewidth = 5)
for y in range(4):
    ax.plot([100, 1300], [100 + y * 400 , 100 + y * 400], color = '#08445D', linewidth = 5)

# scale the axis area to fill the whole figure
ax.set_position([0, 0, 1, 1])

# get rid of axes and everything (the figure background will show through)
ax.set_axis_off()

# scale the plot area conveniently (the board is in 0,0..18,18)

#plt.savefig("board1.png", format = "png", bbox_inches = "tight", transparent = True, dpi = 600)
plt.savefig("board1.png", format = "png", transparent = True, dpi = 60)
#plt.show()
