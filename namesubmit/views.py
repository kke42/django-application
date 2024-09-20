from django.shortcuts import render, redirect
from .forms import SubmissionForm

# Create your views here.
def submit_form(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you') # Redirect to thank you page
    else:
        form = SubmissionForm()
    
    return render(request, 'namesubmit/submit_form.html', {'form':form})
    