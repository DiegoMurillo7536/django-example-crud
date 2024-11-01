from django.shortcuts import render,redirect
from .models import Example

# Create your views here.
def home(request):
    examples = Example.objects.all()
    return render(request, 'manage_example.html', {'examples': examples})

def add_example(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        description = request.POST['description']
        if name and description:
            example = Example(name=name, description=description)
            example.save()
            return redirect('/')
        examples = Example.objects.all()
        return render(request, 'manage_example.html', {'examples': examples})
def edit_example(request, id):
    example = Example.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        if name and description:
            example.name = name
            example.description = description
            example.save()
            return redirect('/')
    return render(request, 'manage_example.html', {'example': example})

def delete_example(_, id):
    example = Example.objects.get(id=id)
    example.delete()
    return redirect('/')