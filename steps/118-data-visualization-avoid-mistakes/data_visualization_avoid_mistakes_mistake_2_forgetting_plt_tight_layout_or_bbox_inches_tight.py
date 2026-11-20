import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_xlabel("A very long label that gets cut off at the edge of the saved image")
fig.savefig("plot.png")  # X-axis label is cropped


fig.savefig("plot.png", bbox_inches="tight")
