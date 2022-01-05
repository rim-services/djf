from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

def index(request):
    return render(request, "index.html")

def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                user1 = C_emploi.objects.get(user=user)
                if user1.type == "c_emploi":
                    login(request, user)
                    return redirect("/user_homepage")
            else:
                thank = True
                return render(request, "user_login.html", {"thank":thank})
    return render(request, "user_login.html")

def user_homepage(request):
    if not request.user.is_authenticated:
        return redirect('/user_login/')
    c_emploi = C_emploi.objects.get(user=request.user)
    if request.method=="POST":   
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        telephone = request.POST['telephone']
        sexe = request.POST['sexe']

        c_emploi.user.email = email
        c_emploi.user.first_name = first_name
        c_emploi.user.last_name = last_name
        c_emploi.phone = telephone
        c_emploi.gender = sexe
        c_emploi.save()
        c_emploi.user.save()
        try:
            image = request.FILES['image']
            c_emploi.image = image
            c_emploi.save()
        except:
            pass
        alert = True
        return render(request, "user_homepage.html", {'alert':alert})
    return render(request, "user_homepage.html", {'c_emploi':c_emploi})

def all_jobs(request):
    travail = Travail.objects.all().order_by('-start_date')
    c_emploi = C_emploi.objects.get(user=request.user)
    deposer = Deposer.objects.filter(c_emploi=c_emploi)
    data = []
    for i in deposer:
        data.append(i.travail.id)
    return render(request, "all_jobs.html", {'travail':travail, 'data':data})

def job_detail(request, myid):
    travail = Travail.objects.get(id=myid)
    return render(request, "job_detail.html", {'travail':travail})

def job_apply(request, myid):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    c_emploi = C_emploi.objects.get(user=request.user)
    travail = Travail.objects.get(id=myid)
    date1 = date.today()
    if travail.date_ < date1:
        closed=True
        return render(request, "job_apply.html", {'closed':closed})
    elif travail.date_debut > date1:
        notopen=True
        return render(request, "job_apply.html", {'notopen':notopen})
    else:
        if request.method == "POST":
            cv = request.FILES['cv']
            Deposer.objects.create(travail=travail, entreprise=travail.entreprise, c_emploi=c_emploi, cv=cv, date_depot=date.today())
            alert=True
            return render(request, "job_apply.html", {'alert':alert})
    return render(request, "job_apply.html", {'travail':travail})

def all_applicants(request):
    entreprise = Entreprise.objects.get(user=request.user)
    deposer = Deposer.objects.filter(company=entreprise)
    return render(request, "all_applicants.html", {'deposer':deposer})

def signup(request):
    if request.method=="POST":   
        username = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        telephon = request.POST['telephone']
        sexe = request.POST['sexe']
        image = request.FILES['image']

        # if password1 != password2:
        #     messages.error(request, "Passwords do not match.")
        #     return redirect('/signup')
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1)
        c = C_emploi.objects.create(user=user, telephone=telephon, sexe=sexe, image=image, type="c_emploi")
        user.save()
        c.save()
        return render(request, "user_login.html")
    return render(request, "signup.html")

