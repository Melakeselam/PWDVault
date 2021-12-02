import mysql.connector

mysqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yeamanuel0108"
)

db = "PWDvault"
dbcursor = mysqldb.cursor()


def setupDb():
    dbcursor.execute("DROP SCHEMA IF EXISTS {}".format(db))
    dbcursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(db))
    dbcursor.execute("USE {}".format(db))

# dbcursor.execute("SHOW DATABASES")

# for x in mycursor:
#     print(x)


def dropTables():
    dbcursor.execute("DROP TABLE IF EXISTS Credentials")
    dbcursor.execute("DROP TABLE IF EXISTS Hosts")
    dbcursor.execute("DROP TABLE IF EXISTS Categories")
    dbcursor.execute("DROP TABLE IF EXISTS Platforms")

# platform : Online, Local, Remote\
# type: Website, Email, BankAccount, CreditCard, Application
# pwd_retention : in days


def createTables():
    specialChars = "'!''\"#$%&()*+,-./:;<=>?@[\]^_`{|}~'"

    dbcursor.execute(
        "CREATE TABLE IF NOT EXISTS Platforms (\
            id CHAR(3) PRIMARY KEY, \
            name VARCHAR(254) NOT NULL, \
            description VARCHAR(254));")
    dbcursor.execute(
        "CREATE TABLE IF NOT EXISTS Categories (\
            platform_prefix CHAR(3) NOT NULL, \
            type VARCHAR(20) NOT NULL, \
            description VARCHAR(254), \
            pwd_retention_days INT NOT NULL DEFAULT 90, \
            CONSTRAINT PK_Category PRIMARY KEY (platform_prefix, type), \
            CONSTRAINT FK_Category_Platform FOREIGN KEY (platform_prefix) \
                REFERENCES Platforms(id)); ")
    dbcursor.execute(
        "ALTER TABLE Categories ADD INDEX (platform_prefix);")
    dbcursor.execute(
        "ALTER TABLE Categories ADD INDEX (type);")
    dbcursor.execute(
        "CREATE TABLE IF NOT EXISTS Hosts (\
            id INT PRIMARY KEY AUTO_INCREMENT, \
            platform CHAR(3) NOT NULL, \
            categType VARCHAR(20) NOT NULL, \
            host_name VARCHAR(254) NOT NULL, \
            url_address VARCHAR(254), \
            category_id INT, \
            pwd_size INT NOT NULL DEFAULT 8, \
            pwd_min_num_req INT NOT NULL DEFAULT 0, \
            pwd_min_upper_req INT NOT NULL DEFAULT 0, \
            pwd_min_special_req INT NOT NULL DEFAULT 0, \
            pwd_special_req VARCHAR(254) NOT NULL DEFAULT {});".format(specialChars))
    dbcursor.execute(
        "ALTER TABLE Hosts ADD INDEX (platform);")
    dbcursor.execute(
        "ALTER TABLE Hosts ADD INDEX (categType);")
    dbcursor.execute(
        "ALTER TABLE Hosts \
            ADD CONSTRAINT FK_Host_Category_Platform \
                FOREIGN KEY (platform) \
                REFERENCES Categories(platform_prefix); \
        ")
    dbcursor.execute(
        "ALTER TABLE Hosts \
            ADD CONSTRAINT FK_Host_Category_Type \
                FOREIGN KEY (categType) \
                REFERENCES Categories(type);")
    dbcursor.execute(
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


def insertIntoTable(table, fields, values):
    valInsert = "%s"
    for x in range(len(values)-1):
        valInsert = valInsert + ", %s"
    sql = "INSERT INTO {} ({}) VALUES ({})".format(table, fields, valInsert)
    dbcursor.execute(sql, values)
    mysqldb.commit()


def clearTable(table):
    dbcursor.execute("DELETE FROM {}.{}".format(db, table))
    mysqldb.commit()


def deleteByField(table, field, value):
    sql = "DELETE FROM {}.{} WHERE {} = %s".format(db, table, field)
    print(sql)
    dbcursor.execute(sql, [value])
    mysqldb.commit()


def deleteByFields(table, fields, values):
    whereClause = "WHERE "
    size = len(fields)
    for i in range(size):
        whereClause = whereClause + "{} = %s"
        if i + 1 < size:
            whereClause + " AND "
    whereClause.format(fields)

    sql = "DELETE FROM {}.{} {}".format(db, table, whereClause)
    print(sql)
    dbcursor.execute(sql, values)
    mysqldb.commit()


def findByFieldInTable(table, field, value):
    sql = "SELECT * FROM {}.{} WHERE {} = %s".format(db, table, field)
    dbcursor.execute(sql, [value])
    result = []
    for r in dbcursor:
        result.append(r)
    return result


def findAllInTable(table):
    dbcursor.execute(
        "SELECT * FROM {}.{} ".format(db, table))
    result = []
    for r in dbcursor:
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


def startPersistence():
    setupDb()
    # dropTables()
    createTables()
