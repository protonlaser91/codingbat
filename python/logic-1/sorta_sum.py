# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 
# inclusive, are forbidden, so in that case just return 20.
def sorta_sum(a, b):
    return a + b if not(a+b) in range(10,20) else 20
