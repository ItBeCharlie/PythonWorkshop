# Commenting

# Talk about indenting and colons
def main():
    sep = '='*10

    # Println

    print(sep, 0, sep)

    print('Hello World')  # No need for ;

    # Print

    print(sep, 1, sep)

    print('Hello', end='')
    print('World')

    # Change end in python

    print(sep, 2, sep)

    print('Hello World', end='!\n')

    # Seperator

    # Default end='\n', sep=' '

    print(sep, 3, sep)

    print('Hello', 'World')

    # Change Seperator

    print(sep, 4, sep)

    print('Hello', 'World', sep='$$$')

    # Division

    print(sep, 5, sep)

    print(5 // 2)

    print(5 % 2)

    print(5 / 2)

    # Boolean types

    print(sep, 6, sep)

    print(True)
    print(False)
    print(None)  # Python null

    # Boolean statements

    print(sep, 7, sep)

    print(True and True)
    print(True and False)
    print(False and False)

    print(True or True)
    print(True or False)
    print(False or False)

    print(not True)
    print(not False)


main()
