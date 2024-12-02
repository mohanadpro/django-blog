from django.shortcuts import render
from .models import About
from .form import AboutForm
from django.contrib import messages
def about_me(request):
    """
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    if request.method == "POST":
        about_form = AboutForm(data=request.POST)
        print(about_form)
        if about_form.is_valid():
            about_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
    about_form = AboutForm()

    return render(
        request,
        "about/about.html",
        {"about": about , 'collaborate_request':about_form},
    )
