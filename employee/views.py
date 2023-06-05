from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
import json
import pymongo


# connects to a MongoDB database hosted on the MongoDB Atlas cloud service

myclient = pymongo.MongoClient('mongodb+srv://deepakvsdevu:root@cluster0.i5xbwqc.mongodb.net/')

# established a connection to the MongoDB cluster, selected the 'test' database, and obtained a reference to the 'demo' collection.
mydb = myclient['test']
mycol = mydb['demo']


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def loginn(request):
    return render(request,'login.html')



 
class Employeedetail(APIView):
    # POST method to handle the file upload
    def post(self, request, format=None):
            
            
            # Creating a list of form data and the uploaded file
            mylist=[]
            data = request.POST
            mylist.append({'name':data['name'],'email':data['email'],'phone':data['phone']})

            # Inserting the data into MongoDB
            x = mycol.insert_many(mylist)
            # Rendering the success page with a success message
            return HttpResponse("Registration succesfull...!")
 
    
    
# Define the API view for getting, updating, and deleting individual profiles
class takeuserprofile(APIView):
    
    # GET method to retrieve a profile by name
    def get(self, request, name):
        if not name:
            return JsonResponse({"error": "Name parameter is missing."})
        # Find the profile in the database by name and exclude the ID field
        mydoc = mycol.find({"name": name}, {"_id": 0, "processed_message_id": 0})
        result = []
        for x in mydoc:
            result.append(x)
        # Return the profile as a JSON response
        return JsonResponse(result, safe=False)
    
    
    # PUT method to update a profile by name
    def put(self,request,name):
        if not name:
            return JsonResponse({"error": "Name parameter is missing."})
        data = request.data
        query = {'name': name}
        new_values = {"$set": data}
        # update the profile in the database by name
        result = mycol.update_one(query, new_values)
        
        if result.modified_count == 1:
            updated_doc = mycol.find_one(query, {"_id": 0, "processed_message_id": 0})
            # Return the updated profile as a JSON response
            return JsonResponse(updated_doc, safe=False)
        else:
            return JsonResponse({"error": "Document not found."})
       
    # DELETE method to delete a profile by name  
    def delete(self,request,name):
        if not name:
            return JsonResponse({"error": "Name parameter is missing."})
        # Delete the profile in the database by name
        mydoc= mycol.delete_one({"name":name})
        mydic = mycol.find({},{"_id": 0,"processed_message_id":0})
        result = []
        for x in mydic:
            result.append(x)
        # Return all profiles as a JSON response
        return JsonResponse(result, safe=False)
    