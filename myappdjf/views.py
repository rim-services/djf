
from urllib import response
from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from itertools import islice

from django.views.decorators.csrf import csrf_exempt

from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

import time
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.decorators import api_view
from .serializers import *
import json


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
#hkj

@api_view(['GET','POST'])
def les_annonces_emploi(request):
    if not request.user.is_authenticated:
        return Response('pas connecter',status=status.HTTP_401_UNAUTHORIZED)
    travail = Travail.objects.all().order_by('-date_debut')
    c_emploi = C_emploi.objects.get(user=request.user)
    deposer = Deposer.objects.filter(c_emploi=c_emploi)
    if request.method == "POST":
        key = request.POST['motcle']
        localite = request.POST['pays']
        
        data = []
        for i in deposer:
            data.append(i.travail.id)
        
       
        
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
        browser.get("https://www.linkedin.com/jobs/search?keywords="+key+"&location="+localite+"&position=1&pageNum=0")
        # recuperation des jobs titres
        jobs_titres=browser.find_elements_by_class_name("base-search-card__title")
        tt=[] 
        iterator = islice(jobs_titres, 25)
        for i in iterator:
            tt.append(i.text)
        # entreprises qui recrutent
        jobs_entreprises=browser.find_elements_by_class_name("base-search-card__subtitle")
        ne=[] 
        iterator = islice(jobs_entreprises, 25)
        for i in iterator:
            ne.append(i.text)
            
            
        jobs_adresses=browser.find_elements_by_class_name("job-search-card__location")
        ja=[]
        iterator = islice(jobs_adresses, 25)
        for i in iterator:
            ja.append(i.text)
            
            
        jobs_date=browser.find_elements_by_tag_name("time")
        # jobs_date=browser.find_elements_by_class_name("job-search-card__listdate--new job-search-card__listdate")
        jd=[]  
        iterator = islice(jobs_date, 25)
        for i in iterator:
            jd.append(i.text)
          
          
            
        jobs_links = browser.find_elements_by_tag_name('a')
        jl= [elem.get_attribute('href') for elem in jobs_links]
        iterator = islice(jl, 25)
        for elem in iterator:
            jl.append(elem)
        
        
        
            
            
        jobss=[ne,tt,ja,jd,jl]
        listjobs=[]
        for item in range(0,len(jobss[3])):
            singlejob=[]
            singlejob.append(jobss[0][item])
            singlejob.append(jobss[1][item])
            singlejob.append(jobss[2][item])
            singlejob.append(jobss[3][item])
            singlejob.append(jobss[4][item])
            listjobs.append(singlejob)
        time.sleep(5)
        browser.close() 
        x=0
        y=1
        return render(request, "les_annonces_emploi.html", {'travail':travail, 'data':data, 'listjobs':listjobs, 'x':x, 'y':y})
    
    if request.method == 'GET':
        x=1
        y=0
        #user2 = User.objects.get(id=1)
        c = C_emploi.objects.get(user=request.user)
        id = c.user_id
        languesm = LangueMaitrise.objects.filter(c_emploi_id=id)
        
    
        lm = []
        for i in languesm:
            lm.append(i.langue.nom)
        key=""
        for i in lm:
            key=key+" "+i
        #if in path
        #browser=webdriver.Chrome("chromedriver.exe") 
        
        
        #if in local
        browser = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))   
        
        
        #if in heroku
        #browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        
        #browser = webdriver.Chrome()  
        # jkdn
        
        browser.get("https://www.linkedin.com/jobs/search?keywords="+key+"&location=""&position=1&pageNum=0")
        jobs_titres=browser.find_elements_by_class_name("base-search-card__title")
        tt=[] 
        iterator = islice(jobs_titres, 25)
        for i in iterator:
            tt.append(i.text)
        
        jobs_entreprises=browser.find_elements_by_class_name("base-search-card__subtitle")
        ne=[] 
        iterator = islice(jobs_entreprises, 25)
        for i in iterator:
            ne.append(i.text)
        jobs_adresses=browser.find_elements_by_class_name("job-search-card__location")
        ja=[]
        iterator = islice(jobs_adresses, 25)
        for i in iterator:
            ja.append(i.text)
        jobs_date=browser.find_elements_by_tag_name("time")
        # jobs_date=browser.find_elements_by_class_name("job-search-card__listdate--new job-search-card__listdate")
        jd=[]  
        iterator = islice(jobs_date, 25)
        for i in iterator:
            jd.append(i.text)
            
        jobs_links = browser.find_elements_by_tag_name('a')
        jl= [elem.get_attribute('href') for elem in jobs_links]
        iterator = islice(jl, 25)
        for elem in iterator:
            jl.append(elem)
        
        
        
        images = browser.find_elements_by_tag_name('img')
        ji=[]
        iterator = islice(images, 25)
        for elem in iterator:
            ji.append(elem.get_attribute('src'))
        
        
        jobss=[ne,tt,ja,jd,jl,ji]
        listjobs=[]
        for item in range(0,len(jobss[3])):
            singlejob=[]
            singlejob.append(jobss[0][item])
            singlejob.append(jobss[1][item])
            singlejob.append(jobss[2][item])
            singlejob.append(jobss[3][item])
            singlejob.append(jobss[4][item])
            singlejob.append(jobss[5][item])
            listjobs.append(singlejob)
        time.sleep(5)
        browser.close() 
    
    back = []
    for item in listjobs:
        obj = {
            "nom": item[0],
            "entreprise": item[1],
            "adresse": item[2],
            "date": item[3],
            "link": item[4],
            "img": item[5]
        }
        back.append(obj)
      
    #js = json.dumps(back)
    js= back
    # return js
    return Response(js, status=status.HTTP_200_OK)
    #return render(request, "les_annonces_emploi.html",{'x':x, 'y':y,'listjobs':listjobs, 'lm':lm})



