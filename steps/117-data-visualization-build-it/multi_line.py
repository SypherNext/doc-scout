import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, np.sin(x), label="sin", linestyle="-", color="blue")
ax.plot(x, np.cos(x), label="cos", linestyle="--", color="red")
ax.plot(x, np.sin(x) * np.cos(x), label="sin*cos", linestyle=":", color="green")
ax.set_xlabel("x")
ax.set_ylabel("value")
ax.set_title("Trigonometric Functions")
ax.legend()
fig.savefig("trig.png", dpi=150, bbox_inches="tight")
