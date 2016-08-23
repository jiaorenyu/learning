from param import counter


def add():
    global counter
    counter += 1

if __name__ == "__main__":
    print(counter)
    add()
    print(counter)

