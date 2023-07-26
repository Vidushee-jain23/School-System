from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    options = [
        ('Female','Female'),
        ('Male','Male')
    ]
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices= options)
    dob = models.DateField()
    fatherName = models.CharField(max_length=50)
    fatherOccupation = models.CharField(max_length=70)
    motherName = models.CharField(max_length=50)
    motherOccupation = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    mobileNo = models.IntegerField()

    def __str__(self):
        return self.name


class Staffs(models.Model):
    options = [
        ('Female','Female'),
        ('Male','Male')
    ]
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices= options)
    dob = models.DateField()
    subject = models.CharField(max_length=50)
    qualification = models.CharField(max_length=80)
    experience = models.CharField(max_length=150)
    mobileNo = models.IntegerField()

class Assignment(models.Model):
    subject = models.CharField(max_length=50)
    homework = models.TextField()

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=20)
    feedback = models.TextField()

class Notice(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    notice = models.TextField()

class StudentLeave(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    days = models.IntegerField()
    leaveReason = models.TextField()

class TeacherLeave(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date = models.DateField()
    days = models.IntegerField()
    leaveReason = models.TextField()



