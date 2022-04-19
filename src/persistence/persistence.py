from datetime import datetime
import mysql.connector
import numpy as np
from config.configuration import Configuration
from domain.Credentials import Credentials,Status
from service.PwdGenerator import PwdGenerator as Generator


entity_tables = {
    'User': 'users',
    'Platform': 'platforms',
    'Category': 'categories',
    'Credentials': 'credentials',
    'Host': 'hosts'
}

entity_table_fields = dict(
    Platform = dict(id='id',name='name',description='description')
    ,Category = ('',)
    ,Credentials = ('',)
    ,Host = ('',)
)

class Persistence:
    def __init__(self) -> None:
        self.db_config = Configuration('database')
        self.app_config = Configuration('application')
        self.mysqldb = mysql.connector.connect(
            host=self.db_config.get('host'),
            user=self.db_config.get('username'),
            password=self.db_config.get('password')
        )

        self.db = 'pwd_vault'
        self.dbcursor = self.mysqldb.cursor()

    def startPersistence(self):
        reset = False
        populate = False
        if self.app_config.get('environment') in ['dev','stage']:
            reset=True if input('Reset DB? (y/n)') == 'y' else False
            populate=True if reset and input('Populate Table? (y/n)') == 'y' else False
        if not reset:
            self.setupDb()
        else:
            self.resetDb(reset,populate)
        # self.dropTables()


    def setupDb(self):
        self.dbcursor.execute(
            'CREATE DATABASE IF NOT EXISTS {}'.format(self.db))
        self.dbcursor.execute('USE {}'.format(self.db))

# dbcursor.execute('SHOW DATABASES')

    def resetDb(self,reset,populate):
        if reset:
            self.dbcursor.execute('DROP SCHEMA IF EXISTS {}'.format(self.db))
            self.dbcursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(self.db))
            self.dbcursor.execute('USE {}'.format(self.db))
            self.createTables()
        if populate:    
            self.populate()

    def dropTables(self):
        for table in entity_tables.values():
            self.dbcursor.execute(f'DROP TABLE IF EXISTS {table}')
    
    def populate(self):
        users_populate_map_1 = dict(
            id=1,
            first_name='John',
            last_name='Smith',
            username='john_smith',
            password='john1234',
            security_question_1='Place of Birth',
            sq_answer_1='Austin, Texas',
            security_question_2='Primary School',
            sq_answer_2='J.E.B Stuart',
            security_question_3='Child\'s Name',
            sq_answer_3='Jane' 
        )
        users_populate_map_2 = dict(
            id=2,
            first_name='Peter',
            last_name='Jenkins',
            username='peter',
            password='peter1234',
            security_question_1='Place of Birth',
            sq_answer_1='Austin, Texas',
            security_question_2='Primary School',
            sq_answer_2='J.E.B Stuart',
            security_question_3='Child\'s Name',
            sq_answer_3='Jane' 
        )
        profiles_populate_map_1 = dict(
            id=1,
            name='Online',
            description='Covers all hosts accessed via network, wether on the internet or LAN'
        )
        categories_populate_map_1 = dict(
            platform_id=1,
            name='finance',
            description='hosts that are financial in nature such as banks, credit card, etc.',
            pwd_retention_hours=90*24
        )
        categories_populate_map_2 = dict(
            platform_id=1,
            name='free-educational-tutorials',
            description='hosts that are free tutorials on skills and knowledge that contribute to professional competency',
            pwd_retention_hours=365*24
        )
        categories_populate_map_3 = dict(
            platform_id=1,
            name='paid-educational-tutorials',
            description='hosts that are paid tutorials on skills and knowledge that contribute to professional competency',
            pwd_retention_hours=365*24
        )
        categories_populate_map_4 = dict(
            platform_id=1,
            name='email',
            description='different email accounts',
            pwd_retention_hours=180*24
        )
        hosts_populate_map_1 = dict(
            user_id=1,
            id=1,
            host_name='gmail_personal',
            platform_id=1,
            category_name='email',
            address='www.gmail.com'
        )
        hosts_populate_map_2 = dict(
            user_id=1,
            id=2,
            host_name='gmail_work',
            platform_id=1,
            category_name='email',
            address='www.gmail.com',
            custom_pwd_retention_period_in_hours=60*24
        )
        hosts_populate_map_3 = dict(
            user_id=1,
            id=3,
            host_name='gmail_business',
            platform_id=1,
            category_name='email',
            address='www.gmail.com',
            custom_pwd_retention_period_in_hours=60*24
        )
        credentials_populate_map_1 = dict(
            host_id=1,
            username='smith.john',
            password=Generator.generatePassword(),
            date_created=datetime.today(),
            pwd_updated_date=datetime.today(),
            pwd_expiration_date= Credentials.calc_exp_date(datetime.today(),90 * 24),
            pwd_size=16,
            pwd_min_num_req=1,
            pwd_min_upper_req=1,
            pwd_min_special_req=1,
            pwd_special_req='#$%&',
            status=Status.ACTIVE.name
        )
        credentials_populate_map_2 = dict(
            host_id=2,
            username='peter',
            password=Generator.generatePassword(),
            date_created=datetime.today(),
            pwd_updated_date=datetime.today(),
            pwd_expiration_date= Credentials.calc_exp_date(datetime.today(),90 * 24),
            pwd_size=16,
            pwd_min_num_req=1,
            pwd_min_upper_req=1,
            pwd_min_special_req=1,
            pwd_special_req='#$%&',
            status=Status.CREATED.name
        )
        credentials_populate_map_3 = dict(
            host_id=3,
            username='lolita',
            password=Generator.generatePassword(),
            date_created=datetime.today(),
            pwd_updated_date=datetime.today(),
            pwd_expiration_date= Credentials.calc_exp_date(datetime.today(),90 * 24),
            pwd_size=16,
            pwd_min_num_req=1,
            pwd_min_upper_req=1,
            pwd_min_special_req=1,
            pwd_special_req='#$%&',
            status=Status.CREATED.name
        )

        self.insert_into_table('User',users_populate_map_1)
        self.insert_into_table('User',users_populate_map_2)
        self.insert_into_table('Platform',profiles_populate_map_1)
        self.insert_into_table('Category',categories_populate_map_1)
        self.insert_into_table('Category',categories_populate_map_2)
        self.insert_into_table('Category',categories_populate_map_3)
        self.insert_into_table('Category',categories_populate_map_4)
        self.insert_into_table('Host',hosts_populate_map_1)
        self.insert_into_table('Host',hosts_populate_map_2)
        self.insert_into_table('Host',hosts_populate_map_3)
        self.insert_into_table('Credentials',credentials_populate_map_1)
        self.insert_into_table('Credentials',credentials_populate_map_2)
        self.insert_into_table('Credentials',credentials_populate_map_3)


