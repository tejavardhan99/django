from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import student_serializer,school_serializer,teacher_serializer,Image_Serializer,Enough_Serializer,User_Serializer,Jwt_Login_serializer,Session_serializer
from .models import Student,Teacher,School,Different_Model,Enough,User

# class Diff(generics.GenericAPIView):
#     serializer_class=school_serializer
#     def post(self,request,*args,**kwargs):
#         try:

#             print("sdfghjdfghnjmk")
#             a=self.get_serializer(data=request.data)
#             print(a,"dfghjmkfvgbhnjmfvgbhnjcvgbhnjmbhnjmk,")
#             a.is_valid(raise_exception=True)
#             a.save()
#             return Response({"Message":"successfiul",
#                              "Status":200,
#                              "Result":a.data,
#                              "HasError":False,
#                              }) 
#         except Exception as e:
#             return Response({"Message":"fail",
#                              "Status":400,
#                              "Result":Exception(e),
#                              "HasError":True,
#                              })


class Diff(generics.GenericAPIView):
    serializer_class=Session_serializer
    def post(self,request,*args,**kwargs):
        a=self.get_serializer(data=request.data)
        if a.is_valid(raise_exception=True):
            a.save()
            return Response({"Message":"completed"})








class Address_Update(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = school_serializer
    def get_object(self):
        id= self.kwargs.get('pk')
        try:
            return School.objects.get(pk=id)
        except Student.DoesNotExist:
            print("sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")




from .serializers import teacher_serializer,get_teacher_serializer,school_serializer,get_master_serializer


# class teacher_class(generics.GenericAPIView):
#     serializer_class=master_serializer
#     def post(self,request,*args,**kwargs):
#         a=self.get_serializer(data=request.data)
#         if a.is_valid(raise_exception=True):
#             ss=a.save()
#             dd=get_master_serializer(ss).data
#             return Response({"Messages":"completed",
#                              "Result":dd,
#                              })




# class Student_Views(generics.GenericAPIView):
#     serializer_class=teacher_serializer
#     def post(self,request,*args,**kwargs):
#         a=self.get_serializer(data=request.data)
        
#         if a.is_valid(raise_exception=True):
#             a.save()
#             return Response({"Message":"completed"})




# #multiple relations:

class Student_Views(generics.RetrieveAPIView):
    serializer_class=teacher_serializer
    def get(self,request,*args,**kwargs):
        school_id=self.kwargs.get("pk")
        a=Teacher.objects.filter(school_id=school_id)
        teacher_ids = [teacher.id for teacher in a]
        b=teacher_serializer(a,many=True).data
        ss=School.objects.get(id=school_id)
        ss1=school_serializer(ss).data   
        q=Student.objects.filter(teacher_id__in=teacher_ids)  
        w=student_serializer(q,many=True).data
        return Response({
                        "School_Details":ss1,
                        "Teacher_Details":b,
                        "Student_Details":w})







class Marks_Views(generics.RetrieveAPIView):
    serializer_class=student_serializer
    def get(self,request,*args,**kwargs):
        a=Student.objects.all()
        b=[i.marks for i in a]
        marks=max(b)
        Student_access=Student.objects.filter(marks=marks)
        Student_access1=student_serializer(Student_access,many=True).data
        teacher_id=[i.teacher_id.id for i in Student_access]
        Teacher_access=Teacher.objects.filter(id__in=teacher_id)
        Teacher_access1=teacher_serializer(Teacher_access,many=True).data
        school_id=[i.school_id.id for i in Teacher_access]
        school_access=School.objects.filter(id__in=school_id)
        school_access1=school_serializer(school_access,many=True).data
        return Response({"Message":"completed",
                         "Student_Result":Student_access1,
                         "Teacher_Result":Teacher_access1,
                         "School_Result":school_access1,
                         }) 
    
    



# school address update
# class Address_Update(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class=school_serializer
#     def get_object(self):
#         id=self.kwargs.get("pk")
#         return School.objects.get(pk=id)
    

#fetch all teachers working in a specific school

class Teacher_Details(generics.RetrieveAPIView):
    serializer_class=school_serializer
    def get(self,request,*args,**kwargs):
        school_id=self.kwargs.get("id")
        a=Teacher.objects.filter(school_id__exact=school_id)
        teacher_details=teacher_serializer(a,many=True).data
        b=School.objects.filter(id__exact=school_id)
        school_details=school_serializer(b,many=True).data
        return Response({
                        "School_details":school_details,
                        "teacher_details":teacher_details})



#add a new teacher to a school

# class Diff(generics.GenericAPIView):
#     serializer_class=teacher_serializer
#     def post(self,request,*args,**kwargs):
#         a=self.get_serializer(data=request.data)
#         if a.is_valid(raise_exception=True):
#             a.save()
#             return Response({"Message":"completed",
#                              "Result":a.data,
#                              })



# all students who scored more than 80 marks

# class Greater_marks(generics.RetrieveAPIView):
#     serializer_class=student_serializer
#     def get(self,request,*args,**kwargs):
#         student_details=Student.objects.filter(marks__gt=90)
#         student_marks=[i.marks for i in student_details]
#         b=Student.objects.filter(marks__in=student_marks)
#         a=student_serializer(b,many=True).data
#         return Response({"Message":a})



#all teachers who teach the subject "py"

# class Greater_marks(generics.RetrieveAPIView):
#     serializer_class=teacher_serializer
#     def get(self,request,*args,**kwargs):
#         subject=Teacher.objects.filter(subject="ds")
#         id=[i.id for i in subject]
#         teacher_details=Teacher.objects.filter(id__in=id)
#         a=teacher_serializer(teacher_details,many=True).data
#         print(id,"dfghjdfghj")
#         return Response({"Message":a})


#students whose email contains "gmail.com"

# class Greater_marks(generics.RetrieveAPIView):
#     serializer_class=student_serializer
#     def get(self,request,*args,**kwargs):
#         subject=Student.objects.filter(Email__endswith="gmail.com")
#         id=[i.id for i in subject]
#         student_details=Student.objects.filter(id__in=id)
#         a=student_serializer(student_details,many=True).data
#         return Response({"Message":a})


#the total number of students in the database

class Greater_marks(generics.RetrieveAPIView):
    serializer_class=teacher_serializer
    def get(self,request,*args,**kwargs):
        a=Teacher.objects.count()
        return Response({"result":a}) 
       



# fetch students in descending order of their marks

class Decreasing_marks(generics.RetrieveAPIView):
    serializer_class=student_serializer
    def get(self,request,*args,**kwargs):
        student_details=Student.objects.all()
        student_marks=[i.marks for i in student_details]    #not working properly
        sorted_data=sorted(student_marks)
        match=Student.objects.filter(marks__in=sorted_data)
        result=student_serializer(match,many=True).data
        return Response({"Result":result}) 
    


#all schools along with their teachers in a single query

class schools_teachers(generics.RetrieveAPIView):
    serializer_class=school_serializer
    def get(self,request,*args,**kwargs):
        school_details=School.objects.all()
        ids=[i.id for i in school_details]
        school_details=School.objects.filter(id__in=ids)
        school=school_serializer(school_details,many=True).data
        teacher_details=Teacher.objects.filter(school_id__in=ids)
        stored_data=teacher_serializer(teacher_details,many=True).data
        return Response({
                        "SCHOOL_RESULT":school,
                        "TEACHER_RESULT":stored_data})




#all students who have the same first name as another student

class Same_name(generics.RetrieveAPIView):
    serializer_class=student_serializer
    def get(self,request,*args,**kwargs):
        student_details=Student.objects.all()
        firstname=[i.firstname for i in student_details]
        for i in firstname:
            a=Student.objects.filter(firstname=i)
            b=student_serializer(a,many=True).data
        return Response({"RESULT":b})





#retrieve all schools that don’t have any teachers assigned yet

class Teachers_assigned(generics.RetrieveAPIView):
    serializer_class=school_serializer
    def get(self,request,*args,**kwargs):
        school_details=School.objects.all()
        ids=[i.id for i in school_details]
        try:
            for i in ids:
                if not Teacher.objects.filter(school_id=i):
                    school_id=School.objects.filter(id=i)
                    a=school_serializer(school_id,many=True).data
                    return Response({"Message":a})
        except:
            return Response({"Message":"all teachers are busy!"})




#retrieve a specific school by its name

class School_name(generics.RetrieveAPIView):
    serializer_class=school_serializer
    def get(self,request,*args,**kwargs):
        school_name=self.kwargs.get("name")
        school_details=School.objects.filter(school_name=school_name)
        result=school_serializer(school_details,many=True).data
        return Response({"RESULT":result})

# ###################################################################
# from django.shortcuts import render
# from rest_framework import generics
# from .models import Different_Model
# import base64

# def im(img):
#     return img.read() 


# class Image(generics.GenericAPIView):
#     def post(self, request, *args, **kwargs):
#         if 'myimage' not in request.FILES:
#             return render(request, 'img.html', {'error': 'No file uploaded'})

#         img = request.FILES.get('myimage')                                                       

#         a = Different_Model()
#         a.image = im(img)
#         a.save()        
#         return render(request, 'img.html', {'message': 'Image uploaded successfully!'})

#########################################################################

# def im(img):
#     return img.read() 

# class Image(generics.GenericAPIView):
#     serializer_class = Image_Serializer

#     def post(self, request, *args, **kwargs):
#         if 'myimage' not in request.FILES:
#             return render(request, 'img.html', {'error': 'No file uploaded'})

#         img = request.FILES['myimage']
#         binary_img = im(img)  # Get binary data

#         # Save binary image in database
#         a = Different_Model(image=binary_img)
#         a.save()

#         return render(request, 'img.html', {'message': 'Image uploaded successfully!'})


##########################################################################

###  " ENCODING THE DATA FROM USER DATA "

import base64

class Image(generics.GenericAPIView):
    serializer_class=Image_Serializer
    def post(self,request,*args,**kwargs):
        a=self.get_serializer(data=request.data)
        if a.is_valid(raise_exception=True):
            some_data=a.validated_data
            b=some_data['full_name']
            encode=base64.b64encode(b.encode()).decode() 
            some_data['full_name']=encode
            a.save()
            return Response({"RESULT":"Successfully encoded the data!!"})
        


#  " DECODING DATA FROM DATA_BASE "

class Decode(generics.RetrieveAPIView):
    serializer_class=Image_Serializer
    def get(self,request,*args,**kwargs):
        id=self.kwargs.get("id")
        b=Different_Model.objects.get(id=id)
        decode=b.full_name
        c=base64.b64decode(decode)
        return Response({
                        "id":id,
                        "RESULT":c})




#NESTED_JSON DATA:

# class Enough_Class(generics.GenericAPIView):
#     serializer_class=Enough_Serializer
#     def post(self,request,*args,**kwargs):
#         a=self.get_serializer(data=request.data)
#         if a.is_valid(raise_exception=True):
#             b=a.data.get("full_id")
#             d=Different_Model.objects.filter(id=b)
#             lost=Image_Serializer(d,many=True).data
#             for i in lost:
#                  j=i['full_name']
#             a=a.data
#             a["full_name"]=j
#             return Response({"RESULT":a,
#                              })




class Enough_Class(generics.GenericAPIView):
    serializer_class=Enough_Serializer
    def post(self,request,*args,**kwargs):
        a=self.get_serializer(data=request.data)
        if a.is_valid(raise_exception=True):
            b=a.data.get("full_id")
            d=Different_Model.objects.filter(id=b)
            lost=Image_Serializer(d,many=True).data
            for i in lost:
                j=i["full_name"]
            c=a.data
            c["full_name"]=j
            main_data=self.get_serializer(data=c)
            if main_data.is_valid(raise_exception=True):
                main_data.save()
            return Response({"RESULT":c})

###  " REGISTRATION FOR JWT "  ###

from rest_framework_simplejwt.tokens import RefreshToken

class Create_Jwt(generics.GenericAPIView):
    serializer_class=User_Serializer
    def post(self,request,*args,**kwargs):
        a=self.get_serializer(data=request.data)
        if a.is_valid(raise_exception=True):
            n=a.save()
            refresh=RefreshToken.for_user(n)
            return Response({
                "RESULT":a.data,
                "REFRESH":str(refresh),
                "ACCESS":str(refresh.access_token),
                            })


###  " LOGIN FOR JWT "  ###
from django.contrib.auth import login
# class Login_Jwt(generics.GenericAPIView):
#     serializer_class=Jwt_Login_serializer
#     def post(self,request,*args,**kwargs):
#         a=self.get_serializer(data=request.data)
#         if a.is_valid(raise_exception=True):
#             b=a.validated_data["username"]
#             login(request, b)
#             return Response({"Message":Jwt_Login_serializer(b,many=True).data})


import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class Login_Jwt(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        # 🔹 Replace with your actual third-party API URL
        THIRD_PARTY_API_URL = "https://third-party-api.com/auth/token/"

        # 🔹 Send user credentials to third-party API
        payload = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(THIRD_PARTY_API_URL, json=payload)
            response_data = response.json()

            # 🔹 If authentication is successful, return the third-party JWT token
            if response.status_code == 200:
                return Response({
                    "message": "Login successful!",
                    "access": response_data.get("access_token"),
                    "refresh": response_data.get("refresh_token")
                })
            else:
                return Response({"error": "Invalid credentials"}, status=400)

        except requests.exceptions.RequestException as e:
            return Response({"error": "Failed to connect to third-party API", "details": str(e)}, status=500)




### how many students in a particular school ####

class Particular_School(generics.RetrieveAPIView):
    serializer_class=school_serializer
    def get(self,request,*args,**kwargs):
        id=self.kwargs.get("pk")
        teacher_id=Teacher.objects.filter(school_id=id)
        total_teacher=teacher_serializer(teacher_id,many=True).data
        required_id=[i.id for i in teacher_id]
        student_id=Student.objects.filter(teacher_id__in=required_id)
        total_student=student_serializer(student_id,many=True).data
        return Response({"Message":total_student})
    



from django.utils.timezone import now
from django.contrib.auth.hashers import check_password
from django.contrib.sessions.models import Session
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Session_Model
from .serializers import Session_serializer

class LoginSession(generics.GenericAPIView):
    queryset = Session_Model.objects.all()
    serializer_class = Session_serializer
    permission_classes = [AllowAny]

    def post(self, request):
        """Login API - Creates a session with a 10-minute expiry"""
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = Session_Model.objects.get(username=username)
        except Session_Model.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if not check_password(password, user.password):
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        # Start session
        request.session["user_id"] = user.id
        request.session["session_start"] = now().timestamp()
        request.session.set_expiry(10)  # 10 minutes expiry

        return Response({"message": "Login successful! Session active for 10 minutes."}, status=status.HTTP_200_OK)

    def get(self, request):
        """Check if the session is still active"""
        if "user_id" not in request.session:
            return Response({"error": "Session expired. Please log in again."}, status=status.HTTP_401_UNAUTHORIZED)

        session_start = request.session.get("session_start")
        if session_start and (now().timestamp() - session_start > 10):
            request.session.flush()  # Clear session
            return Response({"error": "Session expired. Please log in again."}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"message": "Session is still active."}, status=status.HTTP_200_OK)

    def delete(self, request):
        """Logout API - Ends session"""
        request.session.flush()  # Clears the session
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

