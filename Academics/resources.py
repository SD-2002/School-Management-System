from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget,DateWidget
from .models import *

class AttendanceResource(resources.ModelResource):
    class Meta:
        model = Attendance


class MarkAdminResource(resources.ModelResource):
    user = fields.Field(column_name='user', attribute='user', widget=ForeignKeyWidget(User, field='username'))
    Student = fields.Field(column_name='Student', attribute='Student', widget=ForeignKeyWidget(Student, field='Reg_No'))
   # hobby = fields.Field(column_name='hobby', attribute='hobby', widget=ManyToManyWidget(Hobby, field='name'))
    #skill = fields.Field(column_name='skill', attribute='skill', widget=ManyToManyWidget(model=Skill,field='name'))
   

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