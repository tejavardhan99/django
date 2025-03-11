from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.exceptions import NotFound
from .models import Student
from django.contrib.auth.hashers import make_password,check_password 



def demo(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if firstname and lastname and email and password:
            if Student.objects.filter(firstname__exact=firstname):
                messages.error(request,"firstname is already exisisted")
              
            if Student.objects.filter(lastname__exact=lastname):
                messages.error(request,"lastname is already exisisted")
                
            if Student.objects.filter(email__exact=email):
                messages.error(request,"email is already exisisted")
                
            if Student.objects.filter(password__exact=password):
                messages.error(request,"password is already exisisted")
            return redirect ('demo')
            server=Student(firstname=firstname,lastname=lastname,email=email,password=password)
            server.save()
    return render(request,"student.html")        




# displaying data from database
def remo(request):
       
        set=Student.objects.all()       
        return render(request,"database.html",{"student":set})



# accessing data from db using id
def sumo(request,id):
     tet=Student.objects.get(id=id)
     return render(request,"id.html",{"student":tet})


#accessing data from db using firstname
def hi(request,firstname):
    if Student.objects.filter(firstname__exact=firstname):
        l=Student.objects.get(firstname=firstname)
        return render(request,"firstname.html",{"student":l}) 
    else:
        return HttpResponse("firstname is not existed")   




#login form
def hlo(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        if Student.objects.filter(email__exact=email,password__exact=password):
            a=Student.objects.filter(email__exact=email,password__exact=password)
            for i in a:
                 messages.success(request,f"the firstname is {i.firstname}")
                 messages.success(request,f"the lastname is {i.lastname}")
                 messages.success(request,f"the email is {i.email}")
                 messages.success(request,f"the password is {i.password}")
            return redirect('hlo')
        elif Student.objects.filter(firstname__exact=email,password__exact=password):
            a=Student.objects.filter(firstname__exact=email,password__exact=password)
            for i in a:
                 messages.success(request,f"the firstname is {i.firstname}")
                 messages.success(request,f"the lastname is {i.lastname}")
                 messages.success(request,f"the email is {i.email}")
                 messages.success(request,f"the password is {i.password}")
            return redirect('hlo')
        elif Student.objects.filter(lastname__exact=email,password__exact=password):
            a=Student.objects.filter(lastname__exact=email,password__exact=password)
            for i in a:
                 messages.success(request,f"the firstname is {i.firstname}")
                 messages.success(request,f"the lastname is {i.lastname}")
                 messages.success(request,f"the email is {i.email}")
                 messages.success(request,f"the password is {i.password}")
            return redirect('hlo')    

        else:
            messages.error(request,"enter valid mail and password")
            return redirect('hlo')  
    return render(request,"login.html")          



# serializers code
from rest_framework import generics
from .serializers import Master
from rest_framework.response import Response
class Beast(generics.GenericAPIView):
    serializer_class=Master
    def post(self,request,*args,**kwargs):
        try:
            set=self.get_serializer(data=request.data)
            password=request.data.get("password")
            set.is_valid(raise_exception=True)
            set.save()
            return Response({"Message":"success",
                            "Status":200,
                            "Result":set.data,
                            "HasError":False,                             
                             })
        except Exception as e:
            return Response({"Message":"error",
                             "Status":400,
                             "Result":str(e),
                             "HasError":True,
                             })
        
# serializer by using get
class Master(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Master
    def get_object(self):
        pk=self.kwargs.get("pk")
        try:
            return Student.objects.get(pk=pk)     
        except Student.DoesNotExist:
            raise NotFound("student not found")
        


from django.shortcuts import render
from .models import Student
from .serializers import Master

def remo(request):
    students = Student.objects.all()  
    serializer = Master(students, many=True)  
    return render(request, "database.html", {"student": serializer.data})


from rest_framework import generics
class Master(generics.RetrieveAPIView):
    serializer_class=Master
    def get_object(self):
        firstname=self.kwargs.get("firstname")
        try:
            return Student.objects.get(firstname=firstname)
        except Student.DoesNotExist:
            raise NotFound("nooooooooooooooooo")





from rest_framework import generics
from rest_framework.response import Response
from .serializers import Master

class Beast(generics.GenericAPIView):
    serializer_class=Master
    def post(self,request,*args,**kwargs):
        try:
            a=self.get_serializer(data=request.data)
            b=request.data.get("firstname")
            c=request.data.get("lastname")
            if Student.objects.filter(firstname__exact=b,lastname__exact=c):
                return Response({"Message":"firstname and lastname is already existed",
                                "State":400,
                                "HasError":True,
                                })
            elif Student.objects.filter(firstname__exact=b):
                return Response({"Message":"firstname is already existed",
                                "State":400,
                                "Result":b,
                                "HasError":True,
                                })
            elif Student.objects.filter(lastname__exact=c):
                return Response({"Message":"lastname is already existed",
                                "State":400,
                                "Result":c,
                                "HasError":True,
                                })
            else:
                a.is_valid(raise_exception=True)
                a.save()
            
                return Response({"Message":"successful",
                                "State":200,
                                "Result":a.data,
                                "HasError":False,
                                })
        except Exception as e:
            return Response({"Message":"Fail",
                             "Status":400,
                             "Result":Exception(e),
                             "HasError":True,
                             })
                          
                             
                             
# task1:
import re
class Task1(generics.GenericAPIView):
    serializer_class=Master
    def post(self,request,*args,**kwargs):
        try:
            a=self.get_serializer(data=request.data)
            b=request.data.get("email")
            c=request.data.get("password")  
            if (any(i.isupper() for i in c) and  len(c) >= 8 and any(i.isdigit() for i in c) and re.search(r'[@$#!*.%_]', c)):
                        try:
                            a.is_valid(raise_exception=True)
                            a.save()
                            return Response({
                                "Message": "successful",
                                "Status": 200,
                                "Result": a.data,
                                "HasError": False,
                            })
                        except Exception as e:    
                            return Response({
                            "Message": Exception(e), 
                            "Status": 400,
                            "HasError": True,
                            })
            return Response({"Message":"password must contains upper case letter and also the size must be more than 8 char need special caracter",
                                    "Status":400,
                                    "HasError":True,
                                    })
                                    
             
        except Exception as e:
            return Response({"Message":"error",
                             "Status":400,
                             "Result":Exception(e),
                             "HasError":True,
                             })





from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import Master  # Import the serializer
from django.contrib.auth.hashers import make_password

# class UserCreateView(APIView):
#     serializer_class = Master  # Assign the serializer class to be used
    
#     def post(self, request):
#         # Get the serializer instance
#         serializer = self.serializer_class(data=request.data)
        
#         # Check if the data is valid
#         if serializer.is_valid():
#             # Hash the password before saving
#             password = make_password(serializer.validated_data['password'])
#             # Create the student object with the hashed password
#             student_data = serializer.validated_data
#             student_data['password'] = password
            
#             # Create the student record
#             try:
#                 student = Student.objects.create(**student_data)
#                 return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
#         # If the serializer is not valid, return the errors
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserCreateView(generics.GenericAPIView):
    serializer_class=Master
    def post(self,request,*args,**kwargs):
        let=[]
        a=self.get_serializer(data=request.data)
        if a.is_valid():
            jack=request.data.get("password")
            rest=make_password(jack)
            let.append(jack)
            let.append(rest)
            b=a.validated_data
            b['password']=let
            try:
                student=Student.objects.create(**b)
                return Response({"Message":"successfully entered",
                                 "Status":200,
                                 })
            except:
                return Response({"Messages":"bad response"})
        return Response(a.errors)   





class Duck(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=Master
    def get_object(self):
        pk=self.kwargs.get("pk")
        try:
            return Student.objects.get(pk=pk)
        except:
            return Response({"Message":"enter valid id"})
        



# class Goat(generics.GenericAPIView):
#     serializer_class=Master
#     def post(self,request,*args,**kwargs):
#         a=self.get_serializer(data=request.data)
#         b=request.data.get("email")    
#         c=request.data.get("password")
#         if a.is_valid():
#             if Student.objects.filter(firstname__exact=b,password__exact=c) or Student.objects.filter(lastname__exact=b,password__exact=c) or Student.objects.filter(email__exact=b,password__exact=c):
#                 return Response({"Message":"successfully registerd",
#                                     "Status":200,
#                                     "HasError":False,
#                                     })
                
#             return Response({"Message":"enter valid data",
#                                     "Status":400,
#                                     "HasError":True,
#                                     }) 
#         return Response({"Message":"fill all fields",
#                                     "Status":400,
#                                     "HasError":True,
#                                     })  




class Goat(generics.GenericAPIView):
    serializer_class=Master
    def post(self,request,*args,**kwargs):
        a=self.get_serializer(data=request.data)
        b=request.data.get("firstname")    
        c=request.data.get("password")
        if a.is_valid(raise_exception=True):            
            if Student.objects.filter(firstname__exact=b,password__exact=c):
                return Response({"Message":"successfully registerd",
                                    "Status":200,
                                    "HasError":False,
                                    })
            elif Student.objects.filter(lastname__exact=b,password__exact=c):
                return Response({"Message":"successfully registerd",
                                    "Status":200,
                                    "HasError":False,
                                    })
            elif Student.objects.filter(email__exact=b,password__exact=c):
                return Response({"Message":"successfully registerd",
                                    "Status":200,
                                    "HasError":False,
                                    })
            else:
                return Response({"Message":"enter valid data",
                                        "Status":400,
                                        "HasError":True,
                                        }) 
        return Response({"Message":"fill all fields",
                                    "Status":400,
                                    "HasError":True,
                                    })       
    


