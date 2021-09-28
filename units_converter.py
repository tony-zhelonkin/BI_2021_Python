print('This is a script for converting celsius and fahrenheit degrees or pounds and kilograms')
choice = input("Please, write temp for celsius <-> fahrenheit conversion or wgt for lbs <-> kigs conversion ",)
if choice == "temp":
    start_temp = input("Please, write cel for celsius -> fahrenheit conversion or fahr for vica versa ",)
    temp_to_convert = float(input("Please, enter number to convert ",))
    if start_temp == "cel":
        result = temp_to_convert * (9 / 5) + 32
        print(temp_to_convert, "celsius equals to ", round(result, 2), " fahrenheit")
    elif start_temp == "fahr":
        result = (temp_to_convert - 32) * 5 / 9
        print(temp_to_convert, "fahrenheit equals to ", round(result, 2) , " celsius")
elif choice == "wgt":
    start_wgt = input("Please, write kig for kilogram -> lbs conversion or lbs for vica versa ", )
    wgt_to_convert = float(input("Please, enter number to convert ",))
    if start_wgt == "kig":
        result = wgt_to_convert * 2.20462262185
        print(wgt_to_convert, "kg equals to ", round(result, 2)," lbs")
    elif start_wgt == "lbs":
        result = wgt_to_convert / 0.45359237
        print(wgt_to_convert, "lbs equals to ", round(result, 2)," kg")
elif choice != "temp" or choice != "wgt":
    print("Unknown unit conversion! Please choose temp or wgt")