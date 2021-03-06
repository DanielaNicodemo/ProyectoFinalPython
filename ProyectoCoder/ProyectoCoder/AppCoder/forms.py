from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class ContactoFormulario(forms.Form):
    nombre= forms.CharField()
    mail= forms.CharField(required=True)
    telefono= forms.IntegerField()
    mensaje= forms.CharField()

class LabialesFormulario(forms.Form):    
    nombre = forms.CharField(max_length=40)
    stock= forms.IntegerField()
    precio= forms.IntegerField()


class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField(required=True)  



class UserRegisterForm(UserCreationForm):

    username= forms.CharField() 
    email= forms.CharField() 
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput) 
    password2= forms.CharField(label="Repetir la contraseña", widget= forms.PasswordInput)

    last_name= forms.CharField()  
    first_name= forms.CharField() 

          # imagen_avatar= forms.ImageField(required= False)


class UserEditForm(UserCreationForm):


    email= forms.CharField(label="Ingrese su email:") 
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput) 
    password2= forms.CharField(label="Repetir la contraseña", widget= forms.PasswordInput)

    last_name= forms.CharField()  
    first_name= forms.CharField() 

    class Meta:
        model= User
        fields= ["email", "password1", "password2", "last_name", "first_name"]



   
      