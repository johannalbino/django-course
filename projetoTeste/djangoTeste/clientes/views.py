from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import personForm
# Create your views here.

def listPerson(request):
	persons = Person.objects.all()
	return render(request, 'person.html', {"pessoas" : persons})

def newPerson(request):
	form = personForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('personList')
	return render(request, 'form.html', {'formPerson' : form })

def updatePerson(request, id):
	personU = get_object_or_404(Person, pk=id)
	form = personForm(request.POST or None, request.FILES or None, instance=personU)

	if form.is_valid():
		form.save()
		return redirect('personList')
	return render(request, 'form.html', {'formPerson': form})

def deletePerson(request, id):
	personU = get_object_or_404(Person, pk=id)
	form = personForm(request.POST or None, request.FILES or None, instance=personU)

	if request.method == 'POST':
		personU.delete()
		return redirect('personList')

	return render(request, 'personDeleteConfirm.html', {'formPerson' : personU})