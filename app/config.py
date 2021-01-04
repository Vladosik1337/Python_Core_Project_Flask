class Configuration:
    DEBUG = True  #Для того щоб не заупскати кожен раз main.py
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #Відслідковує дію перед або після запису в БД
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Vladosik15@localhost/test1'