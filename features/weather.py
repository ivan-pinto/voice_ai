import requests, json
 

# Enter your API key here
api_key = "48f9539b8d5646ea61157e1e3765135b"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def weather(query):

    """
    Just return weather for determinate city
    :return: results if success, False if fail
    """
    try:
        query = query.replace("weather", "")
        complete_url = base_url + "appid=" + api_key + "&q=" + query + "&units=metric"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
        
            # store the value of "main"
            # key in variable y
            y = x["main"]
        
            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]
        
            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]
        
            # store the value corresponding
            # to the "humidity" key of y
            current_humidity = y["humidity"]
        
            # store the value of "weather"
            # key in variable z
            z = x["weather"]
        
            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
            weather_description = z[0]["description"]
        
            # print following values
            results = (" Temperature (in celsius unit) = " +
                            str(current_temperature) +
                       " atmospheric pressure (in hPa unit) = " +
                                    str(current_pressure) +
                       " humidity (in percentage) = " +
                                    str(current_humidity) +
                       " description = " +
                                    str(weather_description))
            print(results)
        
        else:
           results= "City Not Found "
    except Exception as e:
        print(e)
        results = False
    return results
