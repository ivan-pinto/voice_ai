import wikipedia 

def search_wikipedia(query):
    """
    Just return wikipedia search as string
    :return: results if success, False if fail
    """
    try:
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
    except Exception as e:
        print(e)
        results = False
    return results