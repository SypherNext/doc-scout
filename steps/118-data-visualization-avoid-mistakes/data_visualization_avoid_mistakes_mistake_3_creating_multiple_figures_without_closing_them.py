import matplotlib.pyplot as plt
import numpy as np

for i in range(100):
    fig, ax = plt.subplots()
    ax.plot(np.random.randn(100))
    # fig is never closed: 100 figures accumulate in memory!


for i in range(100):
    fig, ax = plt.subplots()
    ax.plot(np.random.randn(100))
    fig.savefig(f"plot_{i}.png")
    plt.close(fig)  # Free memory
