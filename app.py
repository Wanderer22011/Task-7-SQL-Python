'''Docstring-this is a python + sql program that can pick up information about anything in the database involving planes.
By Wilson Tong on the 02/05/24 '''

#Imports
import sqlite3

#Constants and variables
DATABASE="Task7Database.db"


#Functions
def print_all_aircraft():
    '''Prints the results nicely'''
    db=sqlite3.connect(DATABASE)
    cursor= db.cursor()
    sql="SELECT * FROM Planes;"
    cursor.execute(sql)
    results=cursor.fetchall()
    #Loop the results
    print("name                          speed   max_g   climb   range   payload")
    for final in results:
        print(f"{final[1]:<30}{final[2]:<8}{final[3]:<8}{final[4]:<8}{final[5]:<8}{final[6]:<8}")
    #Loop finishes here
    db.close()

def show_all_aircraft_sorted_by_speed():
    '''Prints the results nicely'''
    db=sqlite3.connect(DATABASE)
    cursor= db.cursor()
    sql="SELECT * FROM Planes ORDER BY speed DESC;"
    cursor.execute(sql)
    results=cursor.fetchall()
    #Loop the results
    print("name                          speed")
    for final in results:
        print(f"{final[1]:<30}{final[2]:<8}")
    #Loop finishes here
    db.close()

def Show_all_aircrafts_sorted_by_climb_rate():
    '''Prints the results nicely'''
    db=sqlite3.connect(DATABASE)
    cursor= db.cursor()
    sql="SELECT * FROM Planes ORDER BY climbrate DESC;"
    cursor.execute(sql)
    results=cursor.fetchall()
                    #Loop the results
    print("name                         climb")
    for final in results:
        print(f"{final[1]:<30}{final[3]:<8}")
                    #Loop finishes here
    db.close()

def Show_all_aircrafts_sorted_by_Max_G():
    '''Prints the results nicely'''
    db=sqlite3.connect(DATABASE)
    cursor= db.cursor()
    sql="SELECT * FROM Planes ORDER BY max_g DESC;"
    cursor.execute(sql)
    results=cursor.fetchall()
                    #Loop the results
    print("name                         max_g")
    for final in results:
        print(f"{final[1]:<30}{final[3]:<8}")
                    #Loop finishes here
    db.close()

def Show_all_aircrafts_sorted_by_range():
    '''Prints the results nicely'''
    db=sqlite3.connect(DATABASE)
    cursor= db.cursor()
    sql="SELECT * FROM Planes ORDER BY range DESC;"
    cursor.execute(sql)
    results=cursor.fetchall()
                    #Loop the results
    print("name                         range")
    for final in results:
        print(f"{final[1]:<30}{final[3]:<8}")
                    #Loop finishes here
    db.close()

def Show_all_aircrafts_sorted_by_payload():
    '''Prints the results nicely'''
    db=sqlite3.connect(DATABASE)
    cursor= db.cursor()
    sql="SELECT * FROM Planes ORDER BY payload DESC;"
    cursor.execute(sql)
    results=cursor.fetchall()
                    #Loop the results
    print("name                         payload")
    for final in results:
        print(f"{final[1]:<30}{final[3]:<8}")
                    #Loop finishes here
    db.close()


#Main code
while True:
    user_input= input("What would you like to?\n 1. Show all aircraft\n 2. Show all aircraft sorted by speed\n 3.Show all aircrafts sorted by climb rate\n 4.Show all aircrafts sorted by max G force\n 5.Show all aircrafts sorted by range\n 6.Show all aircrafts sorted by weapons payload\n 7.Exit\n ")
    if user_input=="1":
        print_all_aircraft()
        
    elif user_input=="2":
        show_all_aircraft_sorted_by_speed()
        
    elif user_input=="3":
        Show_all_aircrafts_sorted_by_climb_rate()
        
    elif user_input=="4":
        Show_all_aircrafts_sorted_by_Max_G()  

    elif user_input=="5":
        Show_all_aircrafts_sorted_by_range()
    
    elif user_input=="6":
        Show_all_aircrafts_sorted_by_payload()
        
    elif user_input=="7":
        break
    else:
         print("Invalid! Please choose a number shown on the options!")