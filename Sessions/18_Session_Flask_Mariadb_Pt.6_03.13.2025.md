# Maria DB
#### Time: 2.5 hrs

## Progress update: Example of a function we created

The function in the example does the following:

##### 1. Creates a table in the database named avengers.
##### 2. It then creates columns with that table (id (primary key), First name and Last name).
##### 3. Executes an insert commnand that adds values to the First name and Last name columns, assigned it to a variable represented as sql.
##### 4. Assigned the Values provided to a variable represented as val.
##### 5. Executes the the commands by referencing the variables.
##### 6. Executes a select all form the table command.
##### 7. prints the output screen.
##### 8. If this command were to fail at any point, execute an expection that prints "Did not work to Screen."
![image](https://github.com/user-attachments/assets/6a08d9fb-93cb-4a4d-b527-3e5023780e9f)


## 

##### We decided to look for inspiration for real execurises for the use of our MariaDB and python knowledge:

##### We came across this article inwhich the author gave  astep by step guide of how he utlized MariaDB with his flask application: https://www.cloudacode.com/tutorials/python/flask/simple-flask-app-mariadb/

##### The Architecture resembles our project structure.

 ![image](https://github.com/user-attachments/assets/643d04eb-221d-4acd-9356-bc710f4803e5)

##### This application consists of 2 docker containers 
##### 1. Hosts the application
##### 2. Hosts the MariaDB Database

##### Following the article step by step.

##### We encountered an error for container 1. 
![image](https://github.com/user-attachments/assets/64373206-13a3-449d-8727-9ba4a8af33f6)


##### From researching online: 

The errors indicate that flask_table might be the issue.

![image](https://github.com/user-attachments/assets/04167101-67bc-4155-842e-6d8226beac52)

##### This is understandable since the github repo that was cloned is 3 years old. Packages have updated thus affecting dependencies.

### Troubleshooting in progress...



