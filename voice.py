import features.date         as f_date
import features.wikipedia    as f_wkp
import features.joke         as f_j
import features.stm32_serial as f_stm
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