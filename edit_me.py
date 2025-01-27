
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    if len(lst) <= 1:
        return True
    
    increasing = decreasing = True  # Assume both for now

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            increasing = False  
        if lst[i] > lst[i - 1]:
            decreasing = False  

    return increasing or decreasing

print(monotonic([1, 2, 3, 4]))
print(monotonic([1,0,1,0]))
# code that tests your function monotonic.
#
