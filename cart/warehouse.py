import random
import time


class Warehouse:
    @classmethod
    def prepare(cls, *skus):
        for sku in skus:
            if random.randint(0, 9) < 3:
                raise RuntimeError("The warehouse system is down.")

            time.sleep(1)
