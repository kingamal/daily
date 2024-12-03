def neg_pos():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("The number is negative.")
    elif num > 0:
        print("The number is positive.")
    else:
        print("The number is zero.")

if __name__ == "__main__":
    neg_pos()