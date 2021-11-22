lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

if text.startswith("var"):
    print("Pascal")
elif text.startswith("#include"):
    print("C++")
elif text.startswith("import"):
    print("Java")
elif text.startswith("<?php"):
    print("Php")