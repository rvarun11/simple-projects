# -*- coding: utf-8 -*-
import sqlite3

def createUsersTable():
    connection = sqlite3.connect("login.db")
    
    #connection.execute("DROP TABLE USERS")
    connection.execute("CREATE TABLE USERS(NAME TEXT NOT NULL CHECK(NAME <> ''),EMAIL TEXT PRIMARY KEY CHECK(EMAIL <> ''), PASSWORD TEXT NOT NULL CHECK(PASSWORD <> ''))")
    
    #connection.execute("INSERT INTO USERS VALUES(?,?,?)",('Varun','varun@gmail.com','123'))
    #connection.execute("UPDATE USERS SET PASSWORD = '12345' WHERE NAME = 'Rahul'") 
    connection.commit()
    
    results = connection.execute("SELECT * FROM USERS")
    for data in results:
        print(data[0])
        print(data[1])
        print(data[2])
    
    connection.close()
 
def createProductsTable():
    connection = sqlite3.connect("productsInfo.db")
    
    connection.execute("DROP TABLE PRODUCTS")
    connection.execute("CREATE TABLE PRODUCTS (P_ID TEXT PRIMARY KEY CHECK(P_ID <> ''),NAME TEXT NOT NULL CHECK(NAME <> ''),DESC TEXT NOT NULL CHECK(DESC <> ''))")
    
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p1','Nike MAGISTAX OLA II TF Football Shoes','₹3,596 - 20% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p2','Sparx SM-322 Canvas Shoes For Men','₹895 - 10% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p3','Chevit Blue Stylish Loafers','₹2540 - 15% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p4','Steve Madden Women Beige Heels','₹3149 - 30% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p5','Tommy Hilfiger Leather Wallet','₹1897 - 33% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p6','Inc.5 Women SULTAN Heels','₹1690 - 50% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p7','US POLO Solid Cotton T-Shirt','₹1399 - 25% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p8','Pepe Striped Shirt','₹1895 - 30% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p9','Provogue T-Shirt For Men','₹1595 - 10% OFF'))
    connection.execute("INSERT INTO PRODUCTS VALUES(?,?,?)",('p10','UCB Solid Cotton T Shirt','₹1225 - 35% OFF'))
    
    connection.commit()
    
    
    results = connection.execute("SELECT * FROM PRODUCTS")
    for data in results:
        print(data[0])
        print(data[1])
        print(data[2])
        
    connection.close()
     
#createUserTable()
createProductsTable()