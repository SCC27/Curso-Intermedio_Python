def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"fistname":"Facundo", "lastname": "Garcia"}

    super_list=[
        {"fistname":"Facundo", "lastname": "Garcia"},
        {"fistname":"Miguel", "lastname": "Torres"},
        {"fistname":"Pepe", "lastname": "Rodelo"},
        {"fistname":"Susana", "lastname": "Martinez"},
        {"fistname":"Jose", "lastname": "Garcia"},
    ]

    super_dic={
        "natural_num":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }

    for key, value in super_dic.items():
        print(key, "-", value)
    

if __name__ == '__main__':
    run()