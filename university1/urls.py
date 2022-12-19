"""university1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from Academics.views import view_student,view_mark,view_Admission,view_feedback,StudentList,view_home,student1,usearch,view_Attendance,Myindex
from Academics.views import StudentListCreate,StudentListUpdate,StudentListDelete 
from django.urls import re_path as url

#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #url('',view_home,name='link_home'),
    url(r'^student',view_student.as_view(),name='link_student'),
    url(r'^student1',student1.as_view(),name="link_st"),
    url(r'^mark',view_mark.as_view(),name='link_mark'),
    url(r'^admission',view_Admission.as_view(),name='link_admission'),
    url(r'^feedback',view_feedback.as_view(),name='link_feedback'),
    url(r'^attendance',view_Attendance.as_view(),name='link_attend'),
    url(r'',view_home.as_view(),name='link_home'),
    url(r'usearch/', usearch, name='usearch'),
    url(r'^index',Myindex.as_view(), name='link_Myindex'),
    #url(r'^student1',student1,name="stu"),
    #url('', StudentList.as_view(template_name='student.html'), name='student_list'),

    #url('new', StudentListCreate.as_view(template_name='student.html'), name='Student_new'),
	#url('edit/<int:pk>', StudentListUpdate.as_view(template_name='student.html'), name='Student_edit'),
  	#url('delete/<int:pk>', StudentListDelete.as_view(template_name='student.html'), name='Student_delete'),

]   


#if settings.DEBUG:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
