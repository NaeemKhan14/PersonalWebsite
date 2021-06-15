from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'homepage/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': ContactForm()})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            body = {
                'Name: ': form.cleaned_data['full_name'],
                'Email: ': form.cleaned_data['email_address'],
                'Phone Number: ': form.cleaned_data['phone_number'],
                'Message: ': form.cleaned_data['message']
            }
            message = "\n".join(body.values())

            try:
                send_mail("Message from naeemkhan.dev", message, 'noreply@naeemkhan.dev', ['naeemukhan14@gmail.com'])
                return render(request, self.template_name, {'form': ContactForm()})
            except BadHeaderError:
                return render(request, self.template_name, {'form': ContactForm()})
