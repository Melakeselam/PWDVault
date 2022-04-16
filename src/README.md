### NOTES:

1. The user should login with a username and password
   User: {
      id: int,
      first_name: varchar(25),
      last_name: varchar(25),
      username: varchar(25),
      password: varchar(16),
      security_question_1: varchar(254),
      sq_answer_1: varchar(254),
      security_question_2: varchar(254),
      sq_answer_2: varchar(254),
      security_question_3: varchar(254),
      sq_answer_3: varchar(254)
   }

2. When the app starts it should notify of expiring and expired passwords, and provide access to rectify - 
   a. Search the system for expired and expiring pwds and show the user for each host. 
   b. generate new pwd on request
   c. once the pwd is updated on the host, update the status on the db

3. To help the user search for credentials of a host, the hosts should be arranged by category -> host name

4. When the user provides a host name like gmail, should check if the host exists and display the credentials. If multiple credentials exist for the host name, it should display additional attributes for each credentials to help make choice

5. Once the credential for a host is displayed, the user should have a choice to update any of the hosts' mutable attributes including generating new pwd

3. At sometime there should be a random search feature based on user key words

1. Add extra layer of fault tolerance by backing up the db after every session

1. platforms:

   1. _**online_public**_: connecting via http/https protocol

   1. _**online_private**_: connecting via vpn

   1. _**local**_: on premis machine like laptop - host not online, like login to laptop

   1. _**hybrid**_: both online and local

1. categories:

   1. financial: banks, credit cards, crypto apps

   1. website: regular websites that need access, they serve information

   1. application: a tool that is used for performing some task, such as mysql or sql server

   1. educational: udemy, edx, MIU, that is used to provide educational content

   1. vault: used to store secret information

   1. file: access to an encrypted file

   1. service_portal: aws, azure, college_student_portals, appartment_portals, all used to access service

   1. email_storages: credentials for accessing personal emails and cloud storages

1. _**credentials**_:

   1. attribute: user_id, user_name, password, category

1. _**domain models**_:
   Platform{id: int, name: varchar(20), description: 'this is an online platform'}
   Category{id: 1, name: 'finance', descritpion: 'financial websites', pwd_retention_in_hours: '137784', platform_id: 1}
