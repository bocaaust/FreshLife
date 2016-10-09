import sqlite3
from fetch_price import *

'''
def fetch_sorted_list():
    return []    

def fetch_cals( user):
    return 2000

def fetch_current_list( user ):
    return ['Cheetos','Eggs','Beer']

def fetch_nut_value( food ):
    return (20,30,40)

def fetch_values_sorted_fat():
    return []
def generate_healthier_list( user ):
    req_cals = fetch_cals( user )
    req_carb = 0.55 * req_cals
    req_fat = 0.25 * req_cals
    req_prot = 0.2 * req_cals
    
'''         
def fetch_food(c):
    c.execute("SELECT Name FROM Nutrition")
    ret = []
    d = c.fetchall()
    for a in d:
        ret.append(a[0])
    return ret

def update_cost( c, i,d):
    c.execute("UPDATE Nutrition SET Cost = %s WHERE name ='%s'"%(d,i))
     
    

conn = sqlite3.connect('database.db')
c = conn.cursor()
a = fetch_food(c)
for i in a:
    print(i)
    d = Fetch_Price(i)
    update_cost(c,i,d)

print(a)
conn.commit()
conn.close()
