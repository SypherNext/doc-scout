import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Fragile: modifies the global figure state
plt.plot(x, y)
plt.xlabel("x")
plt.title("My Plot")
plt.show()  # Which figure is this showing?


fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("x")
ax.set_title("My Plot")
fig.savefig("plot.png")
