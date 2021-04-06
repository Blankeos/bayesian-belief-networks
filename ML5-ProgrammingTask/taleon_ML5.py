from bayesian.bbn import build_bbn

def f_outlook(outlook):
    if outlook == 'sunny':
        return 5/14
    elif outlook == 'overcast':
        return 4/14
    elif outlook == 'rainy':
        return 5/14

def f_humidity(humidity):
    return 0.5

def f_windy(windy):
    return 0.5

def f_play(outlook, humidity, windy, play):
    if outlook == humidity:  # Guest was correct!
        if outlook == windy:
            return 0     # Monty never reveals the prize
        else:
            return 0.5   # Monty can choose either goat door
    elif outlook == windy:
        return 0         # Again, Monty wont reveal the prize
    elif humidity == windy:
        return 0         # Monty will never choose the guest door
    else:
        # This covers all case where
        # the guest has *not* guessed
        # correctly and Monty chooses
        # the only remaining door that
        # wont reveal the prize.
        return 1



if __name__ == '__main__':
    g = build_bbn(
        f_outlook,
        f_humidity,
        f_windy,
        f_play,
        domains=dict(
            outlook=('sunny','overcast','rainy'),
            humidity=('high', 'normal'),
            windy=('true','false'),
            play=('yes', 'no')))

    print("rainy, high, and weak wind: ")
    g.q(outlook="rainy", humidity="high", wind="false")