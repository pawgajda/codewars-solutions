# https://www.codewars.com/kata/57403b5ad67e87b5e7000d1d
def bubble(lst):
    result = []

    for i in range(len(lst)):
        swapped = False
        
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                swapped = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
                # save list snapshot after each swap
                # we need to use .copy() to create a new object
                # otherwise we would reference the same object all the time
                result.append(lst.copy())

        # break out of the loop if there were no swaps in recent inner loop run
        if swapped is False:
            break

    return result
