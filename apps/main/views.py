from django.shortcuts import render, redirect
from .models import User, Hat
from django.contrib import messages
import bcrypt 

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def home(request):
    if "user_id" not in request.session:
        #print("someone was unauthorized")
        return redirect('/')
    user = User.objects.get(id=request.session["user_id"])
    context = {
        #"name": user.first_name + " " + user.last_name
        "user": user
    }
    return render(request, "main/homepage.html", context)

def register(request):
    form = request.POST

    errors = User.objects.basic_validator(form)
    if len(errors) > 0:
        #print(errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    user = User.objects.create(first_name=form["first_name"], last_name=form["last_name"],
                                email=form["email"], password=bcrypt.hashpw(form["password"].encode(), bcrypt.gensalt()).decode())
    
    #print("\n\n\n\n", request.POST)
    request.session["user_id"] = user.id
    return redirect("/homepage")

def login(request):
    form = request.POST
    try:
        user = User.objects.get(email = form["email"])
    except:
        #print("User does not exist!")
        messages.error(request, "Check your email and password")
        return redirect("/")

    if bcrypt.checkpw(form["password"].encode(), user.password.encode()):
        request.session["user_id"] = user.id
        return redirect("/homepage")
    
    #print("user entered the wrong password")
    messages.error(request, "Check your email and password")
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect("/")

def show_hat(request, hat_id):
    context = {
        "hat": Hat.objects.get(id=hat_id)
    }
    return render(request, "main/show-hat.html", context)

def create_hat(request):
    post = request.POST
    Hat.objects.create(brand=post["brand"], color=post["color"], size=post["size"], owner=User.objects.get(id=request.session["user_id"]))
    return redirect("/homepage")

def add_hat(request):
    return render(request, "main/add-hat.html")

def edit_hat(request, hat_id):
    context = {
        "hat": Hat.objects.get(id=hat_id)
    }
    return render(request, "main/edit-hat.html", context)

def delete_hat(request, hat_id):
    Hat.objects.get(id=hat_id).delete()
    return redirect("/homepage")

def update_hat(request, hat_id):
    post = request.POST
    hat = Hat.objects.get(id=hat_id)
    hat.brand = post["brand"]
    hat.color = post["color"]
    hat.size = post["size"]
    hat.save()
    #Hat.objects.update()
    return redirect("/homepage")