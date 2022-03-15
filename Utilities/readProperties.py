import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url
    
    @staticmethod
    def getUserEmail():
        username = config.get('common info','username')
        return username

    @staticmethod
    def getUserPassword():
        pwd = config.get('common info','password')
        return pwd

class ReadTitlePage:
    @staticmethod
    def getTitleM6():
        title = config.get('titre page chaine','m6')
        return title

    @staticmethod
    def getTitleW9():
        title = config.get('titre page chaine','w9')
        return title

    @staticmethod
    def getTitle6ter():
        title = config.get('titre page chaine','6ter')
        return title

    @staticmethod
    def getTitleguilli():
        title = config.get('titre page chaine','guilli')
        return title

    @staticmethod
    def getTitleteva():
        title = config.get('titre page chaine','teva')
        return title

    @staticmethod
    def getTitleparis_premiere():
        title = config.get('titre page chaine','paris_premiere')
        return title
    
    @staticmethod
    def getTitleLelive():
        title = config.get('titre page chaine','le_live')
        return title
    
    @staticmethod
    def getTitleHomePage():
        title = config.get('titre page chaine','home_page')
        return title