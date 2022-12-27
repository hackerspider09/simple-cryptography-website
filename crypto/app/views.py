from django.shortcuts import render,HttpResponse,redirect
import base64
from .myfunctions import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log,logout as logt 
from django.contrib import messages
# Create your views here.
def home(request):
    if request.user.is_authenticated:
         return render(request,"crypto.html")
    else:
        return redirect("login")


@login_required
def cryption(request):
    obj ={}
    if request.method=="POST":
        uvalue=request.POST['uinput']
        # print(type(uvalue))
        if ('encode_btn' in request.POST):
            obj['somekey_flag']=False
            # print("Encode btn clicked")
            if ("opt1" == request.POST.get('opt')):
                # print("opt1 clicked")
                n = int(request.POST.get('cipher_input'))
                ans = encode_caesar(uvalue,n)
                obj['coded_op']=ans
            elif ("opt2" == request.POST.get('opt')):
                # print("opt1 clicked")
                keyword = request.POST.get('cipher_input')
                key = generateKey(uvalue,keyword)
                # print(key)
                ans = cipherText(uvalue,key)
                obj['coded_op']=ans
                obj['vigenere_key']=key
                obj['somekey_flag']=True
                print(key)
                
            elif ("opt3" == request.POST.get('opt')):
                ans = morse_encrypt(uvalue)
                obj['coded_op']=ans
            elif ("opt4" == request.POST.get('opt')):
                ans = uvalue.swapcase()
                obj['coded_op']=ans
            elif ("opt5" == request.POST.get('opt')):
                encoded_in_ascii = uvalue.encode("ascii")
                encoded_in_base64 = base64.b64encode(encoded_in_ascii)
                encoded_base64 =encoded_in_base64.decode("ascii")
                # print(encoded_in_base64)
                obj['coded_op']=encoded_base64
            elif ("opt6" == request.POST.get('opt')):
                camel_to_snake =to_camel(uvalue)
                obj['coded_op']=camel_to_snake
            return render(request,"crypto.html",obj)

        elif ('decode_btn' in request.POST):
            obj['somekey_flag']=False
            # print("Decode btn clicked")
            if ("opt1" == request.POST.get('opt')):
                # print("opt1 clicked")
                n = int(request.POST.get('cipher_input'))
                ans = decode_caesar(uvalue,n)
                obj['coded_op']=ans
            elif ("opt2" == request.POST.get('opt')):
                # print("opt1 clicked")
                key = request.POST.get('cipher_input')
                ans = originalText(uvalue,key)
                obj['coded_op']=ans
            elif ("opt3" == request.POST.get('opt')):
                ans = morse_decrypt(uvalue)
                obj['coded_op']=ans
            elif ("opt5" == request.POST.get('opt')):
                encoded_in_ascii = uvalue.encode("ascii")
                encoded_in_base64 = base64.b64decode(encoded_in_ascii)
                encoded_base64 =encoded_in_base64.decode("ascii")
                # print(encoded_in_base64)
                obj['coded_op']=encoded_base64
            return render(request,"crypto.html",obj)
    else:
        return render(request,"login.html")

def login(request):
    if request.method=="POST":
        usern=request.POST['username']
        pasword=request.POST['userpass']
        user =authenticate(request,username=usern,password=pasword)
        if user is not None:
            log(request,user)
            messages.success(request, "Login Successful" )
            return redirect('home')
        else:
            messages.warning(request,"Invalid Credential")
            return redirect("login")
    else:
        return render(request,"login.html")

@login_required
def logout(request):
    logt(request)
    return redirect('/')

def signup(request):
    if (request.method == "POST"):
        uname= request.POST['uname']
        usname= request.POST['usname']
        uemail= request.POST['uemail']
        uusername= request.POST['username']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']
        message =[]
        if (not check_email(uemail)):
            message.append("Enter valid email")
        if (pass1!=pass2):
            message.append("Enter same password")
        if (not check_pass(pass1,pass2)):
            message.append("Enter Strong password")
        if (User.objects.filter(username=uname).exists()):
            message.append("Username already exits")
        if (len(message) <=0):
            user=User.objects.create_user(username=uusername,first_name=uname,last_name=usname,email=uemail,password=pass1)
            user.save()
            messages.success(request,"Successfully Account Created")
            return redirect("login")
        else:
            return render(request,"signup.html",{"messages":message})
    return render(request,"signup.html")

