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

from django.db import connection
from django.contrib.auth.models import Group, Permission, ContentType
import subprocess


cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])
cursor.close()


#Address
for data in [	
	[ "100 Default", "Default", "AK", "99654" ],
	[ "25 E 900 N", "Provo", "Utah", "84604" ],
	[ "1250 E 800 N", "Provo", "Utah", "84604" ],
	[ "700 N 789 E", "Provo", "Utah", "84604" ],
	[ "880 S 4673 W", "Provo", "Utah", "84604" ],
	[ "880 S 4673 W", "Provo", "Utah", "84604" ],
	[ "25 E 900 N", "Provo", "Utah", "84604" ],
	[ "456 Victory", "Langley", "Virginia", "34652" ],
	[ "575 OneLife", "New York", "New York", "42566" ],
	[ "1 Greif ", "Malmedy", "Germany", "55624" ],
	[ "132 North Africa", "Calais", "Virginia", "77485" ],
	[ "584 Bulge St", "West Point", "Virginia", "84733" ],
	[ "89 N 89 S", "Providence", "Rhode Island", "68556" ],
]:
	a = hmod.Address()
	a.address1 = data[0]
	a.city = data[1]
	a.state =[2]
	a.zip = data[3]
	a.save()	


#User
for data in [
	[ "AdminFirst", "AdminLast", "adminP", "admin1", False, 1, "group13chf@gmail.com", '801-423-1428', "What is the answer to the universe?", "41" ],
	[ "ManagerFirst", "ManagerLast", "managerP", "manager1", False, 1, "manager@chf.com", '801-423-1428', "What is the answer to the universe?", "41" ],
	[ "AgentFirst", "AgentLast", "agentP", "agent1", False, 1, "agent@chf.com",'801-423-1428', "What is the answer to the universe?", "41"],
    [ "BakerFirst", "BakerLast", "bakerP", "baker1", False, 1, "baker@chf.com",'801-423-1428', "What is the answer to the universe?", "41"],
    [ "CooperFirst", "CooperLast", "cooperP", "cooper1", False, 1, "cooper@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
    #5
    [ "Customer1First", "Customer1Last", "customerP", "customer1", False, 1, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
    [ "Customer2First", "Customer2Last", "customerP", "customer2", False, 1, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Dustin", "Belliston", "dustinP", "dustin1", False, 2, "dustinbelliston@gmail.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Izzy", "Beh", "izzyP", "izzy1", False, 2, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Derek", "Brimley", "derekP", "derek1", False, 3, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	#10
    [ "John", "Blackburn", "johnP", "john1", False, 4, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Kelly", "Blackburn", "kellyP", "kelly1", False, 5, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Kalli", "Belliston", "kalliP", "kalli1", False, 6, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "George", "Washington", "georgeP", "george1", False, 7, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Nathan", "Hale", "nathanP", "nathan1", False, 8, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	#15
    [ "Otto", "Scorzeny", "ottoP", "otto1", False, 9, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Erwin", "Rommel", "erwinP", "erwin1", False, 10, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "George", "Patton", "georgeP", "georges1", False, 11, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],
	[ "Omar", "Bradley", "omarP", "omar1", False, 12, "default@chf.com", '801-423-1428', "What is the answer to the universe?", "41"],   
]:
    u = hmod.User()
    u.first_name = data[0]
    u.last_name = data[1]
    u.set_password(data[2])
    u.username = data[3]
    u.is_superuser = data[4]
    u.address_id = data[5]
    u.email = data[6]
    u.phone = data[7]
    u.security_question = data[8]
    u.security_answer = data[9]

    u.save()



#####Permissions#####
##Code from Carter Hesterman
# Permission.objects.all().delete()
# Group.objects.all().delete()
# permission = Permission()
# permission.codename = 'manager_rights'
# permission.content_type = ContentType.objects.get(id=7)
# permission.name = 'Has Manager Rights'
# permission.save()
# group = Group()
# group.name = "Managers"
# group.save()
# group.permissions.add(permission)
# print('permissions initialized')


con = None
try:    
    con = psycopg2.connect("dbname='colonial' user='postgres' password='password'")   
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")

    #Create 3 groups
    cur.execute("INSERT INTO auth_group VALUES(1,'admin')")
    cur.execute("INSERT INTO auth_group VALUES(2,'manager')")
    cur.execute("INSERT INTO auth_group VALUES(3,'agent')")
    
    #Give the 3 groups the permissions
    cur.execute("INSERT INTO auth_group_permissions VALUES(1, 1, 1)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(2, 1, 2)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(3, 1, 3)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(4, 2, 2)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(5, 2, 3)")
    cur.execute("INSERT INTO auth_group_permissions VALUES(6, 3, 3)")

    #Update the permissions that where generated
    cur.execute("UPDATE auth_permission SET name='admin level', codename='admin' WHERE id='1'")
    cur.execute("UPDATE auth_permission SET name='manager level', codename='manager' WHERE id='2'")
    cur.execute("UPDATE auth_permission SET name='agent level', codename='agent' WHERE id='3'")
    
    #Update the first content type to be [home.%]
    cur.execute("UPDATE django_content_type SET name='colonial', app_label='home', model='colonial' WHERE id='1'")

    #Put the first three users into the groups
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




################################Start Inserting an image
# def readImage():

#     try:
# 	    fin = open("shop-placeholder.png","rb")
# 	    img = fin.read()
# 	    return img
        
#     except:

        
#         sys.exit(1)

#     finally:
        
#         if fin:
#             fin.close()


# try:
#     con = psycopg2.connect(database="colonial", user="postgres", password="password") 
    
#     cur = con.cursor()
#     data = readImage()
#     binary = psycopg2.Binary(data)
#     cur.execute("INSERT INTO PHOTOGRAPH VALUES (01/01/2015, Colonial Heritage Event, '1', %s)", (binary,) )

#     con.commit()    
    
# except:

#     if con:
#         con.rollback()

#     print   
#     sys.exit(1)
    
# finally:
    
#     if con:
#         con.close() 
###################################End Inserting an image


#Photograph
for data in [
    [ '2015-01-01', "Colonial Event", 1, "1.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "2.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "3.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "4.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "5.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "6.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "7.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "8.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "9.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "10.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "11.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "12.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "13.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "14.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "15.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "pp_1.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "pp_8.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "pp_14.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "pp_19.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "event_1.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "event_2.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "event_3.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "event_4.jpg"],
    [ '2015-01-01', "Colonial Event", 2, "area_Bakery.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "area_Blacksmith.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "area_Seamstress.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "area_Cooperage.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "area_Archery.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "area_Musket Shooting.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "hf_Alexander Hamilton.jpg"],
    [ '2015-01-01', "Colonial Event", 1, "hf_Benjamin Franklin.jpg"],

]:
    u = hmod.Photograph()
    u.date_taken = data[0]
    u.place_taken = data[1]
    u.user_id = data[2]
    u.image = data[3]
    u.save()


#Event
for data in [
    [ "Colonial Heritage July 4", "Annual Celebration on July 4th. Celebrate our Indepedence!", '2015-07-04', '2015-07-04', "file0", "Scera Outdoor Ampitheater", 1 ],
    [ "Heritage Expo", "Come see the many wonders of the Colonial time period", '2015-10-10', '2015-10-10', "file1", "UVU Center", 1 ],
    [ "Costume Showcase!", "This is a special event for High School students interested in costume design.", '2015-11-11', '2015-11-11', "file2", "Provo High School", 1 ],
    [ "Muskets and Gunpowder", "Come practice shooting some muskets with George, Alex and Benny", '2015-06-06', '2015-06-06', "file3", "Provo Gun Range", 1 ],
]:
    u = hmod.Event()
    u.name = data[0]
    u.description = data[1]
    u.start_date = data[2]
    u.end_date = data[3]
    u.map_file = data[4]
    u.venue_name = data[5]
    u.address_id = data[6]
    u.save()


#HistoricalFigure
for data in [
    [ "Benjamin Franklin", '1706-01-17', "Boston", '1790-04-17', "Philedelphia", 
        """He was one of the most extraordinary human beings the world has
        ever known. Born into the family of a Boston candle maker, Benjamin
        Franklin became the most famous American of his time. He helped
        found a new nation and defined the American character. Writer,
        inventor, diplomat, businessman, musician, scientist, humorist,
        civic leader, international celebrity . . . genius. 
        Explore the life of a remarkable man.""", False, 1],
    [ "Alexander Hamilton", '1755-01-11', "Charleston", '1804-07-12', "New York", 
        """Hamilton became the leading cabinet member in the new government under President Washington.
        Hamilton was a nationalist, who emphasized strong central government and successfully argued 
        that the implied powers of the Constitution provided the legal authority to fund the national debt, 
        assume states' debts, and create the government-owned Bank of the United States.""", False, 1],
    [ "John Cooper", '1714-05-05', "Coopertown", '1804-07-12', "Coopertown", 
        """Most famous cooper in town. Made the barrels used in the Boston Tea Party!""", True, 1],
]:

    u = hmod.HistoricalFigure()
    u.name = data[0]
    u.birth_date = data[1]
    u.birth_place = data[2]
    u.death_date = data[3]
    u.death_place = data[4]
    u.biographical_note = data[5]
    u.is_fictional = data[6]
    u.event_id = data[7]
    u.save()


#Area
for data in [
    [ "Bakery", "This is where the bread is baked.", 1, 1, 2, 1 ],
    [ "Blacksmith", "This is where the metal is pounded.", 2, 1, 2, 1 ],
    [ "Seamstress", "This is where the thread is sewn.", 3, 1, 2, 1 ],
    [ "Archery", "This is where the archers arch.", 4, 1, 2, 1 ],
    [ "Cooperage", "This is where the barrells are coopered.", 5, 1, 2, 1 ],
    [ "Musket Shooting", "This is where the muskets are shot.", 1, 1, 2, 4 ],
    [ "Bakery", "This is where the bread is baked.", 1, 1, 2, 2 ],
    [ "Blacksmith", "This is where the metal is pounded.", 2, 1, 2, 2 ],
    [ "Seamstress", "This is where the thread is sewn.", 3, 1, 2, 3 ],
    [ "Archery", "This is where the archers arch.", 4, 1, 2, 4 ],
    [ "Cooperage", "This is where the barrells are coopered.", 5, 1, 2, 2 ],
]:
    u = hmod.Area()
    u.area_name = data[0]
    u.description = data[1]
    u.place_number = data[2]
    u.coordinator_id = data[3]
    u.supervisor_id = data[4]
    u.event_id = data[5]
    #u.participants_id = data[6]
    u.save()


#UserRole
for data in [
    [ 5, 5, "Cooper", "Artisan", 3 ],
    [ 1, 4, "Baker", "Artisan",  None ],
]:
    u = hmod.UserRole()
    u.area_id = data[0]
    u.participant_id = data[1]
    u.name = data[2]
    u.type = data[3]
    #if data[4] != None:
    u.historical_figure_id = data[4]
    u.save()


#ExpectedSaleItem
for data in [
    [ "Bread Pin", "A baker's rolling pin. An essential in the colonial kitchen!.", 10.00, 20.00, None, 1 ],
    [ "Coopers Brush", "Used to give a nice stain to the new barrel.", 5.00, 20.00, None, 5 ],
    [ "Musket", "Modern replica. Does not fire live rounds.", 5.00, 20.00, None, 6 ],
]:
    u = hmod.ExpectedSaleItem()
    u.name = data[0] 
    u.description = data[1] 
    u.low_price =  data[2] 
    u.high_price = data[3] 
    u.photo = data[4] 
    u.area_id = data[5]
    u.save()


#Transaction
for data in [
    #1Random
    [ '2015-01-01', '2015-01-01', 3, '2015-01-01', 3, '2015-01-01', 3, "AA12345678", 1, 3, 3, 3, 6],
    #2Bulk buy of Liberty Bell by Customer1
    [ '2015-01-02', '2015-01-02', 3, '2015-01-02', 3, '2015-01-02', 3, "BB12345678", 1, 3, 3, 3, 5],
    #3Bulk buy of Liberty Pen by Customer2
    [ '2015-01-03', '2015-01-03', 3, '2015-01-03', 3, '2015-01-03', 3, "CC12345678", 1, 3, 3, 3, 6],
    #4Erwin Rommel rented guns in the following transaction
    [ '2015-01-04', '2015-01-04', 3, '2015-01-04', 3, '2015-01-04', 3, "DD12345678", 1, 3, 3, 3, 17],
    #5George Washington rented swords in the following transaction
    [ '2015-01-05', '2015-01-05', 3, '2015-01-05', 3, '2015-01-05', 3, "FF12345678", 1, 3, 3, 3, 14],
    #6customer1 rented a cannon in the following transaction
    [ '2015-01-05', '2015-01-05', 3, '2015-01-05', 3, '2015-01-05', 3, "GG12345678", 1, 3, 3, 3, 5],
    #7Kalli rented 1 glove, 1 pants, 1 shirt in the following transaction
    [ '2015-02-05', '2015-02-05', 3, '2015-02-05', 3, '2015-02-05', 3, "HH12345678", 1, 3, 3, 3, 13],
    #8Dustin rented 1 sword, 1 gun, 1 belt, 1 shirt in the following transaction
    [ '2015-01-05', '2015-01-05', 3, '2015-01-05', 3, '2015-01-05', 3, "II12345678", 1, 3, 3, 3, 8],
    #7Kalli rented 1 glove, 1 pants, 1 shirt in the following transaction
    [ '2015-04-01', '2015-04-01', 3, '2015-04-01', 3, '2015-04-01', 3, "HH12345678", 1, 3, 3, 3, 8],
    #8Dustin rented 1 sword, 1 gun, 1 belt, 1 shirt in the following transaction
    [ '2015-04-01', '2015-04-01', 3, '2015-04-01', 3, '2015-04-01', 3, "II12345678", 1, 3, 3, 3, 8],
]:
    u = hmod.Transaction()
    u.date = data[0]
    u.date_packed = data[1]
    u.packed_by_id =data[2]
    u.date_paid =data[3]
    u.payment_handler_id = data[4]
    u.date_shipped = data[5]
    u.shipped_by_id =data[6]
    u.tracking_number =data[7]
    u.ships_to_id = data[8]
    u.payment_processed_by_id = data[9]
    u.shipped_by_id = data[10]
    u.handled_by_id = data[11]
    u.customer_id = data[12]
    u.save()




#Category
for data in [
    ["Stock"],
    ["Serialized"],
    ["Wardrobe"],
    ["Rentable"],
    ["Clothing"],
    ["Military"],
    ["Appliance"],
]:
    u = hmod.Category()
    u.description = data[0]
    u.save()

#ProductSpecification
for data in [
    [ "Liberty Bell", 5.00, "A small replica of the liberty bell. A hot seller!", "Colonial Heritage Foundation", 5.00, "ABCDEF01", "Order for [Name Here]", "2014-06-06", 1, 1, 1],
    [ "Handkerchief", 3.00, "An old handkerchief. A hot seller!", "Colonial Heritage Foundation", 5.00, "ABCDEF02", "Order for [Name Here]", "2014-06-06", 2, 1, 1],
    [ "Liberty Pen", 5.00, "A replica of an old pen. A hot seller!", "Colonial Heritage Foundation", 5.00, "ABCDEF03", "Order for [Name Here]", "2014-06-06", 3, 1, 1],
    #Serialized
    [ "Necklace", 15.00, "A necklace with an American flag pendant.", "Colonial Heritage Foundation", 15.00, "ABCDEF04", "Order for [Name Here]", "2014-06-06", 4, 1, 2],
    [ "Bracelet", 15.00, "A Bracelet with an American flag pendant.", "Colonial Heritage Foundation", 15.00, "ABCDEF05", "Order for [Name Here]", "2014-06-06", 5, 1, 2],
    [ "Watch", 15.00, "A watch with an American flag pendant.", "Colonial Heritage Foundation", 15.00, "ABCDEF06", "Order for [Name Here]", "2014-06-06", 6, 1, 2],
    #Wardrobe 
    [ "Hat", 22.00, "A hat from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF07", "Order for [Name Here]", "2014-06-06", 7, 1, 3],
    [ "Shirt", 22.00, "A shirt from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF08", "Order for [Name Here]", "2014-06-06", 8, 1, 3],
    [ "Belt", 22.00, "A belt from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF09", "Order for [Name Here]", "2014-06-06", 9, 1, 3],
    [ "Pants", 22.00, "A pants from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF10", "Order for [Name Here]", "2014-06-06", 10, 1, 3],
    [ "Boots", 22.00, "A boot from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF11", "Order for [Name Here]", "2014-06-06", 11, 1, 3],
    [ "Gloves", 22.00, "A glove from the colonial time.", "Colonial Heritage Foundation", 15.00, "ABCDEF12", "Order for [Name Here]", "2014-06-06", 12, 1, 3],
    #Rentable
    [ "Cannon", 122.00, "A cannon from the colonial time.", "Colonial Heritage Foundation", 30.00, "ABCDEF13", "Order for [Name Here]", "2014-06-06", 13, 1, 4],
    [ "Gun", 122.00, "A gun from the colonial time.", "Colonial Heritage Foundation", 30.00, "ABCDEF14", "Order for [Name Here]", "2014-06-06", 14, 1, 4],
    [ "Sword", 122.00, "A sword from the colonial time.", "Colonial Heritage Foundation", 30.00, "ABCDEF15", "Order for [Name Here]", "2014-06-06", 15, 1, 4],
]:
    u = hmod.ProductSpecification()
    u.name = data[0]
    u.price = data[1]
    u.description = data[2]
    u.manufacturer = data[3]
    u.average_cost  = data[4]
    u.sku = data[5]
    u.order_form_name = data[6]
    u.production_time = data[7]
    u.photo_id = data[8]
    u.vendor_id = data[9]
    u.category_id = data[10]
    u.save()


#StockedProduct
for data in [
    [ '50', "Top", "Order_File1", 1],
    [ '50', "Bottom", "Order_File2", 2],
    [ '50', "Middle", "Order_File3", 3],
]:
    u = hmod.StockedProduct()
    u.quantity_on_hand = data[0]
    u.shelf_location = data[1]
    u.order_file = data[2]
    u.product_specification_id = data[3]
    u.save()


#SerializedProduct
for data in [
    [ '10', "Top", "Order_File01", 4, "00001", '2014-01-01', 5.00, "Status", True, True, True, "Serialized Product 1: Necklace"],
    [ '10', "Bottom", "Order_File02", 5, "00002", '2014-01-01', 5.00, "Status", True, True, True, "Serialized Product 2: Bracelet"],
    [ '10', "Middle", "Order_File03", 6, "00003", '2014-01-01', 5.00, "Status", True, True, True, "Serialized Product 3: Watch"],
]:
    u = hmod.SerializedProduct()
    u.quantity_on_hand = data[0]
    u.shelf_location = data[1]
    u.order_file = data[2]
    u.product_specification_id = data[3]
    u.serial_number = [4]
    u.date_acquired = [5]
    u.cost = data[6]
    u.status = data[7]
    u.for_sale = data[8]
    u.condition_new = data[9]
    u.is_rentable = data[10]
    u.notes = data[11]
    u.save()


#WardrobeItem
for data in [
    [ '30', "Bottom", "Order_File10", 7, "00007", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 1: Hat", None, None, "Male", "Blue", None, 1770, 1870, "This is a hat"],
    [ '30', "Bottom", "Order_File20", 8, "00008", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 2: Shirt", 'M', None, "Male", "Blue", None, 1770, 1870, "This is a shirt"],
    [ '25', "Bottom", "Order_File30", 9, "00009", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 3: Belt", '30', None, "Male", "Blue", None, 1770, 1870, "This is a belt"],
    [ '25', "Bottom", "Order_File40", 10, "000010", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 4: Pants", '30', None, "Male", "Blue", None, 1770, 1870, "This is pants"],
    [ '10', "Bottom", "Order_File50", 11, "000011", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 5: Boots", '10', None, "Male", "Blue", None, 1770, 1870, "This is a boot"],
    [ '10', "Bottom", "Order_File60", 12, "000012", '2014-01-01', 5.00, "Status", True, True, True, "Wardrobe Item 6: Gloves", 'M', None, "Male", "Black", None, 1770, 1870, "This is a glove"],
]:
    u = hmod.WardrobeItem()
    u.quantity_on_hand = data[0]
    u.shelf_location = data[1]
    u.order_file = data[2]
    u.product_specification_id = data[3]
    u.serial_number = [4]
    u.date_acquired = [5]
    u.cost = data[6]
    u.status = data[7]
    u.for_sale = data[8]
    u.condition_new = data[9]
    u.is_rentable = data[10]
    u.notes = data[11]
    u.size =data[12]
    u.size_modifier = data[13]
    u.gender = data[14]
    u.color =data[15]
    u.pattern =data[16]
    u.start_year = data[17]
    u.end_year =data[18]
    u.note = data[19]
    u.save()


#RentableProduct
for data in [
    [ '5', "Bottom", "Order_File001", 13, "00007", '2014-01-01', 500.00, "Status", True, True, True, "Rentable Item 1: Cannon", 5, 25.00, 100.00],
    [ '5', "Bottom", "Order_File002", 14, "00008", '2014-01-01', 25.00, "Status", True, True, True, "Rentable Item 2: Gun",5, 25.00, 100.00],
    [ '5', "Bottom", "Order_File003", 15, "00009", '2014-01-01', 50.00, "Status", True, True, True, "Rentable Item 3: Sword", 5, 25.00, 100.00],
]:
    u = hmod.RentableProduct()
    u.quantity_on_hand = data[0]
    u.shelf_location = data[1]
    u.order_file = data[2]
    u.product_specification_id = data[3]
    u.serial_number = [4]
    u.date_acquired = [5]
    u.cost = data[6]
    u.status = data[7]
    u.for_sale = data[8]
    u.condition_new = data[9]
    u.is_rentable = data[10]
    u.notes = data[11]
    u.times_rented = data[12]
    u.price_per_day = data[13]
    u.replacement_price = data[14]
    u.save()

#LineItem - Abstract!
# for data in [
#     # ['1.0',1],
#     # ['1.1',1]
# ]:
#     u = hmod.LineItem()
#     u.price = data[0]
#     u.transaction_id = data[1]
#     u.save()


#SaleItem
for data in [
    #Bulk buy of Liberty Bell by Customer1
    [ 500.00, 2, 100, 1],
    #Bulk buy of Liberty Pen by Customer2
    [ 300.00, 3, 100, 3]
]:
    u = hmod.SaleItem()
    u.price = data[0]
    u.transaction_id = data[1]
    u.quantity = data[0]
    u.item_id = data[1]
    u.save()


#8Dustin rented 1 sword15, 1 gun14, 1 belt9, 1 shirt8 in the following transaction

#Rental Item
for data in [
    #Three Guns are checked out by Erwin OVER 30
    [10.00, 4, '2014-01-01', None, '2015-03-01', None, 14],
    [10.00, 4, '2014-01-01', None, '2015-03-01', None, 14],
    [10.00, 4, '2014-01-01', None, '2015-03-01', None, 14],
    #Six Swords are checked out Washington Over 90
    [12.00, 5, '1776-09-26', None, '1780-02-20', None, 15],
    [12.00, 5, '1776-09-26', None, '1780-02-20', None, 15],
    [12.00, 5, '1776-09-26', None, '1780-02-20', None, 15],
    [12.00, 5, '1776-09-26', None, '1780-02-20', None, 15],
    [12.00, 5, '1776-09-26', None, '1780-02-20', None, 15],
    [12.00, 5, '1776-09-26', None, '1780-02-20', None, 15],
    #One cannon is checked out by customer1 Over 60
    [10.00, 6, '2015-01-30', None, '2015-01-29', None, 13],
    #7Kalli rented 1 glove12, 1 pants10, 1 shirt8 in the following transaction
    [10.00, 7, '2015-03-15', None, '2015-04-20', None, 12],
    [10.00, 7, '2015-03-15', None, '2015-04-20', None, 10],
    [10.00, 7, '2015-03-15', None, '2015-04-20', None, 8],
    #8Dustin rented 1 sword15, 1 gun14, 1 belt9, 1 shirt8 in the following transaction
    [12.00, 8, '2015-03-15', None, '2015-03-20', None, 15],
    [12.00, 8, '2015-03-15', None, '2015-03-20', None, 14],
    [12.00, 8, '2015-03-15', None, '2015-03-20', None, 9],
    [12.00, 8, '2015-03-15', None, '2015-03-20', None, 8],
    #Six shirts are checked out 
    [12.00, 9, '2015-04-01', '2015-04-02', '2015-04-02', None, 8],
    [12.00, 9, '2015-04-01', '2015-04-02', '2015-04-02', None, 8],
    [12.00, 9, '2015-04-01', '2015-04-02', '2015-04-02', None, 8],
    [12.00, 9, '2015-04-01', '2015-04-02', '2015-04-02', None, 8],
    [12.00, 9, '2015-04-01', '2015-04-02', '2015-04-02', None, 8],
    [12.00, 9, '2015-04-01', '2015-04-02', '2015-04-02', None, 8],
    #Six belts are checked out
    [12.00, 10, '2015-04-01', '2015-04-02', '2015-04-02', None, 9],
    [12.00, 10, '2015-04-01', '2015-04-02', '2015-04-02', None, 9],
    [12.00, 10, '2015-04-01', '2015-04-02', '2015-04-02', None, 9],
    [12.00, 10, '2015-04-01', '2015-04-02', '2015-04-02', None, 9],
    [12.00, 10, '2015-04-01', '2015-04-02', '2015-04-02', None, 9],
    [12.00, 10, '2015-04-01', '2015-04-02', '2015-04-02', None, 9],

]:
    u = hmod.RentalItem()
    u.price = data[0]
    u.transaction_id = data[1]
    u.date_out = data[2]
    u.date_in = data[3]
    u.date_due = data[4]
    u.discount_percent = data[5]
    u.rentable_product_id = data[6]
    u.save()



# Fee
for data in [
    [ 1.00, False, "Gun #1 was not returned clean by Rommel", 1],
    [ 1.00, False, "Gun #2 was not returned clean by Rommel", 2],
    [ 10.00, False, "Sword #1 was not returned clean by Washington", 4],
    [ 10.00, False, "Sword #6 was not returned clean by Washington", 9],
]:
    u = hmod.Fee()
    u.amount = data[0]
    u.waived = data[1]
    u.description = data[2]
    u.rental_item_id = data[3]
    u.save()




# select * from home_transaction 
# join home_rentalitem  on home_transaction.id=home_rentalitem.transaction_id 
# join home_stockedproduct on home_rentalitem.rentable_product_id=home_stockedproduct.id 
# join home_productspecification on home_stockedproduct.product_specification_id=home_productspecification.id


##This SQL will get the user, trnasaction, rental item
# select home_transaction.id as transaction, first_name, home_rentalitem.id as Rental_Item, home_productspecification.name
# from home_transaction 
# join home_user on home_transaction.customer_id=home_user.id 
# join home_rentalitem on home_transaction.id=home_rentalitem.transaction_id 
# join home_rentableproduct on home_rentableproduct.serializedproduct_ptr_id=home_rentalitem.rentable_product_id 
# join home_productspecification on home_productspecification.id=home_rentableproduct.serializedproduct_ptr_id 
# where home_user.first_name='George'