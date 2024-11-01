# Kacper Starzyk

import math

def H(Pr):
    return -sum([value * math.log2(value) for value in Pr])

random_key_probabilities = [0.5 for _ in range(128)]
print(f"128 bit key uniform number entrophy: {H(random_key_probabilities)}")

n = 100
random_key_probabilities = [0.5 for _ in range(n)]
print(f"{n} bit key uniform number entrophy: {H(random_key_probabilities)}")

# Entropia dla losowego klucza przy jednorodnym rozkładzie wynosi: liczba_bitów / 2