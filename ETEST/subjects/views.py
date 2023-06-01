from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

subject_desc = {
    "Honors US History":{"500-510":"2/23", "RQ 500-510":"2/23", "511-521":"2/26", "RQ 511-521":"2/26"},
    "english":{"Read Macbeth":"2/28", "Read 20 Poems":"3/1", "Write an Essay":"3/14"},
    "math":{"Problems 1-20":"2/24", "Problems 25-50":"2/27", "Study":"3/1", "Test":"3/1"},
    "chemistry":{"Webassign 100.2":"2/28", "Watch a 3-hour Screencast":"3/1", "Write a Lab Report":"3/5", "Study for Test":"3/10"},
    "chinese":{"Memorize Dialogue":"2/28", "Speaking Quiz":"3/4", "Reading Quiz":"3/8", "Writing Quiz":"3/10"},
    "web development":{"Work on Lab ":"2/24", "Work on Lab":"2/28", "Lab Due":"3/4"}
}

def index(request):
    subjects = list(subject_desc.keys())
    return render(request, "subjects/index.html",
    {
        "subjects_list":subjects
    })

def subject_description(request, subject):
    try:
        assignment = list(subject_desc[subject])   # Read Macbeth, Read 20 Poems, etc
        duedate = list(subject_desc[subject].values()) # 2/28, 3/1
        myAssignmentList = zip(assignment, duedate) #zip function to merge them to tuple
        print(f"assignment  {assignment}" )  # display in terminal
        print(f"duedate  {duedate}" )     # display in terminal

        return render(request, "subjects/subject.html", {
            "assignments" : myAssignmentList,
            "subject_name" : subject
        })
    except:
        return HttpResponseNotFound("ERROR")