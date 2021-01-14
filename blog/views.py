from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Post
from blog.forms import AddPostForm,EditPostForm, loginForm
# from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


def Add_Post(request):
    form = AddPostForm()
    if request.method=="POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/showpost/")
    return render(request,"add.html",{'form':form})

def Home_Post(request):
    data = Post.objects.all()
    print(data)
    return render(request,"home.html",{"data":data})


def Show_Post(request):
    data = Post.objects.all()
    print(data)
    return render(request,"show.html",{"data":data})

def Edit_Post(request,id):
    obj = Post.objects.get(pk=id)
    form = EditPostForm(instance=obj)
    if request.method=="POST":
        form = EditPostForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/showpost/")
    return render(request,"edit.html",{'form':form ,'obj':obj})

def Delete_Post(request,id):
    obj = Post.objects.get(pk = id)
    obj.delete()
    return redirect("/showpost/")



# def login_request(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now Logged in as {username}")
#                 return redirect("/addpost/")
#             else:
#                 messages.error(request, "Invalid username or password")
#         else:
#             messages.error(request, "Invalid username or password")
#     else:
#         form = AuthenticationForm()
#     return render(request, "login.html", {"form": form})

# def User_Register(request):
#     form = UserCreationForm()
#     if request.method=="POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/login/")
#     return render(request,"user_register.html",{'form':form})
