#!/usr/bin/env python

#initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'colonial.settings'
import django
django.setup()


#regular imports
import home.models as hmod
import psycopg2
import sys








# #User
# for data in [
# 	[ "AdminFirst", "AdminLast", "adminP", "admin1", False, 1 ],
# 	[ "ManagerFirst", "ManagerLast", "managerP", "manager1", False, 1 ],
# 	[ "AgentFirst", "AgentLast", "agentP", "agent1", False, 1 ],
#     [ "BakerFirst", "BakerLast", "bakerP", "baker1", False, 1 ],
#     [ "CooperFirst", "CooperLast", "cooperP", "cooper1", False, 1],
#     [ "Customer1First", "Customer1Last", "customerP", "customer1", False, 1 ],
#     [ "Customer2First", "Customer2Last", "customerP", "customer2", False, 1 ],
# 	[ "Dustin", "Belliston", "dustinP", "dustin1", False, 2 ],
# 	[ "Izzy", "Beh", "izzyP", "izzy1", False, 2 ],
# 	[ "Derek", "Brimley", "derekP", "derek1", False, 3 ],
# 	[ "John", "Blackburn", "johnP", "john1", False, 4 ],
# 	[ "Kelly", "Blackburn", "kellyP", "kelly1", False, 5 ],
# 	[ "Kalli", "Belliston", "kalliP", "kalli1", False, 6 ],
# 	[ "George", "Washington", "georgeP", "george1", False, 7 ],
# 	[ "Nathan", "Hale", "nathanP", "nathan1", False, 8 ],
# 	[ "Otto", "Scorzeny", "ottoP", "otto1", False, 9 ],
# 	[ "Erwin", "Rommel", "erwinP", "erwin1", False, 10 ],
# 	[ "George", "Patton", "georgeP", "georges1", False, 11 ],
# 	[ "Omar", "Bradley", "omarP", "omar1", False, 12 ],
    
# ]:

#####Permissions#####
#auth_group
# for data in [
#     ["admin"],
#     ["manager"],
#     ["agent"]
# ]:
#     u = auth_group()
#     u.name = data[0]
#     u.save()


#Try to connect


# #####Returns Username#####
# con = None
# try:    
#     con = psycopg2.connect("dbname='colonial' user='postgres' password='kevntseeg'")   
#     cur = con.cursor()    
#     cur.execute("SELECT home_user.username FROM home_user")
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)
    
# except:
#     print("error")  
#     sys.exit(1)
       
# finally: 
#     if con:
#         con.close()
# #^^^^^Returns Username^^^^^#




con = None
try:    
    con = psycopg2.connect("dbname='colonial' user='postgres' password='kevntseeg'")   
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
    cur.execute("INSERT INTO home_user_groups VALUES(1, 1, 1)")
    cur.execute("INSERT INTO home_user_groups VALUES(2, 2, 2)")
    cur.execute("INSERT INTO home_user_groups VALUES(3, 3, 3)")

    con.commit()
    
except:
    print("error")  
    sys.exit(1)
       
finally: 
    if con:
        con.close()
















#^^^^^Permissions^^^^^#