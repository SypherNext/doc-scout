# Line by line
with open("large_file.txt", "r", encoding="utf-8") as f:
    for line in f:
        process(line)

# Chunk by chunk
while True:
    chunk = f.read(8192)  # 8 KB at a time
    if not chunk:
        break
    process(chunk)
