from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
'''
Sub = (
    ('Python', 'Python Programming'),
    ('SE', 'Software Engineering'),
    ('DBMS', 'Database Management System'),
    ('OS', 'Operating System'),
    ('TOC','Theory of Computation'),
    ('C', 'C')
)

Sem = (
    ('Odd', 'Winter'),
    ('Even','Summer')
)

Yr = (
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Third'),
    ('4', 'Fourth')
) '''

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
    #                          blank=True, on_delete=models.SET_NULL)
    Student_Name = models.CharField(max_length=30)
    Reg_No = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Taluka = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    pincode = models.IntegerField()
    #stu_image = models.ImageField(upload_to='upload/')
    
    def __str__(self):
        return '%s -%s' % (self.Student_Name,self.Reg_No)

    class Meta:
        verbose_name = "Students Information"
        verbose_name_plural = "Students Informations"

class Mark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    Reg_No = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='Registration_Number')
    Subject = models.CharField(max_length=19)
    Marks = models.IntegerField()
    Semester = models.CharField(max_length=10)
    Year = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.Subject)

    class Meta:
        verbose_name = "Mark Information"
        verbose_name_plural = "Mark Informations"

class Admission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
    #                          blank=True, on_delete=models.SET_NULL)
    Student_Name = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='Student_names')
    Reg_No = models.ForeignKey(Student, on_delete=models.CASCADE, null=True,related_name='Registration_No')
    Standard = models.CharField(max_length=50)
    Branch = models.CharField(max_length=20)
    Year = models.CharField(max_length=20)
    Date_of_admission = models.DateField()
    Semester = models.IntegerField(default='443301')
    
    def __str__(self):
        return '%s' % (self.Reg_No)

    class Meta:
        verbose_name = "Admission Information"
        verbose_name_plural = "Admission Informations"

class Feedbackform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    Reg_No = models.ForeignKey(Student, on_delete=models.CASCADE)
    Date = models.DateField()
    Subject = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True)
    Feedback = models.TextField()
    class Meta:
        verbose_name = "Feedback Information"
        verbose_name_plural = "Feedback Informations"

class Attendance(models.Model):
    Roll_No = models.IntegerField()
    Attendance_class = models.IntegerField()
    class Meta:
        verbose_name = "Attendance Information"
        verbose_name_plural = "Attendance Informations"
    def __str__(self):
        return f'{self.Roll_No} - {self.Attendance_class}'
             

