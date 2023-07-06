def GravityForce(
        force: float
        ):
    return force * 8002

def JumpForce(
        force: float
        ):
    return force * 2

def High(
        a: float,
        b: float
        ):
    return a + 1 == b

def Low(
        a: float,
        b: float
        ):
    return a - 1 == b

def Founder(
        value,
        a: float,
        b: float
):
    if value >= a and value <= b:
        return True
    else:
        return False
    