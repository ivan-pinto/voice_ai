
def choose(query):
    """
    Just return result as string
    :return: result if success, False if fail
    """
    try:
        query = query.replace("calculate", "")
        result = "that's difficult to calculate"

        if '+'  in query:
            x = query.split("+")
            a = float(x[0])
            b = float(x[1])
            result = a + b
        if '-' in query:
            x = query.split("-")
            a = float(x[0])
            b = float(x[1])
            result = a - b
        if '*' in query:
            x = query.split("*")
            a = float(x[0])
            b = float(x[1])
            result = a * b
        if '/' in query:
            x = query.split("/")
            a = float(x[0])
            b = float(x[1])
            result = a / b
        

    except Exception as e:
        print(e)
        result = False
    return result

if __name__ == "__main__":
    print(choose("calculate 2 + 2"))

