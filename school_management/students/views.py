from django.shortcuts import render,HttpResponse, redirect
from . import models
from. import forms
from django.contrib import messages
from django.views.generic import ListView,UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         course = request.POST.get('course')
#         password = request.POST.get('password')
#         checbox = request.POST.get('checbox')

#         if checbox == 'on':
#             checbox = True
#         else:
#             checbox = False

#         student = models.Student(name=name, email=email, phone=phone, course=course, password=password, checbox=checbox)
#         student.save()
#         return HttpResponse('Student created successfully')
#     return render(request, 'students/index.html')

def create_student(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Created successfully.')
            return redirect('home')
    else:
        form = forms.StudentForm()
    return render(request, 'students/create_student.html', {'form': form})

class CreatStudent(CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name ='students/create_student.html'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Created successfully.')
        return super().form_valid(form)

def home(request):
    students = models.Student.objects.all()
    return render(request, 'students/index.html', {'students': students})



class StudentList(ListView):
    model = models.Student
    template_name ='students/index.html'
    context_object_name ='students'

def update_student(request,id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)
    # form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Edited successfully.')
            return redirect('home')
    return render(request, 'students/create_student.html', {'form': form,'edit': True})


class UpdaeStudent(UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name ='students/create_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Edited successfully.')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context

def delete_student(request,id):
    student = models.Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.SUCCESS, 'Deleted successfully.')
    return redirect('home')

class DeleteStudent(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'students/delete_student.html'

    def delete(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Deleted successfully.')
        return super().delete(request, *args, **kwargs)