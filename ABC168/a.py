N = input()

x = N[len(N)-1]

hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]
bon = [3]

if int(x) in hon:
    print("hon")

elif int(x) in pon:
    print("pon")

else:
    print("bon")
