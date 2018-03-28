from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SurveyForm
from django.http import HttpResponse
from .models import Survey


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def birds_eye_view(request):
    return HttpResponse("birds eye view")


def get_survey(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SurveyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SurveyForm()

    return render(request, 'scouter/newscout.html', {'form': form})
