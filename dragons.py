def hero(bullets, dragons):
    mult = 2
    if (dragons * mult) <= bullets:
        return True
    else:
        return False