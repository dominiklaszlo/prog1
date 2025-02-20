import multiprocessing
import random


def max_cpu():
    while True:
        random.random() ** random.random()


if __name__ == '__main__':
    process = multiprocessing.Process(target=max_cpu)
    process.start()
