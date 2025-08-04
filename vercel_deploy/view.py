from django.shortcuts import render
from httpx import request



def หน้าหลัก(request):
    return render(request, 'หน้าหลัก.html')


def เกี่ยวกับ(request):
    return render(request, 'เกี่ยวกับ.html')


def ติดต่อ(request):
    return render(request, 'ติดต่อ.html')

def วนซ้ำ(request):
    return render(request, 'วนซ้ำ.html')