# platform : Online, Local, Remote\
# type: Website, Email, BankAccount, CreditCard, Application
# pwd_retention : in days

    def createTables(self):
        specialChars = "'!''\"#$%&()*+,-./:;<=>?@[\]^_`{|}~'"

        self.dbcursor.execute(
            'CREATE TABLE IF NOT EXISTS users (\
                id INT PRIMARY KEY AUTO_INCREMENT, \
                first_name VARCHAR(25) NOT NULL, \
                last_name VARCHAR(25) NOT NULL, \
                username VARCHAR(25) NOT NULL UNIQUE, \
                password VARCHAR(16) NOT NULL, \
                security_question_1 VARCHAR(254) NOT NULL, \
                sq_answer_1 VARCHAR(254) NOT NULL, \
                security_question_2 VARCHAR(254) NOT NULL, \
                sq_answer_2 VARCHAR(254) NOT NULL, \
                security_question_3 VARCHAR(254) NOT NULL, \
                sq_answer_3 VARCHAR(254) NOT NULL);')
        self.dbcursor.execute(
            'CREATE TABLE IF NOT EXISTS platforms (\
                id INT PRIMARY KEY AUTO_INCREMENT, \
                name VARCHAR(254) NOT NULL UNIQUE, \
                description VARCHAR(254));')
        self.dbcursor.execute(
            'CREATE TABLE IF NOT EXISTS categories (\
                platform_id INT NOT NULL, \
                name VARCHAR(30) NOT NULL, \
                description VARCHAR(254), \
                pwd_retention_hours INT NOT NULL DEFAULT 90, \
                CONSTRAINT PK_Category PRIMARY KEY (platform_id, name), \
                CONSTRAINT FK_Category_Platform FOREIGN KEY (platform_id) \
                    REFERENCES platforms(id)); ')
        self.dbcursor.execute(
            'ALTER TABLE categories ADD INDEX (platform_id);')
        self.dbcursor.execute(
            'ALTER TABLE categories ADD INDEX (name);')
        self.dbcursor.execute(
            'CREATE TABLE IF NOT EXISTS hosts (\
                user_id INT NOT NULL,\
                id INT PRIMARY KEY AUTO_INCREMENT, \
                host_name VARCHAR(254) NOT NULL, \
                platform_id INT NOT NULL, \
                category_name VARCHAR(20) NOT NULL, \
                address VARCHAR(254) NOT NULL, \
                custom_pwd_retention_period_in_hours INT DEFAULT 0, \
                CONSTRAINT UC_Host_Name UNIQUE (user_id, host_name));')
        self.dbcursor.execute(
            'ALTER TABLE hosts ADD INDEX (platform_id);')
        self.dbcursor.execute(
            'ALTER TABLE hosts ADD INDEX (category_name);')
        self.dbcursor.execute(
            'ALTER TABLE hosts \
                ADD CONSTRAINT FK_Host_Category_Platform \
                    FOREIGN KEY (platform_id) \
                    REFERENCES Categories(platform_id); \
            ')
        self.dbcursor.execute(
            'ALTER TABLE hosts \
                ADD CONSTRAINT FK_Host_Category_Type \
                    FOREIGN KEY (category_name) \
                    REFERENCES Categories(name);')
        self.dbcursor.execute(
            'CREATE TABLE IF NOT EXISTS credentials (\
                host_id INT NOT NULL, \
                username VARCHAR(254) NOT NULL, \
                password VARCHAR(254) NOT NULL, \
                date_created TIMESTAMP NOT NULL, \
                pwd_updated_date TIMESTAMP NOT NULL, \
                pwd_expiration_date TIMESTAMP NOT NULL, \
                pwd_size INT NOT NULL DEFAULT 8, \
                pwd_min_num_req INT NOT NULL DEFAULT 0, \
                pwd_min_upper_req INT NOT NULL DEFAULT 0, \
                pwd_min_special_req INT NOT NULL DEFAULT 0, \
                pwd_special_req VARCHAR(254) NOT NULL DEFAULT {},\
                status VARCHAR(20) NOT NULL, \
                CONSTRAINT FK_Credentials_Host FOREIGN KEY (host_id) \
                    REFERENCES hosts(id), \
                CONSTRAINT PK_Credentials PRIMARY KEY (host_id, username));'.format(specialChars))

