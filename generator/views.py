from django.shortcuts import render
import string
import random
def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")


def password(request):
    x=""
    letras=string.ascii_letters
    numeros = string.digits
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    otros= string.punctuation
    numero_de_caracteres = int(request.GET.get("length"))
    mitad = numero_de_caracteres // 2
    tercera = numero_de_caracteres // 3

    x = random.choices(minusculas, k=numero_de_caracteres)
    if request.GET.get("Checkbox"):
        x = random.choices(letras,k=numero_de_caracteres)
    if request.GET.get("Checkbox_number"):
        x = random.choices(minusculas, k=mitad) + random.choices(numeros, k=numero_de_caracteres-mitad)
    if request.GET.get("Checkbox_number") and request.GET.get("Checkbox"):
        x = random.choices(letras, k=mitad) + random.choices(numeros, k=numero_de_caracteres-mitad)
    if request.GET.get("Checkbox_special"):
        x = random.choices(minusculas, k=mitad)+random.choices(otros,k=numero_de_caracteres-mitad)
    if request.GET.get("Checkbox") and request.GET.get("Checkbox_special"):
        x = random.choices(minusculas, k=tercera) + random.choices(mayusculas,k=tercera)+ random.choices(otros, k= numero_de_caracteres - (tercera*2))
    if request.GET.get("Checkbox") and request.GET.get("Checkbox_special")and request.GET.get("Checkbox_number"):
        x = random.choices(letras, k=tercera) + random.choices(otros, k=tercera) + random.choices(numeros,k= numero_de_caracteres-(tercera*2))
    x.sort()
    x = "".join(x)
    return render(request, "password.html", {"Contra": x})

