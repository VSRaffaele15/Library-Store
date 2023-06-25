import time

def Tick(
        numtick: int,
        sleeptimeframetick: float
        ):
    ticks = 0
    while not ticks == numtick:
        time.sleep(sleeptimeframetick)
        ticks += 1
    if ticks == numtick:
        return True