def company_signup(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        telephon = request.POST['telephone']
        sexe = request.POST['sexe']
        image = request.FILES['image']
        nom_entreprise = request.POST['nom_entreprise']

        # if User.objects.filter(username = username).first():
        #     messages.error(request, "This username is already taken")
        #     return redirect('/signup')
        
        # if password1 != password2:
        #     messages.error(request, "Passwords do not match.")
        #     return redirect('/signup')
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
        entreprise = Entreprise.objects.create(user=user, telephone=telephon, sexe=sexe, image=image, nom_entreprise=nom_entreprise, type="entreprise", status="non_confirmer")
        user.save()
        entreprise.save()
        return render(request, "company_login.html")
    return render(request, "company_signup.html")

def company_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            user1 = Entreprise.objects.get(user=user)
            if user1.type == "entreprise" and user1.status != "non_confirmer":
                login(request, user)
                return redirect("/company_homepage")
        else:
            alert = True
            return render(request, "company_login.html", {"alert":alert})
    return render(request, "company_login.html")

def company_homepage(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    entreprise = Entreprise.objects.get(user=request.user)
    if request.method=="POST":   
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        telephone = request.POST['telephone']
        sexe = request.POST['sexe']

        entreprise.user.email = email
        entreprise.user.first_name = first_name
        entreprise.user.last_name = last_name
        entreprise.phone = telephone
        entreprise.gender = sexe
        entreprise.save()
        entreprise.user.save()

        try:
            image = request.FILES['image']
            entreprise.image = image
            entreprise.save()
        except:
            pass
        alert = True
        return render(request, "company_homepage.html", {'alert':alert})
    return render(request, "company_homepage.html", {'entreprise':entreprise})

def add_job(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    if request.method == "POST":
        titre = request.POST['titre']
        date_debut = request.POST['date_debut']
        date_fin = request.POST['date_fin']
        salaire = request.POST['salaire']
        experience = request.POST['experience']
        adresse = request.POST['adresse']
        skills = request.POST['skills']
        description = request.POST['description']
        user = request.user
        entreprise = Entreprise.objects.get(user=user)
        travail = Travail.objects.create(entreprise=entreprise, titre=titre,date_debut=date_debut, date_fin=date_fin, salaire=salaire, image=entreprise.image, experience=experience, adresse=adresse, skills=skills, description=description, date_creation=date.today())
        travail.save()
        alert = True
        return render(request, "add_job.html", {'alert':alert})
    return render(request, "add_job.html")

def job_list(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    entreprises = Entreprise.objects.get(user=request.user)
    travails = Travail.objects.filter(entreprise=entreprises)
    return render(request, "job_list.html", {'travails':travails})

def edit_job(request, myid):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    travail = Travail.objects.get(id=myid)
    if request.method == "POST":
        title = request.POST['titre']
        start_date = request.POST['date_debut']
        end_date = request.POST['date_fin']
        salary = request.POST['salaire']
        experience = request.POST['experience']
        location = request.POST['adresse']
        skills = request.POST['skills']
        description = request.POST['description']

        travail.titre = title
        travail.salaire = salary
        travail.experience = experience
        travail.adresse = location
        travail.skills = skills
        travail.description = description

        travail.save()
        if start_date:
            travail.date_debut = start_date
            travail.save()
        if end_date:
            travail.date_fin = end_date
            travail.save()
        alert = True
        return render(request, "edit_job.html", {'alert':alert})
    return render(request, "edit_job.html", {'travail':travail})

def company_logo(request, myid):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    travail = Travail.objects.get(id=myid)
    if request.method == "POST":
        image = request.FILES['logo']
        travail.image = image 
        travail.save()
        alert = True
        return render(request, "company_logo.html", {'alert':alert})
    return render(request, "company_logo.html", {'travail':travail})

def Logout(request):
    logout(request)
    return redirect('/')

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_superuser:
            login(request, user)
            return redirect("/all_companies")
        else:
            alert = True
            return render(request, "admin_login.html", {"alert":alert})
    return render(request, "admin_login.html")

def view_applicants(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    c_emploi = C_emploi.objects.all()
    return render(request, "view_applicants.html", {'c_emploi':c_emploi})

def delete_applicant(request, myid):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    c_emploi = User.objects.filter(id=myid)
    c_emploi.delete()
    return redirect("/view_applicants")

def pending_companies(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    entreprises = Entreprise.objects.filter(status="non_confirmer")
    return render(request, "pending_companies.html", {'entreprises':entreprises})

def change_status(request, myid):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    entreprise = Entreprise.objects.get(id=myid)
    if request.method == "POST":
        status = request.POST['status']
        entreprise.status=status
        entreprise.save()
        alert = True
        return render(request, "change_status.html", {'alert':alert})
    return render(request, "change_status.html", {'entreprise':entreprise})

def accepted_companies(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    entreprises = Entreprise.objects.filter(status="Accepted")
    return render(request, "accepted_companies.html", {'entreprises':entreprises})

def rejected_companies(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    entreprises = Entreprise.objects.filter(status="Rejected")
    return render(request, "rejected_companies.html", {'entreprises':entreprises})

def all_companies(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    entreprises = Entreprise.objects.all()
    return render(request, "all_companies.html", {'entreprises':entreprises})

def delete_company(request, myid):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    entreprise = User.objects.filter(id=myid)
    entreprise.delete()
    return redirect("/all_companies")