@api_view(['GET','POST'])
def rest(request):
    if request.method == 'GET':
        c = Langue.objects.all()
        serializer = LangueSerializer(c, many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        try:
            n = request.data["nom"]
            d = request.data["description"]
            lang = Langue.objects.create(nom=n, description=d)
            return Response(
            "success",
            status=status.HTTP_201_CREATED
        )
        except:
            return Response(
                "error, invalid data",
                status=status.HTTP_400_BAD_REQUEST
            )
            
            
def scrapp(request):
    
    list=[[1,2,3],["med","sidi","ali"],["brk","psidi","pali"]]
    listjobs=[]
    for item in range(0,len(list[0])):
        singlejob=[]
        singlejob.append(list[0][item])
        singlejob.append(list[1][item])
        singlejob.append(list[2][item])
        listjobs.append(singlejob)
        
    return render(request, "jobscrapped.html",{'listjobs':listjobs})

def index(request):
    return render(request, "index.html")

def stat(request):
    t = Travail.objects.count()
    e = Entreprise.objects.count()
    c = C_emploi.objects.count()
    return render(request, "statistiques.html", {'t':t, 'e':e, 'c':c})
# @csrf_exempt


@api_view(['GET'])
def deconnecter(request):
    if request.user.is_authenticated:
        logout(request)
        return Response("success",status=status.HTTP_201_CREATED )
        
    else:
        return Response("tu n'est pas connecter",status=status.HTTP_201_CREATED ) 
    #return redirect('/')
    
@csrf_exempt
@api_view(['POST'])
def connexion_chercheur_emploi(request): 
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response("Authenticated",status=status.HTTP_201_CREATED)
        else:
            return Response("error, invalid data",
                   status=status.HTTP_400_BAD_REQUEST)
            
    else:
            return Response("only post method ",status=status.HTTP_404_NOT_FOUND ) 
@csrf_exempt
@api_view(['GET','POST'])
def page_home_chercheur_emploi(request):
    if not request.user.is_authenticated:
        return Response('pas connecter',status=status.HTTP_401_UNAUTHORIZED)
    c_emploi = C_emploi.objects.get(user=request.user)
    if request.method=="POST":   
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        telephone = request.POST['telephone']
        sexe = request.POST['sexe']
        description = request.POST['description']

        c_emploi.user.email = email
        c_emploi.user.first_name = first_name
        c_emploi.user.last_name = last_name
        c_emploi.phone = telephone
        c_emploi.sexe = sexe
        c_emploi.description = description
        
        c_emploi.save()
        c_emploi.user.save()
        try:
            image = request.FILES['image']
            c_emploi.image = image
            c_emploi.save()
        except:
            pass
        serializer = C_emploiSerializer(c_emploi, many=False)
        return Response(serializer.data)
    
    if request.method=="GET":   
        serializer = C_emploiSerializer(c_emploi, many=False)
        return Response(serializer.data)
    #return render(request, "page_home_chercheur_emploi.html", {'c_emploi':c_emploi})
@api_view(['GET'])   
def detail_annonce(request, myid):
    if not request.user.is_authenticated:
        return Response('pas connecter',status=status.HTTP_401_UNAUTHORIZED)
    if request.method == "GET":
        travail = Travail.objects.get(id=myid)
        serializer = TravailSerializer(travail, many=False)
        return Response(serializer.data)
    else:
        return Response("not get method",status=status.HTTP_401_UNAUTHORIZED)
    #return render(request, "detail_annonce.html", {'travail':travail})

def deposer_pour_emploi(request, myid):
    if not request.user.is_authenticated:
        return Response('pas connecter',status=status.HTTP_401_UNAUTHORIZED)
    c_emploi = C_emploi.objects.get(user=request.user)
    travail = Travail.objects.get(id=myid)
    date1 = date.today()
    if travail.date_fin < date1:
        return Response("closed", status=status.HTTP_200_OK)
    elif travail.date_debut > date1:
        
        return Response("pas encore ouvert", status=status.HTTP_200_OK)
    else:
        if request.method == "POST":
            cv = request.FILES['cv']
            Deposer.objects.create(travail=travail, entreprise=travail.entreprise, c_emploi=c_emploi, cv=cv, date_depot=date.today())
            
            return Response("done", status=status.HTTP_200_OK)
    return Response("erreur survenue", status=status.HTTP_404_NOT_FOUND)

def les_interesses(request):
    entreprise = Entreprise.objects.get(user=request.user)
    deposer = Deposer.objects.filter(entreprise=entreprise)
    return render(request, "les_interesses.html", {'deposer':deposer})


@csrf_exempt
@api_view(['GET','POST'])
def inscription_chercheur_emploi(request):
    if request.method=="POST":   
        email = request.POST['email']
        username = request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        telephon = request.POST['telephone']
        sexe = request.POST['sexe']
        image = request.FILES['image']
        experience = request.POST['experience']
        adresse = request.POST['adresse']
        skills = request.POST['skills']
        description = request.POST['description']
        

        if password1 != password2:
            msg = "les mot de passes ne sont pas siyani"
            #return render(request, "inscription_chercheur_emploi.html", {'msg':msg})
            return Response(msg,status=status.HTTP_401_UNAUTHORIZED)
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
        c = C_emploi.objects.create(user=user, telephone=telephon, sexe=sexe, image=image, type="c_emploi",experience=experience, adresse=adresse, skills=skills, description=description)
        user.save()
        c.save()
        serializer = C_emploiSerializer(c, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #msg = "inscription faite avec succées, vous pouvez se connecter maintenant"
        #return render(request, "connexion_chercheur_emploi.html", {'msg':msg})
    msg = "Désolé, only post method"
    return response(msg,status=status.HTTP_404_NOT_FOUND)
    #return render(request, "inscription_chercheur_emploi.html", {'msg2':msg})

def inscription_entreprise(request):
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
        return render(request, "connexion_entreprise.html")
    return render(request, "inscription_entreprise.html")

def connexion_entreprise(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            user1 = Entreprise.objects.get(user=user)
            if user1.type == "entreprise" and user1.status == "Accepted":
                login(request, user)
                return redirect("/page_home_entreprise")
            elif user1.type == "entreprise" and user1.status == "non_confirmer":
                msg2 = "Votre entreprise a besoin de confirmation, veuillez patientez"
                return render(request, "connexion_entreprise.html", {"msg2":msg2})
            elif user1.type == "entreprise" and user1.status == "Rejected":
                msg2 = "Votre entreprise a été rejeté."
                return render(request, "connexion_entreprise.html", {"msg2":msg2})
        else:   
            msg = "Les données sont  erronés, ressayer"
            return render(request, "connexion_entreprise.html", {"msg":msg})
    return render(request, "connexion_entreprise.html")

def page_home_entreprise(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_entreprise")
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
        return render(request, "page_home_entreprise.html", {'alert':alert})
    return render(request, "page_home_entreprise.html", {'entreprise':entreprise})

def publier_annonce(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_entreprise")
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
        return render(request, "publier_annonce.html", {'alert':alert})
    return render(request, "publier_annonce.html")

def liste_des_annonces(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_entreprise")
    entreprises = Entreprise.objects.get(user=request.user)
    travails = Travail.objects.filter(entreprise=entreprises)
    return render(request, "liste_des_annonces.html", {'travails':travails})

def modifier_annonce(request, myid):
    if not request.user.is_authenticated:
        return redirect("/connexion_entreprise")
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
        return render(request, "modifier_annonce.html", {'alert':alert})
    return render(request, "modifier_annonce.html", {'travail':travail})

def logo_entreprise(request, myid):
    if not request.user.is_authenticated:
        return redirect("/connexion_entreprise")
    travail = Travail.objects.get(id=myid)
    if request.method == "POST":
        image = request.FILES['logo']
        travail.image = image 
        travail.save()
        alert = True
        return render(request, "logo_entreprise.html", {'alert':alert})
    return render(request, "logo_entreprise.html", {'travail':travail})



def connexion_administrateur(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("/stat")
        else:   
            msg = "Les données sont  erronés,ressayer"
            return render(request, "connexion_administrateur.html", {"msg":msg})
    return render(request, "connexion_administrateur.html")


def rien(request):
    
    return render(request, "cnx_admin.html")
def liste_chercheurs_emploi(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    c_emploi = C_emploi.objects.all()
    return render(request, "liste_chercheurs_emploi.html", {'c_emploi':c_emploi})

def supprimer_un_chercheur_emploi(request, myid):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    c_emploi = User.objects.filter(id=myid)
    c_emploi.delete()
    return redirect("/liste_chercheurs_emploi")

def entreprises_non_confirmer(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    entreprises = Entreprise.objects.filter(status="non_confirmer")
    return render(request, "entreprises_non_confirmer.html", {'entreprises':entreprises})

def change_status(request, myid):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    entreprise = Entreprise.objects.get(id=myid)
    if request.method == "POST":
        status = request.POST['status']
        entreprise.status=status
        entreprise.save()
        alert = True
        return render(request, "change_status.html", {'alert':alert})
    return render(request, "change_status.html", {'entreprise':entreprise})

def entreprises_confirmer(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    entreprises = Entreprise.objects.filter(status="Accepted")
    return render(request, "entreprises_confirmer.html", {'entreprises':entreprises})

def entreprises_rejeter(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    entreprises = Entreprise.objects.filter(status="Rejected")
    return render(request, "entreprises_rejeter.html", {'entreprises':entreprises})

def tous_les_entreprises(request):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    entreprises = Entreprise.objects.all()
    return render(request, "tous_les_entreprises.html", {'entreprises':entreprises})

def supprimer_entreprise(request, myid):
    if not request.user.is_authenticated:
        return redirect("/connexion_administrateur")
    entreprise = User.objects.filter(id=myid)
    entreprise.delete()
    return redirect("/tous_les_entreprises")


@csrf_exempt
@api_view(['GET','POST'])
def freelancerHomePage(request):
    
    if request.method == "POST":
        mot = request.POST['motcle']
        c_emplois = C_emploi.objects.filter(description__contains=mot)
        serializer = C_emploiSerializer(c_emplois, many=True)
        return Response(serializer.data)
     
    if request.method == 'GET':
        c = C_emploi.objects.all()
        serializer = C_emploiSerializer(c, many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
def languesmaitrise(request):
    if not request.user.is_authenticated:
        return Response('pas connecter',status=status.HTTP_401_UNAUTHORIZED)
    if request.method == "POST":
        langueid = request.POST['idid']
        c_emploi = C_emploi.objects.get(user=request.user)
        langue = Langue.objects.get(id=langueid)
        id = c_emploi.user_id
        
        lm = LangueMaitrise.objects.create(c_emploi=c_emploi, langue=langue)
        lm.save()
        serializer = LangueMaitriseSerializer(lm, many=False)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    if request.method == "GET":
        c_emploi = C_emploi.objects.get(user=request.user)
        #langues = LangueMaitrise.objects.filter(c_emploi=c_emploi)
        lang = Langue.objects.all()
        serializer = LangueSerializer(lang, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
        # return render(request, "languesmaitrise.html", {'langues':langues, 'lang':lang})




@csrf_exempt
@api_view(['GET','POST'])
def detailfreelancer(request):
    if request.method == "POST":
        c_emploi = C_emploi.objects.get(id=request.data['id'])
        iddd = c_emploi.user_id
        lm = LangueMaitrise.objects.filter(c_emploi_id=iddd)
        serializer1 = C_emploiSerializer(c_emploi, many=False)
        serializer2 = LangueMaitriseSerializer(lm, many=True)
        data = []
        data.append(serializer1.data)
        data.append(serializer2.data)
        
        return Response(data,status=status.HTTP_200_OK)
    else:
        return Response("erreur", status=status.HTTP_404_NOT_FOUND)