import time
i = 0
size = 5
while True:
    i = i + 1 if i < size else 0
    buffer = str()
    buffer += " ["
    for j in range(size):
        if i == j:
            buffer += "█"
        else:
            buffer += " "
    buffer += "]  Loading..."
    print(buffer, end="\r")
    time.sleep(0.2)