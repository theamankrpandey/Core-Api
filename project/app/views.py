from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from app.models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.



# put : Update All Fields 
# Patch : single Field or MUltiple field Ko Update krta hai

# model to dict sirf ek object ko convert krte hai dictionary se
# filter multiple object ki query h or get single object ki

# json to python convert using loads

# @csrf_exempt
# def all_data(req):
#     if req.method == "POST":
#         data = req.body
#         # print(data)
#         # print(type(data))
#         p_data=json.loads(data) #json to python convert using loads
#         # print(p_data)
#         # print(type(p_data))
#         n = p_data.get('name')
#         a = p_data.get('age')
#         e = p_data.get('email')
#         c = p_data.get('contact')
#         if 'name'in p_data and 'age' in p_data and 'email' in p_data and'contact' in p_data:
#             Student.objects.create(name=n,age=a,email=e,contact=c)
#             p_data={"msg":"Object Created"}
#         else:
#             if not 'name' in p_data:
#                 p_data={'msg':'Name fields are Missing'}
#                 return HttpResponse(json.dumps(p_data),content_type='application/json')

#             if not 'age' in p_data:
#                 p_data={'msg':'Age fields are Missing'}
#                 return HttpResponse(json.dumps(p_data),content_type='application/json')

#             if not 'email' in p_data:
#                 p_data={'msg':'Email fields are Missing'}
#                 return HttpResponse(json.dumps(p_data),content_type='application/json')

#             if not 'contact' in p_data:
#                 p_data={'msg':'Contact  fields are Missing'}
#                 return HttpResponse(json.dumps(p_data),content_type='application/json')

#             # p_data={'msg':'some Required fields are Missing'}
#             # return HttpResponse(json.dumps(p_data),content_type='application/json')   
#     data = Student.objects.all()
#     print(data.values())
#     p_data=list(data.values())
#     print(p_data)
#     j_data=json.dumps(p_data) 
#     # print(j_data)
#     return HttpResponse(j_data,content_type='application/json') 



# @csrf_exempt
# def single_data(req,pk):
#     user = Student.objects.filter(id=pk)
#     if not user:
#         p_data = {'msg':'Enter Id not present in Our Db'}
#         return HttpResponse(json.dumps(p_data),content_type="application/json")
#     else:
#         if req.method == 'PUT':
#             data = req.body
#             print(data)
#             print(type(data))
#             p_data = json.loads(data) 
#             print(p_data)
#             print(type(p_data))
#             if 'name' in p_data and 'age' in p_data and 'contact' in p_data and 'city' in p_data:
#                 n = p_data.get('name')
#                 a = p_data.get('age')
#                 e = p_data.get('email')
#                 c = p_data.get('contact')
#                 old_data = Student.objects.get(id=pk)
#                 old_data.name=n
#                 old_data.age=a
#                 old_data.email=e
#                 old_data.contact=c
#                 old_data.save()
#                 p_data = {'msg':'object updated'}
#                 return HttpResponse (json.dumps(p_data),content_type='application/json')
#             else:
#                 if not 'name' in p_data:
#                     p_data={'msg':'Name fields are Missing'}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')

#                 if not 'age' in p_data:
#                     p_data={'msg':'Age fields are Missing'}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')

#                 if not 'email' in p_data:
#                     p_data={'msg':'Email fields are Missing'}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')

#                 if not 'contact' in p_data:
#                     p_data={'msg':'Contact  fields are Missing'}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')
#         elif req.method =='PATCH':
#             data = req.body
#             print(data)
#             print(type(data))
#             p_data=json.loads(data)
#             print(p_data)
#             print(type(p_data))
#             n = p_data.get('name')
#             a = p_data.get('age')
#             e = p_data.get('email')
#             c = p_data.get('contact')
#             if p_data:
#                 n = p_data.get('name')
#                 a = p_data.get('age')
#                 e = p_data.get('email')
#                 c = p_data.get('contact')
#                 old_data = Student.objects.get(id=pk)
#                 if n:
#                     old_data.name=n
#                 if a:
#                     old_data.age=a
#                 if e:
#                     old_data.email=e
#                 if c:
#                     old_data.contact=c
#                 old_data.save()
#                 p_data = {'msg':'object partially Updated'}
#                 return HttpResponse (json.dumps(p_data),content_type='application/json') # python to json convert use dumps
#             else:
#                 p_data = {'msg':'object Values are missing'}
#                 return HttpResponse (json.dumps(p_data),content_type='application/json')
#         elif req.method =='DELETE':
#             User = Student.objects.get(id=pk)
#             user.delete()
#             p_data={'msg':'object Delete'}
#             return HttpResponse(json.dumps(p_data),content_type='application/json')

        


