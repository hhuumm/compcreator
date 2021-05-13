from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/',views.about,name="about"),
  path('beginCreate/',views.nameOfComputer,name='create'),
  path('nameComputer/',views.createComputer,name='createComp'),
  path('brandchoice/amd/<int:newComp_id>',views.choseAMD,name='choiceamd'),
  path('brandchoice/intel/<int:newComp_id>',views.choseIntel,name='choiceintel'),
  path('chipchoice/<int:comp_id>/<int:chip_id>',views.addChip,name="addChip"),
  path('mobochoice/<int:comp_id>/<int:mobo_id>',views.addMobo,name="addMobo"),
  path('casechoice/<int:comp_id>/<int:case_id>',views.addCase,name="addCase"),
  path('ramchoice/<int:comp_id>/<int:ram_id>',views.addRam,name="addRam"),
  path('cardchoice/<int:comp_id>/<int:card_id>',views.addCard,name="addCard"),
  path('psuchoice/<int:comp_id>/<int:psu_id>',views.addPsu,name="addSupply"),
  path('myComps',views.myComp,name="myComp"),
  path('deleteComp/<int:comp_id>',views.delComp,name="delComp"),
  path('allComps',views.allComp,name="allComp"),
  path('detailComp/<int:comp_id>',views.compDet,name="compDet"),
  path('accounts/signup/', views.signup, name='signup'),
]