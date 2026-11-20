import dis

def with_loop():
    result = []
    for n in range(1000):
        if n % 2 == 0:
            result.append(n * 2)
    return result

def with_comp():
    return [n * 2 for n in range(1000) if n % 2 == 0]

# Compare bytecode
print("=== Loop ===")
dis.dis(with_loop)
print("\n=== Comprehension ===")
dis.dis(with_comp)