# dbcursor.execute('SHOW TABLES')

# for x in dbcursor:
#     print(x)

    def insert_into_table(self, table, field_value_map):

        fields = ', '.join(field_value_map.keys())
        values = [*field_value_map.values()]
        value_place_holders = '%s'
        for x in range(len(values)-1):
            value_place_holders = value_place_holders + ', %s'
        sql = f'INSERT INTO {self.db}.{entity_tables[table]} ({fields}) VALUES ({value_place_holders})'
        input(sql)
        self.dbcursor.execute(sql, values)
        insert_id = self.dbcursor.lastrowid
        self.mysqldb.commit()
        return insert_id

    def update_table(self, table, set_clause_map, where_clause_map):
        values = []
        set_clause_fields = []
        where_clause_fields = []
        for field in set_clause_map.keys():
            set_clause_fields.append(f'{field} = %s')
            values.append(set_clause_map[field])
        set_clause = ', '.join(set_clause_fields)
        for condition_param in where_clause_map.keys():
            where_clause_fields.append(f'{condition_param} = %s')
            values.append(where_clause_map[condition_param])
        where_clause = ' AND '.join(where_clause_fields)
        
        sql = f'UPDATE {self.db}.{entity_tables[table]} SET {set_clause} WHERE {where_clause}'
        input(f'sql= {sql}')
        self.dbcursor.execute(sql, tuple(values))
        self.mysqldb.commit()

    def clear_table(self, table):
        self.dbcursor.execute('DELETE FROM {}.{}'.format(self.db, table))
        self.mysqldb.commit()

    def delete_by_field(self, table, field, value):
        sql = f'DELETE FROM {self.db}.{entity_tables[table]} WHERE {field} = %s'
        self.dbcursor.execute(sql, [value])
        self.mysqldb.commit()

    def delete_by_fields(self, table, field_value_map):
        fields = [field for field in field_value_map.keys()]
        values = [value for value in field_value_map.values()]
        where_clause = 'WHERE '
        size = len(fields)
 
        for i in range(size):
            where_clause += '{} = %s'
            if i + 1 < size:
                where_clause += ' AND '

        where_clause = where_clause.format(*fields)
        sql = f'DELETE FROM {self.db}.{entity_tables[table]} {where_clause}'
        self.dbcursor.execute(sql, values)
        self.mysqldb.commit()

    def find_by_field_in_table(self, table, field, value):
        sql = f'SELECT * FROM {self.db}.{entity_tables[table]} WHERE {field} = %s'
        self.dbcursor.execute(sql, [value])
        result = []
        for r in self.dbcursor:
            result.append(r)
        return result
    
    def find_by_fields_in_table(self, table, fields, values):
        where_conditions = ' AND '.join([f'{field} = %s' for field in fields])
        sql = f'SELECT * FROM {self.db}.{entity_tables[table]} WHERE {where_conditions}'
        self.dbcursor.execute(sql, values)
        result = []
        for r in self.dbcursor:
            result.append(r)
        return result

    def find_all_in_table(self, table):
        self.dbcursor.execute(
            f'SELECT * FROM {self.db}.{entity_tables[table]} ')
        result = []
        for r in self.dbcursor:
            result.append(r)
        return result

    def find_all_in_table_by_values(self, table, field, values):
        csv = ','.join([str(v) for v in values])
        where_clause = f'WHERE {field} IN ({csv})'
        sql = f'SELECT * FROM {self.db}.{entity_tables[table]} {where_clause}'
        self.dbcursor.execute(sql)
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
