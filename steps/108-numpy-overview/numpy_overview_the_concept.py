import numpy as np

scores = np.array([0.12, 0.87, 0.45, 0.92, 0.33, 0.78])
threshold = 0.5

mean = (scores[scores > threshold] ** 2).mean()  # Filter, square, average, all at C speed
print(f"{mean:.4f}")  # 0.7372
