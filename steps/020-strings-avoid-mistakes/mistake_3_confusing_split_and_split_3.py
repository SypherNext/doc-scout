line = "a  b   c"  # Multiple spaces between words
print(line.split())      # ['a', 'b', 'c']: splits on any whitespace
print(line.split(' '))   # ['a', '', 'b', '', '', 'c']: splits on single space
