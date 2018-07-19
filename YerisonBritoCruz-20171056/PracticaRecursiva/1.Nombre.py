def nombre(num):
    if num == 0:
        return "Yerison Y. Brito Cruz"
    else:
        print("Yerison Y. Brito Cruz")
        return nombre(num-1)


nombre(5)
