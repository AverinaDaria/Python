def palindrome(data):
    a = 0
    l = len(data)-1
    for sym in data:
        if sym != data[l]:
            print("False")
            a = 1
            break
        l = l-1
    if a == 0:
        print("True")

palindrome("anna")

