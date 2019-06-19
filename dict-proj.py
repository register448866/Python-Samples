
phone = input("PLEASE TYPE IN SOME INTEGERS UP TO 3 DIGITS >   ")
oneplace = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine ",
    "0": "Zero "
}
abnormal = {
    "10": "Ten ",
    "11": "Eleven ",
    "12": "Twelve ",
    "13": "Thirteen ",
    "14": "Fourteen ",
    "15": "Fifteen ",
    "16": "Sixteen ",
    "17": "Seventeen ",
    "18": "Eighteen ",
    "19": "Ninteen"
}
twoplace={
    "1": " ",
    "2": "Twenty ",
    "3": "Thirty ",
    "4": "Forty ",
    "5": "Fifty",
    "6": "Sixty ",
    "7": "Seventy ",
    "8": "Eighty",
    "9": "Ninty ",
    "0": ""
}

answer = ''

if len(phone) == 1:
    answer = oneplace[phone]

if len(phone) == 2:
    if phone[0] == '1':
        answer = abnormal[phone]
    elif phone[0] == '0':
        answer = oneplace[phone[1]]
    else:
        answer = twoplace[phone[0]] + (oneplace[phone[1]]).lower()


# Print result
print(answer)