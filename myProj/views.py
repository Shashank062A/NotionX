from django.http import HttpResponse
from django.shortcuts import render
from fileuploads.models import UploadeFiles
from django.http import JsonResponse
def home (request):
    return render(request, 'home.html')
def branch (request):
    return render(request, 'ee.html')
def pdf(request):
    files = UploadeFiles.objects.all()
    context = {
        'files': files,
    }
    return render(request, 'pdf.html', context)

def CseNotes(request):
    Csefiles = UploadeFiles.objects.filter(branch="CSE", category="NOTES")
    context = {
     'Csefiles': Csefiles,   
    }
    return render(request, "cse.html", context)
def getFiles (request):
    if request.method == "POST":
        semester = request.POST.get("semester")
        subject = request.POST.get("subject")
        resources = request.POST.get("resource")
        files = UploadeFiles.objects.filter(sem = semester, subject = subject, category = resources)
        category_name = resources
        subject_name = subject
        context = {
            'files': files,
            'category_name' : category_name,
            'subject_name' : subject_name,

        }
        return render(request, "files.html", context)

def getSubjects (request, semester):
    subject = (
        UploadeFiles.objects.filter(sem = semester)
        .values_list("subject", flat=True)
        .distinct()
     )
    return JsonResponse(list(subject), safe=False)