import sqlite3
from fetch_price import *

def fetch_list(c, user):
    c.execute("SELECT Current_List FROM User WHERE Name = ?",user)
    return c.fetchone()

def fetch_cost(c, prod):
    print(prod)
    c.execute("SELECT Cost FROM Nutrition WHERE Name ='%s'"%prod)
    d=c.fetchone()
    if(d == None):
        return 0
    return d[0]

def fetch_user(c):
    c.execute("SELECT Name from User")
    return c.fetchone()

def fetch_values_sorted_fat(c):
    c.execute("SELECT Name FROM Nutrition ORDER BY Fat")
    ret = []
    d = c.fetchall()
    for a in d:
        ret.append(a[0])
    return ret

def generate_healthier_list( c, user ):
#    req_cals = fetch_cals( user )
#    req_carb = 0.55 * req_cals
#    req_fat = 0.25 * req_cals
#    req_prot = 0.2 * req_cals
    vals = fetch_list(c, user)
    vals = vals[0].split(",")
    print(vals)
    sm =0
    for i in vals:
        sm = sm + float(fetch_cost(c,i))
    
    d = fetch_values_sorted_fat(c)
    msm =0
    ret = []
    for i in  d:
        if ( msm + int(fetch_cost(c,i)) < sm):
            msm = msm + int(fetch_cost(c,i))
            ret.append(i)
        else:
            break   
    return  ret

def update_healthier_list (c, user,  val):
    myList = ','.join(map(str, val))
    c.execute("UPDATE User SET Healthy_List = '%s' WHERE Name ='%s'"%(myList,user[0]))

def fetch_food(c):
    c.execute("SELECT Name FROM Nutrition")
    ret = []
    d = c.fetchall()
    for a in d:
        ret.append(a[0])
    return ret

def update_cost( c, i,d):
    c.execute("UPDATE Nutrition SET Cost = %s WHERE Name ='%s'"%(d,i))
     
    

conn = sqlite3.connect('database.db')
c = conn.cursor()
#a = fetch_food(c)
#for i in a:
#    print(i)
#    d = Fetch_Price(i)
#    update_cost(c,i,d)

#conn.commit()
user = fetch_user(c)
ll = generate_healthier_list(c,user)
update_healthier_list(c, user, ll)
conn.commit()
conn.close()
