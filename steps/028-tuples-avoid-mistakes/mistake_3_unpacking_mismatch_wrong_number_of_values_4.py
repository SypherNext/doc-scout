model, year, score, _ = record  # OK: ignore "production"
model, year, *rest = record     # OK: rest = [0.95, "production"]
