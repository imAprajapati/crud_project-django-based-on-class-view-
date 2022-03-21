from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic import View
# Create your views here.

class Add_Show(View):
    def get(self,request):
        fm=StudentRegistration()
        stud=User.objects.all()
        return render(request,'crud/addshow.html',{'form':fm,'st':stud})
    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')


class Delete_Data(View):
    def post(self,request,id):
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


class Update_Data(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'crud/update.html',{'form':fm,'sti':pi})

    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request,'crud/update.html',{'form':fm})


# def add_show(request):
#     if request.method=='POST':
#         fm=StudentRegistration(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm=StudentRegistration()
#     else:
#         fm=StudentRegistration()
#     stud=User.objects.all()
#     return render(request,'crud/addshow.html',{'form':fm,'st':stud})


# def update_data(request,id):
#     if request.method=='POST':
#         pi=User.objects.get(pk=id)
#         fm=StudentRegistration(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi=User.objects.get(pk=id)
#         fm=StudentRegistration(instance=pi)
#     return render(request,'crud/update.html',{'form':fm,'sti':pi})


# def delete_data(request,id):
#     if request.method=='POST':
#         pi=User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')