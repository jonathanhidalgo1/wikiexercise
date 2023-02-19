from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import re

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def css(request):
    return render(request, "encyclopedia/css.html", {
        "texts": util.get_entry("CSS")
    })
    
def django(request):
    return render(request, "encyclopedia/django.html", {
        "texts": util.get_entry("Django")
    })

def git(request):
    return render(request, "encyclopedia/git.html", {
        "texts": util.get_entry("Git")
    })

def html(request):
    return render(request, "encyclopedia/html.html", {
        "texts": util.get_entry("HTML")
    })
    
def python(request):
    return render(request, "encyclopedia/python.html", {
        "texts": util.get_entry("Python")
    })
    
def pagenotfound(request, name):
    pass
    
    # return render(request, "encyclopedia/pagenotfound.html", {
    #     "name": name.capitalize()
    # })
    #colocar uma condicao para aceita a pagina search
    
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        if searched in util.list_entries():
            return render(request, f"encyclopedia/{searched}.html",{
        "texts": util.get_entry(searched)
    })
        else:            
            r = re.compile(f".*{searched}")
            newlist = list(filter(r.match, util.list_entries()))       
            return render(request, "encyclopedia/search.html", {
                "searchlist": newlist
            })
    
        
    
    
    # if "Git" in util.list_entries():
    #     return render(request, "encyclopedia/search.html", {
    #         "searchlist": util.list_entries()
    #     })
    # else:
    #     pass
    

    
    