from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from hr.forms import ApplicantForm
from hr.models import Applicant


def home(request):
    return render(request, 'hr/home.html')


# login method that will return the role
def do_login():
    # if you change the role manually to Selc then the login function will render the selc.html
    return {"name": "XYZ", "role": "Sec"}


def login(request):
    # we will decide based on the role if we want to redirect to selc.html or OE.html
    acc = do_login()
    if acc["role"] == "Selc":
        return render(request, 'hr/SelC/SelC.html')
    else:
        applicants = Applicant.objects.all()
        context = {'applicants': applicants}
        return render(request, 'hr/OE/OE.html', context=context)


def approve(request, pk):
    instance = Applicant.objects.get(pk=pk)
    instance.approved = True
    instance.save()
    return HttpResponse({"ok": "documents approved"})


def applicant(request):
    if request.method == 'POST':
        print(request.FILES)
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ApplicantForm()
    # add a form here to get the referal code
    return render(request, 'hr/applicant.html', {'form': form})
