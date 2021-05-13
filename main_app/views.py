from django.shortcuts import render,redirect
from .models import CustomComputer,PSU,Chipset,Case,Graphics,OS,Ram,MotherBoard
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import login

#Thisgs to work on, add a PSU to the new Comp object, add costs and TDP consumption
def compDet(request,comp_id):
  thisComp=CustomComputer.objects.get(id=comp_id)
  return render(request,'computers/details.html',{'computer':thisComp})


def allComp(request):
  comps=CustomComputer.objects.all()
  return render(request,"computers/allComps.html",{'computers':comps})
def myComp(request):
  comps=CustomComputer.objects.filter(user=request.user)
  return render(request,'computers/myComps.html',{'computers':comps})
  
def delComp(request,comp_id):
  CustomComputer.objects.get(id=comp_id).delete()
  return redirect('myComp')


def addPsu(request,comp_id,psu_id):
  newComp=CustomComputer.objects.get(id=comp_id)
  newPsu=PSU.objects.get(id=psu_id)
  newComp.psu=newPsu
  newComp.price += newPsu.price
  newComp.save()
  return render(request,'computers/confirmation.html',{'computer':newComp})


# Create your views here.
def addCard(request,comp_id,card_id):
  #save from old page
  newComp=CustomComputer.objects.get(id=comp_id)
  newGraphics=Graphics.objects.get(id=card_id)
  newComp.gpu=newGraphics
  newComp.price+=newGraphics.price
  newComp.save()
  #stuff for new page
  newPsu=PSU.objects.all()
  return render(request,'computers/Psu.html',{'supplies':newPsu,'computer':newComp})
  

def addRam(request,comp_id,ram_id):
  #save from old page
  newComp=CustomComputer.objects.get(id=comp_id)
  newRam=Ram.objects.get(id=ram_id)
  newComp.ram=newRam
  newComp.price+=newRam.price
  newComp.save()
  #stuff for new page
  newGraphics=Graphics.objects.all()
  return render(request,'computers/Graphics.html',{'graphics':newGraphics,'computer':newComp})

def addCase(request,comp_id,case_id):
  #save from old page
  newComp=CustomComputer.objects.get(id=comp_id)
  newCase=Case.objects.get(id=case_id)
  newComp.case=newCase
  newComp.price+=newCase.price
  newComp.save()
  #stuff for new page
  newRam=Ram.objects.all()
  return render(request,'computers/Ram.html',{'rams':newRam,'computer':newComp})

def addMobo(request,comp_id,mobo_id):
  #save from old page
  newComp=CustomComputer.objects.get(id=comp_id)
  newMobo=MotherBoard.objects.get(id=mobo_id)
  newComp.mobo=newMobo
  newComp.price+=newMobo.price
  newComp.save()
  #stuff for new page
  matchingCases=Case.objects.filter(form=newMobo.form)
  return render(request,'computers/Case.html',{'cases':matchingCases,'computer':newComp})

def addChip(request,comp_id,chip_id):
  #save from old page
  newComp=CustomComputer.objects.get(id=comp_id)
  newChip=Chipset.objects.get(id=chip_id)
  newComp.cpu=newChip
  newComp.price=0
  newComp.price+=newChip.price
  newComp.save()
  #stuff for new page
  matchingMobos=MotherBoard.objects.filter(socket=newChip.brand)
  return render(request,'computers/Mobo.html',{'mobos':matchingMobos,'computer':newComp})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def nameOfComputer(request):
    nform=NameForm()
    return render(request,'computers/name.html',{'nameForm':nform})

def createComputer(request):
    form = NameForm(request.POST)
    if form.is_valid():
        new_computer=form.save(commit=False)
        new_computer.user=request.user
        new_computer.save()
        return render(request,'computers/PBrand.html',{'computer':new_computer})
    else:
        nform=NameForm()
        return render(request,'computers/name.html',{'nameForm':nform})

def choseAMD(request,newComp_id):
    newComp=CustomComputer.objects.get(id=newComp_id)
    pOptions=Chipset.objects.filter(brand='A')
    return render(request,'computers/Processor.html',{'computer':newComp,'processors':pOptions})

def choseIntel(request,newComp_id):
    newComp=CustomComputer.objects.get(id=newComp_id)
    pOptions=Chipset.objects.filter(brand='I')
    return render(request,'computers/Processor.html',{'computer':newComp,'processors':pOptions})

def signup(request):
  print(request)
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
