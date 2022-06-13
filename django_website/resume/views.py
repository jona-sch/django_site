from django.shortcuts import render

from resume.models import Experience

def resume(request):
    experiences = Experience.objects.order_by("-date_begin").all()

    for e in experiences:
        e.date_begin = str(e.date_begin).split(" ")[0]
        e.date_end = str(e.date_end).split(" ")[0]

    print(experiences)

    context = {
        'experiences': experiences
    }

    return render(request, 'resume.html', context)