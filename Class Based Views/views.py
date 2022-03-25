# Imports for class based views
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Redirecting
from django.urls import reverse_lazy
# Import Model
from .models import Person


# Minimal CRUD for Person Model

class PersonList(ListView):
    # List
    model = Person
    context_object_name = 'people'
    paginate_by = 10
    template_name = 'dishes/people.html'
    # you can search for other attributes to customize


class PersonDetail(DetailView):
    # Detail
    model = Person
    context_object_name = 'person'


class PersonCreate(CreateView):
    # Create
    model = Person
    success_url = reverse_lazy('people')
    form_class = PersonForm()


class PersonUpdate(UpdateView):
    # Update
    model = Person
    fields = '__all__'
    # It is fields or form_class
    success_url = reverse_lazy('people')


class PersonDelete(DeleteView):
    # Delete
    model = Person
    context_object_name = 'person'
    success_url = reverse_lazy('people')
