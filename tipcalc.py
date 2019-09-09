def tipcalc(subtotal,tip):   
    # convert % value to decimal value
    tip_pct = float(tip) * 0.01

    #calculate the tip amount
    tip_amt = subtotal * tip_pct

    # print tip amount
    return(tip_amt)

def main():
    #prompt the user for meal subtotal
    subtotal = input("Meal subtotal: ")
    subtotal = float(subtotal)

    # prompt the user for tip %
    tip_pct = input("Tip %: ")

    tip = tipcalc(subtotal,tip_pct)

    print(tip)


if __name__ == '__main__':
    main()
