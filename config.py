import mysql.connector


class credentials:    
    data_base = mysql.connector.connect(host='db4free.net',
                                        user='rootmysql',
                                        passwd='rootmysql',
                                        db='bookmyshow',
                                        port=3306)


