from django.http import HttpResponse
from django.shortcuts import render
from fileuploads.models import UploadeFiles
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from User.models import QuestionPaper, Purchase
import uuid   # for transaction IDs

def home (request):
    return render(request, 'home.html')
def branch (request):
    return render(request, 'ee.html')
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

# def SelectSemester (request):
#     if request.method == "POST":
#         branch = request.POST.get("branch")
#         semester = request.POST.get("semester")
#         request.session["branch"] = branch
#         request.session["semester"] = semester
#         return redirect ("show_Packages")
#     return render(request, 'selectSemester.html')

# # Show 3 packages
# def show_Packages(request):
#     branch = request.session.get("branch")
#     semester = request.session.get("semester")
#     return render(request, 'packages.html', {"branch": branch, "semester": semester})

# # Step 3: Checkout Page
# @login_required
# def checkout(request, package):
#     branch = request.session.get("branch")
#     semester = request.session.get("semester")
#     price_map = {
#         "single": 3 * 100,     # ₹3 → in paise
#         "subject": 15 * 100,   # ₹15
#         "semester": 50 * 100   # ₹50
#     }
    
#     if request.method == 'POST':
#         subject = request.POST.get("subject") if package in ["single", "subject"] else None
        
        # Create Razorpay client

        