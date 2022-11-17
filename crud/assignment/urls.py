from django.urls import path
from assignment import views

urlpatterns = [
    #Users
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('list/delete/<str:email>', views.delete, name="delete"),
    path('list/edit/<str:email>', views.edit, name="edit"),
    path('list/update/', views.update, name="update"),
    path('list/create/', views.create, name="create"),
    path('list/add/', views.add, name="add"),
    #DiseaseType
    path('disease_type/', views.listDT, name='listDT'),
    path('disease_type/editDT/<int:id>', views.editDT, name="editDT"),
    path('disease_type/updateDT/', views.updateDT, name="updateDT"),
    path('disease_type/deleteDT/<int:id>', views.deleteDT, name="deleteDT"),
    path('disease_type/createDT/', views.createDT, name="createDT"),
    path('disease_type/addDT/', views.addDT, name="addDT"),
    #Country
    path('country/', views.listCountry, name='listCountry'),
    path('country/deleteCountry/<str:cname>', views.deleteCountry, name="deleteCountry"),
    path('country/editCountry/<str:cname>', views.editCountry, name="editCountry"),
    path('country/updateCountry/', views.updateCountry, name="updateCountry"),
    path('country/createCountry/', views.createCountry, name="createCountry"),
    path('country/addCountry/', views.addCountry, name="addCountry"),
    #Disease
    path('disease/', views.listDisease, name='listDisease'),
    path('disease/deleteDisease/<str:disease_code>', views.deleteDisease, name="deleteDisease"),
    path('disease/editDisease/<str:disease_code>', views.editDisease, name="editDisease"),
    path('disease/updateDisease/', views.updateDisease, name="updateDisease"),
    path('disease/createDisease/', views.createDisease, name="createDisease"),
    path('disease/addDisease/', views.addDisease, name="addDisease"),
    #Public Servant
    path('servant/', views.listServant, name='listServant'),
    path('servant/deleteServant/<str:email>', views.deleteServant, name="deleteServant"),
    path('servant/editServant/<str:email>', views.editServant, name="editServant"),
    path('servant/updateServant/', views.updateServant, name="updateServant"),
    path('servant/createServant/', views.createServant, name="createServant"),
    path('servant/addServant/', views.addServant, name="addServant"),
    #Doctor
    path('doctor/', views.listDoctor, name='listDoctor'),
    path('doctor/deleteDoctor/<str:email>', views.deleteDoctor, name="deleteDoctor"),
    path('doctor/editDoctor/<str:email>', views.editDoctor, name="editDoctor"),
    path('doctor/updateDoctor/', views.updateDoctor, name="updateDoctor"),
    path('doctor/createDoctor/', views.createDoctor, name="createDoctor"),
    path('doctor/addDoctor/', views.addDoctor, name="addDoctor"),
    #Specialize
    path('spec/', views.listSpec, name='listSpec'),
    path('spec/deleteSpec/<int:id>/<str:email>', views.deleteSpec, name="deleteSpec"),
    path('spec/editSpec/<int:id>/<str:email>', views.editSpec, name="editSpec"),
    path('spec/updateSpec/', views.updateSpec, name="updateSpec"),
    path('spec/createSpec/', views.createSpec, name="createSpec"),
    path('spec/addSpec/', views.addSpec, name="addSpec"),
    #Record
    path('record/', views.listRecord, name='listRecord'),
    path('record/deleteRecord/<str:email>/<str:cname>/<str:disease_code>', views.deleteRecord, name="deleteRecord"),
    path('record/editRecord/<str:email>/<str:cname>/<str:disease_code>', views.editRecord, name="editRecord"),
    path('record/updateRecord/', views.updateRecord, name="updateRecord"),
    path('record/createRecord/', views.createRecord, name="createRecord"),
    path('record/addRecord/', views.addRecord, name="addRecord"),
    #Discover
    path('discover/', views.listDiscover, name='listDiscover'),
    path('discover/deleteDiscover/<str:cname>/<str:disease_code>', views.deleteDiscover, name="deleteDiscover"),
    path('discover/editDiscover/<str:cname>/<str:disease_code>', views.editDiscover, name="editDiscover"),
    path('discover/updateDiscover/', views.updateDiscover, name="updateDiscover"),
    path('discover/createDiscover/', views.createDiscover, name="createDiscover"),
    path('discover/addDiscover/', views.addDiscover, name="addDiscover"),
]
