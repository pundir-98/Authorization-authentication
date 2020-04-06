import sys 
from flask import *
sys.path.append('./')
from DB_ADMIN import db
import json



databaseObj = db.database()

databaseClient = databaseObj.getClient1()
db = databaseClient.login 
collection =db.logindetail

def is_exist(employee):
    for id in collection.find({},{"_id": 0}):
        print("crunt id ="+ id['userid'])
        if((employee["userid"]==id['userid'] and employee["password"]==id["password"]) and employee["role"]==id["role"]):
            print("match")
            return True
    return False

def login():
    employee = request.get_json()
    
    userid = employee["userid"]
    password = employee["password"]
    role  = employee["role"]
    operation= employee['operation']
    if(is_exist(employee)):

        if(role == "manager"):
            
            return redirect('http://192.168.99.100:32001/'+operation,code=307)
        elif(role == "hr"):
            if(operation== "create"):
                data = json.dumps(employee['data'])
                return redirect('http://192.168.99.100:32001/'+operation+'/'+data,code=307)
            elif(operation == "delete"):
                primary_key = employee['mail']
                return redirect('http://192.168.99.100:32001/'+operation+'/'+primary_key,code=307)

        elif(role == 'developer'):
            if(operation== "create"):
                data = json.dumps(employee['data'])
                return redirect('http://192.168.99.100:32001/'+operation+'/'+data,code=307)
            elif(operation == "update"):
                primary_key = employee['mail']
                data = employee['data']
                return redirect('http://192.168.99.100:32001/'+operation+'/'+primary_key+'/'+json.dumps(data),code=307)    
    return jsonify({"message": "unautherized user"})


