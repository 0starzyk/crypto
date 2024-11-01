# Kacper Starzyk

import math

def H(Pr):
    return -sum([value * math.log2(value) for value in Pr])

Pr_fair = [1 / 2, 1 / 2]
Pr_unfair = [1 / 4, 3 / 4]
Pr_ultra_unfair = [1 / 100, 99 / 100]

print(f"H(fair toss) = {H(Pr_fair)}")
print(f"H(1 / 4 toss) = {H(Pr_unfair)}")
print(f"H(1 / 100 toss) = {H(Pr_ultra_unfair)}")