#     p_data=Student.objects.get(id=pk)
#     print(p_data)
#     print(type(p_data))
#     p_data=model_to_dict(p_data)   x
#     print(p_data)
#     print(type(p_data))
#     return HttpResponse(json.dumps(p_data),content_type="application/json")


# @csrf_exempt    
# def single_url(req):
#     data = req.body
#     print(data)
#     print(type(data))
#     # if data:
#     #     print("hello")
#     # else:
        
#     # n=p_data.get('Name')
#     # a=p_data.get('Age')
#     # c=p_data.get('Contact')
#     # ci=p_data.get('City')
#     if data:
#         p_data = json.loads(data) # json to python object convert
#         print(p_data)
#         print(type(p_data))
#         if 'id' in p_data:
#             pk = p_data['id']
#             if req.method == 'PUT':
#                 data = req.body
#                 print(data)
#                 print(type(data))
#                 p_data = json.loads(data)
#                 print(p_data)
#                 print(type(p_data))
#                 if 'Name' in p_data and 'Age' in p_data and 'Contact' in p_data and 'City' in p_data:
#                     n=p_data.get('Name')
#                     a=p_data.get('Age')
#                     c=p_data.get('Contact')
#                     ci=p_data.get('City')
#                     old_data = Student.objects.get(id=pk)
#                     old_data.Name=n
#                     old_data.Age=a
#                     old_data.Contact=c
#                     old_data.City=ci
#                     old_data.save()
#                     p_data={'msg':'object updated'}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')
#                 else:
#                     if not 'Name' in p_data:
#                         p_data={'msg':'Please fill name'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json')
#                     if not 'Age' in p_data:
#                         p_data={'msg':'Please fill age'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json')
#                     if not 'Contact' in p_data:
#                         p_data={'msg':'Please fill contact detail'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json')
#                     if not 'City' in p_data:
#                         p_data={'msg':'Please fill city'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json')

#             elif req.method == 'PATCH':
#                 data = req.body
#                 print(data)
#                 print(type(data))
#                 p_data = json.loads(data)
#                 print(p_data)
#                 print(type(p_data))
#                 n=p_data.get('Name')
#                 a=p_data.get('Age')
#                 c=p_data.get('Contact')
#                 ci=p_data.get('City')
#                 if p_data:
#                     n=p_data.get('Name')
#                     a=p_data.get('Age')
#                     c=p_data.get('Contact')
#                     ci=p_data.get('City')
#                     old_data = Student.objects.get(id=pk)
#                     if n:
#                         old_data.Name=n
#                     if a:
#                         old_data.Age=a
#                     if c:
#                         old_data.Contact=c
#                     if ci:
#                         old_data.City=ci 
#                     old_data.save()
#                     p_data={'msg':'object Partially updated'}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')
#                 else:
#                     p_data={'msg':'object values are missing'}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')
        
#             elif req.method == 'DELETE':
#                 user = Student.objects.get(id=pk)
#                 user.delete()
#                 p_data={'msg':'Object Deleted'}
#                 return HttpResponse(json.dumps(p_data),content_type='application/json')

