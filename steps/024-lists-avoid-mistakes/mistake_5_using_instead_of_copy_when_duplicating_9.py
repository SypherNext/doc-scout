original = [1, 2, 3]
copied = original        # ❌ This is a reference, not a copy
copied.append(4)
print(original)          # [1, 2, 3, 4]: original changed
