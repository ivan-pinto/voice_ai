import pyjokes

def joke():
    """
    Just return joke as string
    :return: joke if success, False if fail
    """
    try:
        joke = pyjokes.get_joke()
    except Exception as e:
        print(e)
        joke = False
    return joke