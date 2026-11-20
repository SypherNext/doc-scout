from itertools import zip_longest
for model, score in zip_longest(models, scores, fillvalue="N/A"):
    print(f"{model}: {score}")
# gpt-4: 0.95
# claude-3: 0.91
# N/A: 0.87
# N/A: 0.88
