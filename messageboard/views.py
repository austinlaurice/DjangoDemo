from django.shortcuts import render
from .models import Message
# Create your views here.


def MessageBoard(request):
    if request.method == 'GET':
        messages = Message.objects.all().order_by('-pub_time')
        return render(request, 'messageboard.html', {'msg': messages})
    elif request.method == 'POST':
        author = request.POST['author']
        content = request.POST['content']
        Message.objects.create(author=author, content=content)
        messages = Message.objects.all().order_by('-pub_time')
        return render(request, 'messageboard.html', {'msg': messages})

