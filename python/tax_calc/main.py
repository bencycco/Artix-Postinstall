def main():
    untaxed = input('How much money is earned without tax? ')
    untaxed = int(untaxed)

    tax(untaxed)


def tax(x):
    taxable = x - 12500
    if x < 37700:
        income = taxable * 0.8
    elif x > 37700 and x < 125140:
        income = taxable * 0.6
    elif x > 125140:
        income = taxable * 0.55
        
    print(f"You would have earned £{income + 12500}")

main()
