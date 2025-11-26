# https://www.codewars.com/kata/5813d19765d81c592200001a 
def dont_give_me_five(start, end):
    n = 0

    for i in range(start, end + 1):
        # base case - add every number to the count
        count = True
        # handle negative numbers by using absolute value of i
        tmp = abs(i)
        
        # take absolute value of i and check digit by digit
        # if the number i contins digit 5
        while tmp > 0:
            digit = tmp % 10
            tmp = tmp // 10
            
            # if digit 5 is found, mark number i as uncountable
            if digit == 5:
                count = False
                break
                
        # count number only if it does not contain number 5
        if count:
            n += 1
        
    return n
