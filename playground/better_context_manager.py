import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time()
    yield
    print("Elapsed: ", time.time() - start)


with timer():
    time.sleep(1)
