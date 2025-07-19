# https://www.codewars.com/kata/5601409514fc93442500010b
def better_than_average(class_points, your_points):
    # Your code here
    avg = (sum(class_points) + your_points) / (len(class_points) + 1)
    if your_points > avg:
        return True
    else:
        return False
