import time
import random


def waiting_game():
    target = random.randint(2, 4)
    print('\n(...Your target time is {} seconds...)'.format(target))

    input('\n(...Press enter again after {} seconds...)'.format(target))
    start = time.perf_counter()

    input('(---Press enter to begin---)')
    elapsed = time.perf_counter() - start

    print('\nElapsed time: {0:.3f} seconds'.format(elapsed))
    if elapsed == target:
        print('Right on!')
    elif elapsed < target:
        print('{0:.3f} seconds to fast!'.format(target - elapsed))
    else:
        print('{0:.3f} seconds to slow!'.format(target + elapsed))


waiting_game()
