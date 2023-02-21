from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
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
    
# def pagenotfound(request, name):
      
#     return render(request, "encyclopedia/pagenotfound.html", {
#         "name": name.capitalize()
#     })
                   
        
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]        
        r = re.compile(f".*{searched}")
        newlist = list(filter(r.match, util.list_entries()))           
        
        for entry in util.list_entries():
            if searched.lower() == entry.lower():
                return HttpResponseRedirect(reverse(f"{entry}"))            
        
        if newlist:          
            return render(request, "encyclopedia/search.html", {
                "searchlist": newlist
            })  
            
        else:
            return HttpResponseNotFound(f'<h1>Page {searched} not found</h1>')
        


def create(request):
    pass