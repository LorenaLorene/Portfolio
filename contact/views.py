from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
from . import form as Forms


def contact_form_submission(request):
    if request.method == 'POST':
        form = Forms.ContactForm(request.POST)
        if form.is_valid():
            try:
                #send_mail(form.cleaned_data['contact_name'], form.cleaned_data['contact_message'], form.cleaned_data['contact_email'], ['lorenija@gmail.com'])
                return HttpResponseRedirect('/')
            except BadHeaderError:
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')