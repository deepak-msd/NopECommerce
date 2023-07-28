import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        ActURL = config.get("common info", "baseURL")
        return ActURL

    @staticmethod
    def getUseremail():
        Actemail = config.get("common info", "useremail")
        return Actemail

    @staticmethod
    def getPassword():
        ActPassword = config.get("common info", "password")
        return ActPassword




