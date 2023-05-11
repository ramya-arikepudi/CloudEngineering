def shopping_with_for_loop():
    my_shopping_list = {"Banana": 0.50,"Apple": 0.25,"Mango": 3.00}
    print(f'Price of apple:{my_shopping_list["Apple"]}')
    shopping_list_keys = my_shopping_list.keys()
    print(shopping_list_keys)
    print(type(shopping_list_keys))
    x = 1.5
    print(type(x))
    # y = int(x)
    # print(y)
    # print(type(y))
    # q = float(y)
    # print(q)
    # print(type(q))
    # price = "10.5"
    # my_int_price = float(price)
    # print(my_int_price)
    # float_price = 25.28
    # int_price = int(float_price)
    # print(int_price)
    for item in shopping_list_keys:
        #print(item)
        #(my_shopping_list.get(item))
        print(f'Item: {item} price:{my_shopping_list.get(item)}')


shopping_with_for_loop()

