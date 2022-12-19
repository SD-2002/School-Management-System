from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget


class StudentAdminResource(resources.ModelResource):
    user = fields.Field(column_name='user', attribute='user', widget=ForeignKeyWidget(User, field='username'))
    Student = fields.Field(column_name='Student', attribute='Student', widget=ForeignKeyWidget(Student, field='Reg_No'))
   # hobby = fields.Field(column_name='hobby', attribute='hobby', widget=ManyToManyWidget(Hobby, field='name'))
    #skill = fields.Field(column_name='skill', attribute='skill', widget=ManyToManyWidget(model=Skill,field='name'))
   # gender = fields.Field(column_name='gender', attribute='gender',widget=CustomDropDownWidget(drop_down=PersonDetail.GENDER))

    class Meta:
        model = Student
        fields = (
            'id',
            'user',
           'Student_Name','Reg_No','Address','Taluka','District',
                    'State','pincode'
        )


class StudentAdmin(ImportExportModelAdmin):
    list_display = ['user','Student_Name','Reg_No','Address','Taluka','District',
                    'State','pincode']
    
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Student,StudentAdmin)

class MarkAdminResource(resources.ModelResource):
    user = fields.Field(column_name='user', attribute='user', widget=ForeignKeyWidget(User, field='username'))
    Student = fields.Field(column_name='Student', attribute='Student', widget=ForeignKeyWidget(Student, field='Reg_No'))
   # hobby = fields.Field(column_name='hobby', attribute='hobby', widget=ManyToManyWidget(Hobby, field='name'))
    #skill = fields.Field(column_name='skill', attribute='skill', widget=ManyToManyWidget(model=Skill,field='name'))
   # gender = fields.Field(column_name='gender', attribute='gender',widget=CustomDropDownWidget(drop_down=PersonDetail.GENDER))

    class Meta:
        model = Mark
        fields = (
            'id',
            'user',
            'Reg_No',
            'Subject',
            'Marks',
            'Semester',
            'Year'
        )

class MarkAdmin(ImportExportModelAdmin):
    list_display = ['Reg_No','Subject','Marks','Semester',
                    'Year']
    resource_class = MarkAdminResource
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Mark,MarkAdmin)

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['Reg_No','Student_Name','Standard','Branch','Semester',
                    'Year','Date_of_admission']
    
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Admission,AdmissionAdmin)

class FeedbackformAdmin(admin.ModelAdmin):
    list_display = ['Reg_No','Date','Subject','Feedback']
    
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Feedbackform,FeedbackformAdmin)

#@admin.register(Mark)
#class MarkAdmin(ImportExportModelAdmin):
#    pass
class AttendanceResource(resources.ModelResource):
    class Meta:
        model = Attendance
        fields = (
            'id',
            'user',
            'Name',
            'Roll_No',
            'Attendance_class'
        )


class AttendanceAdmin(ImportExportModelAdmin):
    list_display = ['Roll_No','Attendance_class']
    
    exclude = ['user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Attendance,AttendanceAdmin)