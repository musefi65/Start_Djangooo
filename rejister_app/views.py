from django.shortcuts import render,HttpResponse

# Create your views here.
def reg_log(request):
    return HttpResponse( " *** برای ورود نام کاربری و رمز را وارد کنید ویا در وب سایت ثبت نام کنید  **** ")
