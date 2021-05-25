
def star_print():
    for i in range(4):
        for j in range(4):
            print("*",end = "")
        print("\t")
    print("--------------------")
    
star_print()


def star_print_more():
    for i in range(4):
        for j in range(i+1):
            print("*",end = "")
        print("\t")
    print("--------------------")

star_print_more()


def star_print_single():
    for i in range(3):
        for j in range(1):
            print("*")
        print("\n")
    print("--------------------")
star_print_single()
