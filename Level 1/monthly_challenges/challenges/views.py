from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "Go for a walk every day for 20 minutes",
    "february": None,
    "march": "Learn to cook",
    "april": "Practice guitar for 15 minutes every day",
    "may": "Read 2 boooks",
    "june": "Go outside",
    "july": "Climb mount everest",
    "august": "Clean up the house",
    "september": "Practice programming",
    "october": "Practice maths",
    "november": "Learn a new skill",
    "december": "Go skiing",
}

def index(request):
    list_items = ""
   
    return render(request, "challenges/index.html", {

        "months": monthly_challenges

    })

def month_challenges_num(request, month):
    l = list(monthly_challenges.keys())

    if month > len(l):
        return HttpResponseNotFound("Month not found!")

    month_to_forward_to = l[month-1]
    link = reverse("month-challenge", args=[month_to_forward_to])
    return HttpResponseRedirect(link)


def month_challenges(request, month):
    try:
        return render(request, "challenges/challenge.html", {
            "text": monthly_challenges[month],
            "month": month
        })
    except:
        raise Http404()