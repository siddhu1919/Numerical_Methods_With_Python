def roots():
    """
    Finds the first positive and negative values of x that satisfy the equation x^3 - 4x - 9 = 0.

    Returns:
        tuple: A tuple containing lists of first negative and positive values of x, respectively.
    """
    #x**3 - 4 * x - 9
    equation = lambda x: x**3-3*x + 1
    x_values = []
    first_negative = None
    first_positive = None

    # Search for the first negative value
    i1 = 0
    temp1 = 0

    while equation(i1):
        if equation(i1) > 0:
            first_positive = i1
            temp1 = i1
            while temp1 :
                if equation(temp1) < 0:
                    first_negative = temp1
                    break
                else:
                    temp1 -= 1
            break
        else:
            i1 += 1
        if first_positive is None or first_negative is None:
            i1 = 0
            while equation(i1):
                if equation(i1) < 0:
                    first_positive = i1
                    temp1 = i1
                    while temp1 :
                        if equation(temp1) > 0:
                            first_negative = temp1
                            break
                        else:
                            temp1 -= 1
                    break
                else:
                    i1 += 1

    print(first_positive)
    print(first_negative)

    # Search for the first positive value
    

# Example usage:
# negative_root, positive_root = roots()
# print("First negative value of x:", negative_root)
# #print("First positive value of x:", positive_root)

roots()