# FOLDER TERMINOLOGY

**$AUTH**
```
Auth contain two file for user login and user registration and they all are responsible for modifying the first database of mongodb which contains the user credentials.
```
**$DB_ADMIN**
```
DB_ADMIN contains a file which will provide mongodb client to all the dependants.
```
**$manifest**
```
manifest contains the manifest files which is required to deploy app in kubernetes 
```

# INSTRUCTIONS

1. run this following command to deploy app in kubernetes in your system.
```
$ kubectl create -f manifest/.
```

2. Go to minikube dashboard to see if its working.
```
$ minikube dashboard
```
3. to get all the services of minikube.
```
$ minikube service list
```
4. choose the following service and use this in postman to hit the api

> To use the Authorization/authentication, use the following url

```
http://192.168.99.100:32000
```

# API TERMINOLOGY

***http://192.168.99.100:32000/register***

```
This will let the use to be registered to the employee management system and to avail the services of crud.
```
$ INPUT

```
{
	"userid": "0002",
	"password": "0002",
	"role": "developer"
}
```

$ OUTPUT

```
{
  "message": "user added"
}
```
# FOR EMP_CREATE
***http://192.168.99.100:32000/login***

$ INPUT
```
{
			"userid": "0006",
	"password": "0006",
	"role": "hr",
	"operation": "create",
	
	
	"data":
		{
			"name": "amar",
			"mail": "amar.pundir@gslab.com",
			"address": "pune"	
	}
		
}
```
$ OUTPUT

```
{
    "status": "sucess"
}
```
