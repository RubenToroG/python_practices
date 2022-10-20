def run():
    my_list = [1, 'hola', True, 4.56]
    my_dict = {"firstname": "Ruben", "lastname": "Toro"}

    super_list = [
        {"firstname": "Ruben", "lastname": "Toro"},
        {"firstname": "Paula", "lastname": "Gutierrez"},
        {"firstname": "Manuel", "lastname": "Octavio"},
        {"firstname": "Oscar", "lastname": "Rod"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4],
        "integer_nums": [-1, -2, 0],
        "floating_nums": [1.2, 3.56, 4.23]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()