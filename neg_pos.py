def neg_pos():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print(f"The number {num} is negative.")
    elif num > 0:
        print(f"The number {num}  is positive.")
    else:
        print(f"The number {num}  is zero.")

if __name__ == "__main__":
    neg_pos()