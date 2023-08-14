from django.shortcuts import render
from . import final


# Create your views here.
def sentiment(request):
    result = ""

    if request.method == 'POST' and 'pred_button' in request.POST:
        name = request.POST.get('text data', '')
        result = final.pre(str(name))

    context = {
        'result': result,
    }

    return render(request, "first.html", context)
