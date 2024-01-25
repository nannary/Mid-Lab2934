from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
# def home(request):
#     return render(request,'base.html')
from .models import *

# Create your views here.
def home(request):
    return render(request,'base.html')

def index(request):
    show_flw = Flower.objects.all()
    context = {'Flowerdata': show_flw}
    return render(request, 'index.html', context)

def list(request):
    query = request.GET.get('name')  # รับคำค้นหาจากช่องกรอกคำค้น
    show_flw = Flower.objects.all()

    if query:
        show_flw = Flower.objects.filter(name__icontains=query)
        count_results = show_flw.count()

        if count_results == 0:
            # ถ้าไม่พบข้อมูล
            messages.warning(request, f'ไม่พบข้อมูลสำหรับคำค้น "{query}"')
        else:
            # ถ้าพบข้อมูล
            messages.success(request, f'พบ {count_results} รายการสำหรับคำค้น "{query}"')

    context = {'Flowerdata': show_flw}
    return render(request, 'list.html', context)


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'เข้าสู่ระบบสำเร็จ!')
            return redirect('/')
        else:
            messages.error(request, 'เข้าสู่ระบบผิดพลาด. โปรดตรวจสอบข้อมูลของคุณอีกครั้ง.')
            pass
    return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return render(request, 'login.html')