from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

from job_application.forms import ApplicationForm
from job_application.models import Form
from django.contrib import messages


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )

            message_body = f"A new job application was submitted. Thank you, {first_name}"
            email_message = EmailMessage("Form submission confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully!")

            return redirect("index")
    return render(request, "index.html")