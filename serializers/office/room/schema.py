import graphene
from graphene_django.types import DjangoObjectType
from .models import Student, Teacher  # Import your models

# Define DjangoObjectTypes for Student and Teacher
class StudentType(DjangoObjectType):
    class Meta:
        model = Student

class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher

# Input types for mutations
class StudentInput(graphene.InputObjectType):
    name = graphene.String()
    age = graphene.Int()
    school = graphene.String()

class TeacherInput(graphene.InputObjectType):
    name = graphene.String()
    subject = graphene.String()

# Mutation class for creating Student and Teacher records
class CreateStudent(graphene.Mutation):
    class Arguments:
        student_data = StudentInput(required=True)

    student = graphene.Field(StudentType)

    def mutate(self, info, student_data):
        student = Student.objects.create(**student_data)
        return CreateStudent(student=student)

class CreateTeacher(graphene.Mutation):
    class Arguments:
        teacher_data = TeacherInput(required=True)

    teacher = graphene.Field(TeacherType)

    def mutate(self, info, teacher_data):
        teacher = Teacher.objects.create(**teacher_data)
        return CreateTeacher(teacher=teacher)

# Query class for fetching students and teachers
class Query(graphene.ObjectType):
    all_students = graphene.List(StudentType)
    all_teachers = graphene.List(TeacherType)

    def resolve_all_students(self, info):
        return Student.objects.all()

    def resolve_all_teachers(self, info):
        return Teacher.objects.all()

# Mutation class to include the defined mutations
class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    create_teacher = CreateTeacher.Field()

# Schema definition
schema = graphene.Schema(query=Query, mutation=Mutation)

