# https://www.codewars.com/kata/5a86073fb17101e453000258
def sort_emotions(arr, order):
    # map emotions to numbers in descending order:
    emotion_num_map = {":D": 5, ":)": 4, ":|": 3, ":(": 2, "T_T": 1}
    # map numbers to emotion by reversing emotion_num_map
    num_emotion_map = {v: k for k, v in emotion_num_map.items()}
    # convert emotions into numbers
    numeric_emotions = [emotion_num_map[x] for x in arr]
    # sort emotions in place by requested order
    if order:
        # descending order
        numeric_emotions.sort(reverse=True)
    else:
        # ascending order
        numeric_emotions.sort(reverse=False)
    
    result = []
    for num in numeric_emotions:
                result.append(num_emotion_map[num])
    return result
    # (ง •̀_•́)ง
