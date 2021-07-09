from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import TodoListItem

from .forms import TodoListForm
from django.http import HttpResponseRedirect

def index(request):
    all_list = TodoListItem.objects.all()
    return render(request,'index.html',{'all_list':all_list})




#Forms
def add(request):
    if request.method == 'POST':
        form= TodoListForm(request.POST)
        if form.is_valid():
            addtolist = form.save()
            return  HttpResponseRedirect('/')

    else:
        form = TodoListForm()

    return render(request, 'index.html', {'form': form})



def deleteView(request,i):
    y= TodoListItem.objects.filter(id=i)
    y.delete()
    return HttpResponseRedirect('/')

    

