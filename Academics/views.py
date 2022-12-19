from django.shortcuts import render
from Academics.models import Student, Mark, Admission, Feedbackform, Attendance
from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .forms import AttendanceForm



class StudentList(ListView):
    model = Student


#from Academics.forms import StudentForm 
class StudentListCreate(CreateView):
    model = Student
    fields = ['user', 'Student_Name', 'Reg_No', 'Address', 'Taluka', 'District', 'State']

    # fields = ['number', 'year', 'inward_number','next_date',
    #                  'action_other',
    #                 'advocate', 'party_names','opposite_party_names',
    #                 'submitted_date','subject',
    #                 'inward_date','receiver_name',
    #                 'notice_subject','document','document1','document2']

    success_url = reverse_lazy('student')

class StudentListUpdate(UpdateView):
    model = Student
    fields = ['user', 'Student_Name', 'Reg_No', 'Address', 'Taluka', 'District', 'State']
    success_url = reverse_lazy('student')

     # fields = ['number', 'year', 'inward_number','next_date',
    #                  'action_other',
    #                 'advocate', 'party_names','opposite_party_names',
    #                 'submitted_date','subject',
    #                 'inward_date','receiver_name',
    #                 'notice_subject','document','document1','document2']
    # # fields = ['name']
    # success_url = reverse_lazy('student:student1_list')

class StudentListDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student')

	# fields = ['user', 'student_name', 'city', 'address', 'branch', 'education', 'experience']
    # success_url = reverse_lazy('student:student1_list')
class view_home(View):
    def get(self,request):
        return render(request,'home.html',{})

class view_student(View):
    def get(self,request):
        Stud_record = Student.objects.all()
        return render(request,'student.html',{'s':Stud_record})

class view_mark(View):
    def get(self,request):
        mark_record = Mark.objects.all()
        return render(request,'mark.html',{'m':mark_record})

class view_Admission(View):
    def get(self,request):
        Admission_record = Admission.objects.all()
        return render(request,'admission.html',{'a':Admission_record})

class view_feedback(View):
    def get(self, request):
        feedback_record = Feedbackform.objects.all()
        return render(request,'feedback.html',{'f':feedback_record})

class view_Attendance(View):
    def get(self,request):
        Attendance_record = Attendance.objects.all()
        return render(request,'attendance.html',{'t':Attendance_record})

class student1(View):
    def get(self,request):
        if request.method == "POST":
            Student_Name = request.POST.get('Student_Name')
            Reg_No = request.POST.get('Reg_No')
            Address = request.POST.get('address')
            Taluka = request.POST.get('taluka')
            District = request.POST.get('district')
            State = request.POST.get('state')
            pincode = request.POST.get('pincode')
            en=Student(Student_Name=Student_Name,Reg_No=Reg_No,Address=Address,Taluka=Taluka,District=District,State=State,pincode=pincode)
            en.save()
            # Student.objects.create(sname=sname,regno=regno,address=address,taluka=taluka,district=district,state=state,pincode=pincode)

        return render(request,"student1.html")


def usearch(request):
    query = request.GET['query']
    print(type(query))


    #data = query.split()
    data = query
    print(len(data))
    if( len(data) == 0):
        return redirect('publisher')
    else:
                a = data

                # Searching for It
                qs5 =models.Academics.objects.filter(id__iexact=a).distinct()
                qs6 =models.Academics.objects.filter(id__exact=a).distinct()

                qs7 =models.Academics.objects.all().filter(id__contains=a)
                qs8 =models.Academics.objects.select_related().filter(id__contains=a).distinct()
                qs9 =models.Academics.objects.filter(id__startswith=a).distinct()
                qs10 =models.Academics.objects.filter(id__endswith=a).distinct()
                qs11 =models.Academics.objects.filter(id__istartswith=a).distinct()
                qs12 =models.Academics.objects.all().filter(id__icontains=a)
                qs13 =models.Academics.objects.filter(id__iendswith=a).distinct()




                files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

                res = []
                for i in files:
                    if i not in res:
                        res.append(i)


                # word variable will be shown in html when user click on search button
                word="Searched Result :"
                print("Result")

                print(res)
                files = res




                page = request.GET.get('page', 1)
                paginator = Paginator(files, 10)
                try:
                    files = paginator.page(page)
                except PageNotAnInteger:
                    files = paginator.page(1)
                except EmptyPage:
                    files = paginator.page(paginator.num_pages)
   


                if files:
                    return render(request,'publisher/result.html',{'files':files,'word':word})
                return render(request,'publisher/result.html',{'files':files,'word':word})




class Myindex(View):
    def get(self, request):
        attend = Attendance.objects.all()

        if request.method == 'POST':
            form = AttendanceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = AttendanceForm()        

        context = {
            "attend": attend,
            "form": form
        }

        return render(request, 'chartapp/index1.html', context)
