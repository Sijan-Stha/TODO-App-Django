from django.shortcuts import render, HttpResponseRedirect
from todo_app.models import ToDo
# Create your views here.



# CRUD OPERATIONS IN DJANGO HERE: 


def todo_list(request):
    todos = ToDo.objects.all()
    return render(
        request,
        "bootstrap/todo_list.html",
        {"todos": todos}
        )

def create_todo(request):
    if request.method == 'POST':
        #save the form data here:
        title = request.POST['title']

        ToDo.objects.create(title = title)
        return HttpResponseRedirect('/')
    return render(request, "bootstrap/todo_create.html")

def delete_todo(request, pk):
    todo = ToDo.objects.get(pk = pk)
    todo.delete()

    return HttpResponseRedirect('/')

def update_todo(request, pk):
    todo = ToDo.objects.get(pk = pk)
    if request.method == 'POST':
        title = request.POST['title']
        todo.title = title
        todo.save()
        return HttpResponseRedirect('/')
    else:
        return render(
            request,
            "bootstrap/todo_update.html",
            {"todo": todo}
        )