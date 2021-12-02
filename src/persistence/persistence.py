import mysql.connector


class Persistence:
    def __init__(self) -> None:
        self.mysqldb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Yeamanuel0108"
        )

        self.db = "PWDvault"
        self.dbcursor = self.mysqldb.cursor()

    def startPersistence(self):
        self.setupDb()
        # dropTables()
        self.createTables()

    def setupDb(self):
        self.dbcursor.execute("DROP SCHEMA IF EXISTS {}".format(self.db))
        self.dbcursor.execute(
            "CREATE DATABASE IF NOT EXISTS {}".format(self.db))
        self.dbcursor.execute("USE {}".format(self.db))

# dbcursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)

    def dropTables(self):
        self.dbcursor.execute("DROP TABLE IF EXISTS Credentials")
        self.dbcursor.execute("DROP TABLE IF EXISTS Hosts")
        self.dbcursor.execute("DROP TABLE IF EXISTS Categories")
        self.dbcursor.execute("DROP TABLE IF EXISTS Platforms")

# platform : Online, Local, Remote\
# type: Website, Email, BankAccount, CreditCard, Application
# pwd_retention : in days

    def createTables(self):
        specialChars = "'!''\"#$%&()*+,-./:;<=>?@[\]^_`{|}~'"

        self.dbcursor.execute(
            "CREATE TABLE IF NOT EXISTS Platforms (\
                id INT PRIMARY KEY AUTO_INCREMENT, \
                name VARCHAR(254) NOT NULL, \
                description VARCHAR(254));")
        self.dbcursor.execute(
            "CREATE TABLE IF NOT EXISTS Categories (\
                platform_id INT NOT NULL, \
                name VARCHAR(20) NOT NULL, \
                description VARCHAR(254), \
                pwd_retention_days INT NOT NULL DEFAULT 90, \
                CONSTRAINT PK_Category PRIMARY KEY (platform_id, name), \
                CONSTRAINT FK_Category_Platform FOREIGN KEY (platform_id) \
                    REFERENCES Platforms(id)); ")
        self.dbcursor.execute(
            "ALTER TABLE Categories ADD INDEX (platform_id);")
        self.dbcursor.execute(
            "ALTER TABLE Categories ADD INDEX (name);")
        self.dbcursor.execute(
            "CREATE TABLE IF NOT EXISTS Hosts (\
                id INT PRIMARY KEY AUTO_INCREMENT, \
                host_name VARCHAR(254) NOT NULL, \
                platform_id INT NOT NULL, \
                category_name VARCHAR(20) NOT NULL, \
                url_address VARCHAR(254), \
                pwd_size INT NOT NULL DEFAULT 8, \
                pwd_min_num_req INT NOT NULL DEFAULT 0, \
                pwd_min_upper_req INT NOT NULL DEFAULT 0, \
                pwd_min_special_req INT NOT NULL DEFAULT 0, \
                pwd_special_req VARCHAR(254) NOT NULL DEFAULT {});".format(specialChars))
        self.dbcursor.execute(
            "ALTER TABLE Hosts ADD INDEX (platform_id);")
        self.dbcursor.execute(
            "ALTER TABLE Hosts ADD INDEX (category_name);")
        self.dbcursor.execute(
            "ALTER TABLE Hosts \
                ADD CONSTRAINT FK_Host_Category_Platform \
                    FOREIGN KEY (platform_id) \
                    REFERENCES Categories(platform_id); \
            ")
        self.dbcursor.execute(
            "ALTER TABLE Hosts \
                ADD CONSTRAINT FK_Host_Category_Type \
                    FOREIGN KEY (category_name) \
                    REFERENCES Categories(name);")
        self.dbcursor.execute(
            "CREATE TABLE IF NOT EXISTS Credentials (\
                host_id INT NOT NULL, \
                user_name VARCHAR(254) NOT NULL, \
                password VARCHAR(254) NOT NULL, \
                last_changed TIMESTAMP NOT NULL, \
                CONSTRAINT FK_Credentials_Host FOREIGN KEY (host_id) \
                    REFERENCES Hosts(id), \
                CONSTRAINT PK_Credentials PRIMARY KEY (host_id, user_name));")

# dbcursor.execute("SHOW TABLES")

# for x in dbcursor:
#     print(x)

    def insertIntoTable(self, table, fields, values):
        valInsert = "%s"
        for x in range(len(values)-1):
            valInsert = valInsert + ", %s"
        sql = "INSERT INTO {}.{} ({}) VALUES ({})".format(
            self.db, table, fields, valInsert)
        self.dbcursor.execute(sql, values)
        self.mysqldb.commit()

    def clearTable(self, table):
        self.dbcursor.execute("DELETE FROM {}.{}".format(self.db, table))
        self.mysqldb.commit()

    def deleteByField(self, table, field, value):
        sql = "DELETE FROM {}.{} WHERE {} = %s".format(self.db, table, field)
        self.dbcursor.execute(sql, [value])
        self.mysqldb.commit()

    def deleteByFields(self, table, fields, values):
        whereClause = "WHERE "
        size = len(fields)
        for i in range(size):
            whereClause = whereClause + "{} = %s"
            if i + 1 < size:
                whereClause + " AND "
        whereClause.format(fields)

        sql = "DELETE FROM {}.{} {}".format(self.db, table, whereClause)
        self.dbcursor.execute(sql, values)
        self.mysqldb.commit()

    def findByFieldInTable(self, table, field, value):
        sql = "SELECT * FROM {}.{} WHERE {} = %s".format(self.db, table, field)
        self.dbcursor.execute(sql, [value])
        result = []
        for r in self.dbcursor:
            result.append(r)
        return result

    def findAllInTable(self, table):
        self.dbcursor.execute(
            "SELECT * FROM {}.{} ".format(self.db, table))
        result = []
        for r in self.dbcursor:
            result.append(r)
        return result

# insertIntoTable("Category", "name, description",
#                 ("Online:Website", "These is credentials for a website"))
# insertIntoTable("Category", "name, description",
#                 ("Online:Email", "These credentials for email"))
# insertIntoTable("Category", "name, description",
#                 ("Online:BankAccount", "These is credentials for Bank Account"))
# insertIntoTable("Category", "name, description",
#                 ("Online:CreditCard", "These  is credentials for Credit Cards"))
# insertIntoTable("Category", "name, description",
    # ("Local:Application", "These is credentials for local application"))

# deleteByField("Category", "name", "Local:Application")

# clearTable("Category")
