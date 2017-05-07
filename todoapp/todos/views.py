from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from todos.models import Todo


def index(request):
    items = Todo.objects.all()

    return render(request, 'index.html', {'items': items})


def create(request):
    return render(request, 'create.html', {
        'form_type': 'create'
    })


def save(request):
    # Get the form data from the request.
    title = request.POST.get('title')
    description = request.POST.get('description')

    if title is None or title.strip() == '':
        messages.error(request, 'Item not saved. Please provide the title.')
        return redirect(request.META.get('HTTP_REFERER'))



    # Get hidden form data.
    form_type = request.POST.get('form_type')
    id = request.POST.get('id')

    print('Form type received:', form_type)
    print('Form todo id received:', id)

    if form_type == 'create':
        # Create a new todo item with the data.
        todo = Todo.objects.create(
            title=title,
            description=description,
            created_at=timezone.now()
        )
        print('New Todo created: ', todo.__dict__)
    elif form_type == 'edit' and id.isdigit():
        todo = Todo.objects.get(pk = id)
        print('Got todo item: ', todo.__dict__)

        # Save logic
        todo.title = title
        todo.description = description
        todo.completed=request.POST.get('checkbox')

        todo.save()
        print('Todo updated: ', todo.__dict__)

    
    messages.info(request , 'Todo Item Saved')
    # Redirect back to index page
    return redirect('index')


def edit(request, id):
    print('Received Id: ' + str(id))

    # Fetch todo item by id
    todo = Todo.objects.get(pk = id)
    print('Got todo item: ', todo.__dict__)

    return render(request, 'create.html', {
        'form_type': 'edit',
        'todo': todo
    })
def remove(request, id):
    

    # Fetch todo item by id
    todo = Todo.objects.get(pk = id)
    todo.delete()

    return redirect('index')

