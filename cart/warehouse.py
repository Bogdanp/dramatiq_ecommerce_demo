import random
import time


class Warehouse:
    @classmethod
    def prepare(cls, *skus):
        for sku in skus:
            time.sleep(1)

        if random.randint(0, 9) < 3:
            raise RuntimeError("The warehouse system is down.")
