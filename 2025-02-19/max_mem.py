import threading


def max_mem():
    stress = []
    for i in range(1000000):
        stress.append(" " * 10 ** 6)
    print("Max memory usage: ", len(stress), "MB")


if __name__ == "__main__":
    thread = threading.Thread(target=max_mem)
    thread.start()
