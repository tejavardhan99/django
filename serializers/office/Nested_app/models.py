from djongo import models

class CodeSet(models.Model):
    CodeType = models.CharField(max_length=50)
    CodeValue = models.CharField(max_length=50)

    class Meta:
        abstract = True

class PersonalDetails(models.Model):
    ProfilePic = models.URLField()
    UserName = models.CharField(max_length=100)
    DoB = models.DateField()
    Gender = models.CharField(max_length=10)
    CodeSet = models.EmbeddedField(model_container=CodeSet)

    class Meta:
        abstract = True

class UserRegistration(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone = models.CharField(max_length=20)
    Password = models.CharField(max_length=100)
    PersonalDetails = models.EmbeddedField(model_container=PersonalDetails)

    class Meta:
        abstract = True

class LocationDetails(models.Model):
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=10)
    Address = models.TextField()

    class Meta:
        abstract = True

class UserProfileDetails(models.Model):
    ShortBrief = models.TextField()
    LongBrief = models.TextField()

    class Meta:
        abstract = True

class User(models.Model):
    UserType = models.CharField(max_length=50)
    UserRegistration = models.EmbeddedField(model_container=UserRegistration, null=True)
    LocationDetails = models.EmbeddedField(model_container=LocationDetails, null=True)
    UserProfileDetails = models.EmbeddedField(model_container=UserProfileDetails, null=True)

    def __str__(self):
        return f"{self.UserRegistration.FirstName} {self.UserRegistration.LastName}" if self.UserRegistration else "No Name"
