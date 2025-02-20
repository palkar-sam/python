from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
#import todo forms and models
from todo.models import Todo
from todo.forms import TodoForm

# Create your views here.
def index(request):

    item_list = Todo.objects.order_by("-date")
    if(request.method == "POST"):
        form = TodoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('todo')
    form = TodoForm()
    page = {
        "forms":form,
        "list": item_list,
        "title":"This is TODO LIST",
    }
    return render(request, 'todo/index.html', page)

#@login_required
#@permission_required('todo.delete_todo', raise_exception=True)
def remove(request, item_id):
    item = get_object_or_404(Todo, id=item_id)
    item.delete()
    messages.info(request, "Item removed successfully !!!")
    return redirect('todo')
    