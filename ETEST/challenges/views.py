from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

monthlyGoals = {
    "january":"happy new year 🎉",
    "february":"Brrrr its cold ❄️",
    "march":"is it spring <i>yet</i>🌷",
    "april":"easter = bunnie 🐰",
    "may":"last month of school 🥹",
    "june":"ready for vacation 🏝️",
    "july":"hbd me !! 🎁",
    "august":"back to school 😔",
    "september":"more school idk 😭",
    "october":"halloween 🎃",
    "november":"thanksgiving 🦃",
    "december":"xmas 🎄"
}

def index(request):
    dataToReturn = ""
    months = list(monthlyGoals.keys())
    # for month in months:
    #     monthPath = f"/challenges/{month}"
    #     dataToReturn += f"<li style = 'font-size:30px'><a href = '{monthPath}'>{month.capitalize()}</a></li>\n"

    # responseData = f"<ul>{dataToReturn}</ul>"
    # return HttpResponse(responseData)
    return render(request, "challenges/index.html", {
        "months_key" : months
    })

def monthly_goal_by_num(request, month):
    # return HttpResponse(f"numeric month entered: {month}")
    months = list(monthlyGoals.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("Invalid number")
    forward_month = months[month - 1]
    return HttpResponseRedirect(f"/challenges/{forward_month}")

def monthly_goal(request, month):
    strToReturn = ""

    try:
        strToReturn = monthlyGoals[month]
        # return HttpResponse(strToReturn)
        return render(request, "challenges/challenge.html", {
            "text": strToReturn,
            "month_name":month.capitalize
        })
    except:
        return HttpResponseNotFound("ERROR")

    return HttpResponse(strToReturn)