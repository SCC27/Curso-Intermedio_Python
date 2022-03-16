def run():
    # squares = []
    # squares3 = []
    # for i in range(1, 101):
    #     squares.append(i**2)

    # for i in range(1, 101) :
    #     if (i%3 !=0):
    #         squares3.append(i**2)
    
    # print(squares)
    # print(squares3)

    #squares = [i**2 for i in range(1, 101) if i% 3 !=0 ]

    #print(squares)

    divisible =[i  for i in range (1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0  ] 
    print(divisible)
if __name__ == '__main__':
    run()