# https://www.codewars.com/kata/5a622f5f85bef7a9e90009e2
def reverse_fizzbuzz(st):
    # convert input string to a list for convenience
    st_lst = st.split()
    print(st_lst)
    
    # guess helper variables
    digit_index = -1
    digit_value = -1
    
    # look for a first digit in the input sequence
    for i, v in enumerate(st_lst):
        if v.isdigit():
            digit_index = i
            digit_value = int(v)
            # first match is all I need, let's break free
            break

    # if digit was found in the input sequence
    if digit_index != -1 and digit_value != -1:
        # list to store our generated sequence
        guessed_seq = []
        # generate the whole number sequence based on found number
        for j in range(len(st_lst)):
            if j < digit_index:
                guessed_seq.append(digit_value - (digit_index - j))
            elif j == digit_index:
                guessed_seq.append(digit_value)
            else:
                guessed_seq.append(digit_value + (j - digit_index))
        
        print(guessed_seq)
        return guessed_seq
    
    # good luck
    else:
        # start the fizz buzz sequence from 0
        # so list index will match underlying value
        # for example [0, 1, 2, 3, 4, 5] = [0, 1, 2, "Fizz", 4, "Buzz"]
        fizz_buzz = [0]
        # magic number, sophisticated guess
        fizz_buzz_max = 99
        
        # generate fizz buzz list
        for k in range(1, fizz_buzz_max + 1):
            if k % 3 == 0 and k % 5 == 0:
                fizz_buzz.append("FizzBuzz")
            elif k % 3 == 0:
                fizz_buzz.append("Fizz")
            elif k % 5 == 0:
                fizz_buzz.append("Buzz")
            else:
                fizz_buzz.append(str(k))
        
        st_len = len(st_lst)
        start, stop = 0, 0
        # look for our sequence in fizz buzz list
        for l in range(len(fizz_buzz) - st_len + 1):
            if fizz_buzz[l:l+st_len] == st_lst:
                start, stop = l, l + st_len
                # we got a match!
                break
        
        print(fizz_buzz[start:stop])
        # generate answer
        gen_seq = [m for m in range(start, stop)]
        print(gen_seq)
        return gen_seq
