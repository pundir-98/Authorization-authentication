import sys 
sys.path.append('./')
from DB_ADMIN import db
from flask import *
from AUTH import login

databaseObj = db.database()

databaseClient = databaseObj.getClient1()

db = databaseClient.login 
collection =db.logindetail



def register():
    employee = request.get_json()
    if(not login.is_exist(employee)):
        userid = employee["userid"]
        password = employee["password"]
        role = employee["role"]
        mydict = {"userid": userid , "password": password ,"role": role}
        collection.insert_one(mydict)
        return jsonify({'message':'user added'})
    return jsonify({"message": "user already exist"})



    