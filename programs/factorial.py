res = 1
n = 8

for i in range(1,n):
    res = res * (i+1)
print(res)

# recursive way
def fact_recursive(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return n * fact_recursive(n-1)
print(fact_recursive(8))

# fact_recursive(8)
#     ↓
# 8 × fact_recursive(7)
#           ↓
#        7 × fact_recursive(6)
#                 ↓
#              6 × fact_recursive(5)
#                       ↓
#                    5 × fact_recursive(4)
#                             ↓
#                          4 × fact_recursive(3)
#                                   ↓
#                                3 × fact_recursive(2)
#                                         ↓
#                                      2 × fact_recursive(1)

# The most important thing to understand
# Recursion has two phases:
# 1. Going DOWN

# 8
# ↓
# 7
# ↓
# 6
# ↓
# 5
# ↓
# 4
# ↓
# 3
# ↓
# 2
# ↓
# 1

# It keeps calling itself until it reaches the base case.

# 2. Coming BACK UP
# 1 → 2 → 6 → 24 → 120 → 720 → 5040 → 40320
