import features.date         as f_date
import features.wikipedia    as f_wkp
import features.joke         as f_j
import features.stm32_serial as f_stm
import features.weather      as f_w
import features.music        as f_m
import features.calc         as f_c
import webbrowser            as wb







class Assistant:

    ###BROWSER

    def search_wikipedia(self, query):
        """
        Just return wikipedia search as string
        :return: results if success, False if fail
        """
        return f_wkp.search_wikipedia(query)

    def open_youtube(self):
        wb.open("youtube.com")

    def open_google(self):
        wb.open("google.com")

    ###DATE

    def tell_me_date(self):
        """
        Just return date as string
        :return: str/Bool
            date if success, False if fail
        """
        return f_date.date()

    def tell_me_time(self):
        """
        Just return date as string
        :return: str/Bool
            date if success, False if fail
        """
        return f_date.time()

    def tell_me_hour(self):
        """
        Just return date as string
        :return: str/Bool
            date if success, False if fail
        """
        return f_date.hour()
    
    ###WEATHER

    def weather(self, query):
        """
        Just return weather for determinate city
        :return: results if success, False if fail
        """
        return f_w.weather(query)

    ###STM

    def stm_command(self, query):
        """
        :return: result if success, False if fail
        """
        return f_stm.choose(query)


    ###FUN

    def tell_joke(self):
        """
        Just return joke as string
        :return: str/Bool
            joke if success, False if fail
        """
        return f_j.joke()

    ###MUSIC
    def play_song_pc(self):
        """
        Just starts play a song
        :return: results true success, False if fail
        """
        return f_m.play_song_pc()
    
    ###CALC
    def calc(self, query):
        """
        Make a calculation
        :return: results if success, False if fail
        """
        return f_c.choose(query)

    ###WISHME
    def wish_me(self):
        hour = int(f_date.hour())
        if hour >= 7 and hour < 12:
            return ("good morning, i am your virtual assistant")
        elif hour >= 12 and hour < 18:
            return ("good afternoon, i am your virtual assistant")
        else:
            return ("good night, i am your virtual assistant")
    
    ###WAKE
    def wake(self, query):
        if 'hey daisy' in query:
            return True
        else:
            return False
    
    ###Sleep
    def sleep(self):
        return False
        
