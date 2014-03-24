from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib
import re

def home(request):
    #message = request.GET('txtweb-message')
    usn="4jn11mca07";
    cleartrip="http://59.90.15.173:8080/simple/jspfiles/formobile.jsp?usn1="+usn+"&submit=click"
    url = urllib.urlopen(cleartrip)
    soup = BeautifulSoup(url) 
    tag1=soup.text
    return render(request, "base.html", {'hello': tag1 })
      