#             data = Student.objects.get(id=pk)
#             print(data)
#             print(type(data))
#             p_data = model_to_dict(data)
#             print(p_data)
#             print(type(p_data))
#             j_data=json.dumps(p_data)
#             print(j_data)
#             return HttpResponse(j_data,content_type='application/JSON')
#         else:
#             if req.method == "POST":
#                 data = req.body
#                 print(data)
#                 print(type(data))
#                 p_data = json.loads(data)
#                 print(p_data)
#                 print(type(p_data))
#                 n=p_data.get('Name')
#                 a=p_data.get('Age')
#                 c=p_data.get('Contact')
#                 ci=p_data.get('City')
#                 if 'Name' in p_data and 'Age' in p_data and 'Contact' in p_data and 'City' in p_data:
#                     Student.objects.create(
#                         Name=n,
#                         Age=a,
#                         Contact=c,
#                         City=ci
#                     )
#                     p_data = {"msg": "object created successfully"}
#                     return HttpResponse(json.dumps(p_data),content_type='application/json')
#                 else:
#                     if not 'Name' in p_data:
#                         p_data={'msg':'Please fill name'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json')
#                     if not 'Age' in p_data:
#                         p_data={'msg':'Please fill age'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json')
#                     if not 'Contact' in p_data:
#                         p_data={'msg':'Please fill contact detail'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json')
#                     if not 'City' in p_data:
#                         p_data={'msg':'Please fill city'}
#                         return HttpResponse(json.dumps(p_data),content_type='application/json') 
#                     # p_data={'msg':'Some required fields are missing'}
#                     # return HttpResponse(json.dumps(p_data),content_type='application/json')
            
#             data = Student.objects.all()
#             print(data)
#             p_data=list(data.values())
#             print(p_data)
#             j_data=json.dumps(p_data)
#             print(j_data)
#             return HttpResponse(j_data,content_type='application/JSON')
#     else:
        
#         p_data={'msg':'atleast provide one empty dict'}
#         j_data=json.dumps(p_data)
#         print(j_data)
#         return HttpResponse(j_data,content_type='application/JSON')



'''For All data'''
@csrf_exempt
def all_data(req):
    if req.method == 'POST':
        j_data = req.body
        p_data = json.loads(j_data)
        n = p_data.get('name')
        a = p_data.get('age')
        user=User.objects.create(name=n,age=a)
        data={
            "data Created":True,
            "name":user.name,
            "age":user.age
        }
        return JsonResponse(data,safe=False)

    '''Get Method for all Data'''
    p_data = User.objects.all().values()
    j_data = list(p_data)
    return JsonResponse(j_data,safe=False)



'''One Specific user Data Update'''
@csrf_exempt
def Student_detail(req,pk):
    user = Student.objects.filter(id=pk)
    if not user:
        msg = "Enter Id not present in Our Db"
        return JsonResponse(msg,safe=False)
    if req.method == 'GET':
        data = Student.objects.get(id=pk)
        print(data)
        # python_data = {
        #     "id": data.id,
        #     "name": data.name,
        #     "age": data.age,
        #     "email": data.email,
        #     "contact": data.contact
        # }

        '''model to dict sirf ek object ko convert krte hai dictionary se'''
        python_data = model_to_dict(data)  
        return JsonResponse(python_data)


    if req.method == 'PUT':
        json_data = req.body
        python_data = json.loads(json_data)
        if not user:
            msg = "Enter Id not present in Our Db"
            return JsonResponse(msg,safe=False)
        if 'name' in python_data and 'age' in python_data and 'email' in python_data and 'contact' in python_data:
            n = python_data.get('name')
            a = python_data.get('age')
            e = python_data.get('email')
            c = python_data.get('contact')
            old_data = Student.objects.get(id = pk)
            old_data.name = n
            old_data.age = a
            old_data.email = e
            old_data.contact = c
            old_data.save()
            emsg = "Object Updated"
            return JsonResponse(emsg,safe=False)
        hmsg = "Some Reuired Fields Are Missing Please Fill"
        return JsonResponse(hmsg,safe=False)



    if req.method == 'PATCH':
        json_data = req.body
        python_data = json.loads(json_data)
        if 'name' in python_data:
            msg = "Name Updated Succesfully"
            return JsonResponse(msg,safe=False)
        if 'age' in python_data:
            msg = "Age Updated Succesfully"
            return JsonResponse(msg,safe=False)

        if 'city' in python_data:
            msg = "City Updated Succesfully"
            return JsonResponse(msg,safe=False)
        
        if 'contact' in python_data:
            msg = "Contact Updated Succesfully"
            return JsonResponse(msg,safe=False)
        else:
            msg="Required Fields Are Missing"
            return JsonResponse(msg,safe=False)

    if req.method=='DELETE':
        id = Student.objects.all()
        id.delete()
        msg = "Data Deleted Succesfully"
        return JsonResponse(msg,safe=False)
    
    
    else:
        return JsonResponse(
            "Something Went Wrong",
            safe=False
        )