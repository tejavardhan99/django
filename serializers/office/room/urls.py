# from .views import Student_Views,Diff,Marks_Views,Address_Update,Teacher_Details,Greater_marks
# from django.urls import path

# urlpatterns = [
#     path("demo/",Diff.as_view()),
#     path("update/<int:pk>/",Address_Update.as_view()),
#     path("post/<int:pk>/",Student_Views.as_view()),
#     path("marks/",Marks_Views.as_view()),
#     path("details/<int:id>/",Teacher_Details.as_view()),
#     path("higher/",Greater_marks.as_view())
# ]




from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import (
    Student_Views, Diff, Marks_Views,  
    Teacher_Details, Greater_marks, Decreasing_marks, schools_teachers, Same_name, Teachers_assigned,
    School_name, Image, Decode, Enough_Class, Address_Update, Create_Jwt, Login_Jwt,Particular_School,LoginSession
)

# Swagger Schema View with JWT Authentication
schema_view = get_schema_view(
    openapi.Info(
        title="Student Management API",
        default_version="v1",
        description="API documentation for Student & Teacher Management",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("demo/", Diff.as_view(), name="demo"),
    path("post/<int:pk>/", Student_Views.as_view(), name="get"),
    path("marks/", Marks_Views.as_view(), name="marks"),
    path("details/<int:id>/", Teacher_Details.as_view(), name="details"),
    path("higher/", Greater_marks.as_view(), name="higher"),
    path("Decreasing_marks/", Decreasing_marks.as_view(), name="Decreasing_marks"),
    path("schools_teachers/", schools_teachers.as_view(), name="schools_teachers"),
    path("Same_name/", Same_name.as_view(), name="Same_name"),
    path("Teachers_assigned/", Teachers_assigned.as_view(), name="Teachers_assigned"),
    path("School_name/<str:name>/", School_name.as_view(), name="School_name"),
    path("Encode/", Image.as_view(), name="encode_base64"),
    path("Decode/<int:id>/", Decode.as_view(), name="Decode_base64"),
    path("NESTED_JSON/", Enough_Class.as_view(), name="NESTED_JSON"),
    path("get,up,del/<int:pk>/", Address_Update.as_view(), name="ALL"),
    path('Create_Jwt/register/', Create_Jwt.as_view(), name='register'),
    path("Login_Jwt/", Login_Jwt.as_view(), name="Login"),
    path("Particular_School/<int:pk>/",Particular_School.as_view(),name="Particular_School"),
    path("LoginSession/",LoginSession.as_view(),name="LoginSession"),
    
    # Swagger Endpoints with JWT Support
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
    re_path(r"^swagger.json$", schema_view.without_ui(cache_timeout=0), name="swagger-json"),
]




# from django.urls import path
# from graphene_django.views import GraphQLView
# from .schema import schema  # Import your GraphQL schema
# from .views import (
#     Student_Views, Diff, Marks_Views,  
#     Teacher_Details, Greater_marks,Decreasing_marks,schools_teachers,Same_name,Teachers_assigned,
#     School_name
# )



# urlpatterns = [
#     # Your existing API endpoints
#     path("demo/", Diff.as_view(), name="demo"),
#     path("post/", Student_Views.as_view(), name="post"),
#     path("marks/", Marks_Views.as_view(), name="marks"),
#     path("details/<int:id>/", Teacher_Details.as_view(), name="details"),
#     path("higher/", Greater_marks.as_view(), name="higher"),
#     path("Decreasing_marks/", Decreasing_marks.as_view(), name="Decreasing_marks"),
#     path("schools_teachers/", schools_teachers.as_view(), name="schools_teachers"),
#     path("Same_name/", Same_name.as_view(), name="Same_name"),
#     path("Teachers_assigned/", Teachers_assigned.as_view(), name="Teachers_assigned"),
#     path("School_name/<str:name>/", School_name.as_view(), name="School_name"),

#     # GraphQL Endpoint
#     path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),  # Enables GraphiQL interface in browser
# ]
