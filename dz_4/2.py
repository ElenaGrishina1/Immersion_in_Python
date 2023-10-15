def reverse_kwargst(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(reverse_kwargst(rev=True, acc="YES", stroka=4))