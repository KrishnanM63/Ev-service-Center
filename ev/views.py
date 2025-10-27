from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import add, add_mechanics, add_service_center,bookings, contact
from .forms import login_frm, register
from django.contrib.auth.decorators import login_required
# -------------------------
# Home Page
# -------------------------
def home_page(request):
    service_centers = add_service_center.objects.all()
    return render(request, "home.html",{'service_centers':service_centers})


# -------------------------
# Login Page
# -------------------------
def login_page(request):
    form = login_frm()
    if request.method == "POST":
        form = login_frm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = form.cleaned_data['role']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session["role"]= person
                messages.success(request, "Login Successfully!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password!")
    return render(request, "login.html", {'form': form})


# -------------------------
# Register Page
# -------------------------
def register_page(request):
    form = register()
    if request.method == "POST":
        form = register(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Register successfully!")
            return redirect("login")
    return render(request, "register.html", {'form': form})

# -------------------------
# Admin Page
# -------------------------
def user_page(request):
   
    return render(request, "user.html")


# -------------------------
# Add Branch Owner
# -------------------------
def add_owners(request):
    if request.method == "POST":
        add.objects.create(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            branch_name=request.POST.get("branch_name"),
            contact=request.POST.get("contact"),
            location=request.POST.get("location"),
            image=request.FILES.get("image"),
            descriptions=request.POST.get("descriptions")
        )
        messages.success(request, "Branch owner added successfully!")
    return render(request, "add_ownes.html")


# -------------------------
# Add Service Center
# -------------------------
def add_service(request):
    if request.method == "POST":
        add_service_center.objects.create(
            username_service=request.POST.get("username_service"),
            email_service=request.POST.get("email_service"),
            branch_name_service=request.POST.get("branch_name_service"),
            contact_service=request.POST.get("contact_service"),
            location_service=request.POST.get("location_service"),
            image_service=request.FILES.get("image_service"),
            descriptions_service=request.POST.get("descriptions_service")
        )
        messages.success(request, "Service center added successfully!")
    return render(request, "add_service_center.html")


# -------------------------
# User Search Bunks
# -------------------------
def user_ds(request):
    query = request.GET.get('q', '')
    bunks = add.objects.none()  # default empty queryset

    if query:
        bunks = add.objects.filter(
            username__icontains=query
        ) | add.objects.filter(
            location__icontains=query
        ) | add.objects.filter(
            branch_name__icontains=query
        )

    context = {
        'bunks': bunks,
        'query': query,
    }
    return render(request, 'search.html', context)


# -------------------------
# Search Service Places
# -------------------------
def search_serviceplace(request):
    query = request.GET.get('q', '')
    if query:
        # Filter service centers by name or location containing the query (case-insensitive)
        bunks_dtails = add_service_center.objects.filter(
            branch_name_service__icontains=query
        ) | add_service_center.objects.filter(
            location_service__icontains=query
        )
    else:
        bunks_dtails = add_service_center.objects.all()  # Show nothing if no query

    return render(request, 'search_service.html', {
        'bunks_dtails': bunks_dtails,
        'query': query
    })

# -------------------------
# Bookings Page
# -------------------------
def bookings_page(request):
    return render(request, "bookin.html")



def add_mechanic(request):
    if request.method == "POST":
        name_mechanic = request.POST.get("name_mechanic")
        contact_mechanic = request.POST.get("contact_mechanic")
        email_mechanic = request.POST.get("email_mechanic")
        specialization_mechanic = request.POST.get("specialization_mechanic")
        location_mechanic = request.POST.get("location_mechanic")
        available_from_mechanic = request.POST.get("available_from_mechanic")
        available_to_mechanic = request.POST.get("available_to_mechanic")
        
        add_mechanics.objects.create(
           name_mechanic=name_mechanic,
           contact_mechanic =contact_mechanic,
           email_mechanic =email_mechanic,
           specialization_mechanic =specialization_mechanic,
           location_mechanic =location_mechanic,
           available_from_mechanic =available_from_mechanic,
           available_to_mechanic =available_to_mechanic
  
        )
        
                
    return render(request,"add_mechanic.html")

def booking_page(request,service_center_id):
    service_center = add_service_center.objects.get(id=service_center_id)
    if request.method =="POST":
        name_booking = request.POST.get("name_booking")
        email_booking = request.POST.get("email_booking")
        number_booking = request.POST.get("number_booking")
        vehicle_number = request.POST.get("vehicle_number")
        service_date = request.POST.get("service_date")
        notes_booking = request.POST.get("notes_booking")
   
        
        bookings.objects.create(
          name_booking=name_booking,
          email_booking = email_booking,
          number_booking = number_booking,
          vehicle_number = vehicle_number,
          service_date=service_date,
          notes_booking=notes_booking,
          service_center=service_center,
          

            
        )
        
        
        
    return render(request,"bookings.html",{'service_center_id':service_center_id})

def service_center_ds(request):
    bookingss = bookings.objects.all()
    mechanics = add_mechanics.objects.all()
    contacts  = contact.objects.all()
    branches =add_service_center.objects.all()
    return render(request,"service_cenetr.html",{'bookingss':bookingss,'mechanics':mechanics,'contacts':contacts,'branches':branches})

def delete_machanic(request,pk):
    product = get_object_or_404(add_mechanics,pk=pk)
    product.delete()
    return redirect('service_center')
def update_mechanic(request,pk):
    mechanic = get_object_or_404(add_mechanics,pk=pk)
    if request.method == "POST":
        mechanic.name_mechanic = request.POST.get("name_mechanic")
        mechanic.contact_mechanic = request.POST.get("contact_mechanic")
        mechanic.email_mechanic = request.POST.get("email_mechanic")
        mechanic.specialization_mechanic = request.POST.get("specialization_mechanic")
        mechanic.location_mechanic = request.POST.get("location_mechanic")
        mechanic.available_from_mechanic = request.POST.get("available_from_mechanic")
        mechanic.available_to_mechanic = request.POST.get("available_to_mechanic")
        mechanic.save()
        
        return redirect('service_center')
    return render(request,"update_mechanic.html",{'mechanic':mechanic})    

def mechanic_dashbord(request):
    bookingss = bookings.objects.all()

    return render(request,"mechanic_dashbord.html",{'bookingss':bookingss})

def update_staus(request,pk):
    product = get_object_or_404(bookings,pk=pk)
    if request.method == "POST":
        new_status = request.POST.get("status")
        product.status = new_status
        product.save()
        return redirect("mechanic_dashbord") 
    
def mybooking_page(request):
    bookingss = bookings.objects.all()
    return render(request,"mybooking.html",{'bookingss':bookingss})    
def lagout_page(request):
    logout(request)
    return redirect("home")

def contact_page(request):
    if request.method == "POST":
        name_contact = request.POST.get("name_contact")
        email_contact = request.POST.get("email_contact")
        message_contact = request.POST.get("message_contact")
        
        contact.objects.create(
            name_contact=name_contact,
            email_contact =email_contact,
            message_contact = message_contact
        )
    return render(request,"contact.html")
def delete_service_center(request,pk):
    product = get_object_or_404(add_service_center,pk=pk)
    product.delete()
    return redirect("service_center")
def edit_branch(request,pk):
    branch =  get_object_or_404(add_service_center,pk=pk)
    if request.method == "POST":
          
            
            branch.username_service = request.POST.get("username_service")
            branch.email_service = request.POST.get("email_service")
            branch.branch_name_service = request.POST.get("branch_name_service")
            branch.contact_service  = request.POST.get("contact_service")
            branch.location_service = request.POST.get("location_service")
            if 'image_service' in request.FILES:
                    branch.image_service = request.FILES['image_service']
            branch.save()
            return redirect("service_center")
    return render(request,"edit_branch.html",{'branch':branch})
     
      

    
    
    
    
    
    
    
    