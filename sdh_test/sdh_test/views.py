from json import dumps as json_dumps

from django.shortcuts import render

def main(request):
    return render(request, 'base.html')