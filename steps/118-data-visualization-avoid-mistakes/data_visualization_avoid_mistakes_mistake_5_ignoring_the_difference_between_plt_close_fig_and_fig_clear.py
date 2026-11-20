import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# ... draw ...
fig.clear()   # Removes the axes but keeps the figure object: hidden memory
plt.close(fig)  # Fully releases the figure resources
