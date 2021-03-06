import sys 
import requests
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
            
            res = requests.post(url='http://employee-management.info/'+operation)
            return res.json()

        elif(role == "hr"):
            if(operation== "create"):
                data = json.dumps(employee['data'])
                res = requests.post(url='http://employee-management.info/'+operation+'/'+data)
                
                return json.loads(res.text)
                
            elif(operation == "delete"):
                primary_key = employee['mail']
                res = requests.get(url='http://employee-management.info/'+operation+'/'+primary_key)
                return json.loads(res.text)

        elif(role == 'developer'):
            if(operation== "create"):
                data = json.dumps(employee['data'])
                res = requests.post(url='http://employee-management.info/'+operation+'/'+data)
                return json.loads(res.text) 
            elif(operation == "update"):
                primary_key = employee['mail']
                data = employee['data']
                res = requests.post(url='http://employee-management.info/'+operation+'/'+primary_key+'/'+json.dumps(data))
                return json.loads(res.text)    
    return jsonify({"message": "unautherized user"})


