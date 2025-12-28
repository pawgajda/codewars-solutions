# https://www.codewars.com/kata/57d307fb9d84633c5100007a
def range_parser(s):
    result = []

    # convert input string to a list: ['1-10', '14', '20-25:2']
    for r in s.replace(" ", "").split(","):
        # if we got a number, just add it to the result: '14'
        if r.isdecimal():
            result.append(int(r))
        # otherwise keep paring the entry
        else:
            # get the range
            elements = r.split("-")
            
            # check if we have step or not
            if len(elements[1].split(":")) == 2:
                # we got stop:step to parse here: '25:2'
                subrange = elements[1].split(":")
                start, stop, step = int(elements[0]), int(subrange[0]), int(subrange[1])
            # there was no step to parse: '1-10'
            else:
                start, stop, step = int(elements[0]), int(elements[1]), 1
            
            # generate the list from the parsed range and add it to our result
            result += list(range(start, stop + 1, step))
            
    return result
