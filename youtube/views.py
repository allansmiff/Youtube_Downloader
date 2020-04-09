from django.shortcuts import render
from pytube import YouTube
import os.path
from django.contrib import messages


def index(request):

    homedir = os.path.expanduser("~")

    dirs = homedir + '/Downloads'

    if request.method == "POST":
        url=request.POST.get('link')
        YouTube(url).streams.first().download(homedir +'/Downloads')
        messages.success(request, 'Vídeo baixado, olhe sua pasta')
    return render(request, 'index.html')
