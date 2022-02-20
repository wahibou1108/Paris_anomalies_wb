from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("<h2>Page accueil index</h2>")
    return render(request, "index.html", context={"date":datetime.today()})

def questions(request, num_question):                  # CETTE FONCTION REGROUPE 3 FICHIERS QUESTIONS
    if num_question in ["1","2","3"]:
        return render(request, f"q{num_question}.html")
    return render(request, "not_found.html")



