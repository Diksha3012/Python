def raise_to_power(base_no,power_no):
    result =1
    for i in range(power_no):

        result = result * base_no
        print(result)
    print(result)



print(raise_to_power(3,5))