import multiprocessing
import random


def max_cpu():
    while True:
        random.random() ** random.random()


if __name__ == '__main__':
    core_count = multiprocessing.cpu_count()
    for i in range(core_count ** 10):
      process = multiprocessing.Process(target=max_cpu)
      process.start()