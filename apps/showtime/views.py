from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
import pytz

# Create your views here.
def index(request):
    context = {
        "time": strftime("%I:%M %p", localtime()),
        "day": strftime("%B %d, %Y", localtime())
    }
    return render(request, 'index.html', context)
