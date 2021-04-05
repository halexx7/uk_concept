from django.views.generic import CreateView
from .models import Person

class PersonCreateView(CreateView):
    model = Person
    template_name = 'formstutor/person_form.html'
    fields = ('name', 'email', 'job_title', 'bio')