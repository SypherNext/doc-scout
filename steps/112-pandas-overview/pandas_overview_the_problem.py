import csv

with open("results.csv") as f:
    rows = list(csv.DictReader(f))

avg_by_model = {}
for r in rows:
    if float(r["accuracy"]) == 0:
        continue
    model = r["model"]
    if model not in avg_by_model:
        avg_by_model[model] = []
    avg_by_model[model].append(float(r["accuracy"]))

result = {m: sum(v)/len(v) for m, v in avg_by_model.items()}
