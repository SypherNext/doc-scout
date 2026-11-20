import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Object-oriented interface
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, label="sin(x)", color="blue", linewidth=2)
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.set_title("Sine Wave")
ax.legend()
ax.grid(True, alpha=0.3)

plt.show()
# To save instead of showing: fig.savefig("sine.png", dpi=150)
