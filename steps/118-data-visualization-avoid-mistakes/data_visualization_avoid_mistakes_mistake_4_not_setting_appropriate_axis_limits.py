import matplotlib.pyplot as plt

data = [0.92, 0.95, 0.88, 0.96, 0.91]
fig, ax = plt.subplots()
ax.plot(data)
# Default y-axis limits are [0.87, 0.97]
# Small changes look dramatic because the axis starts near the data


ax.set_ylim(0, 1.0)  # Full range for percentages
# Or use a consistent range across subplots
