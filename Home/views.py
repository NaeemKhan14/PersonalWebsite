from django.contrib import messages
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
            message = "Name: " + form.cleaned_data['full_name'] + "\nEmail: " + form.cleaned_data[
                'email_address'] + "\nPhone Number: " + form.cleaned_data['email_address'] + "\nMessage: " + \
                      form.cleaned_data['message']

            try:
                send_mail("Message from naeemkhan.dev", message, 'noreply@naeemkhan.dev', ['naeemukhan14@gmail.com'])
                messages.add_message(request, messages.SUCCESS,
                                     'Message sent successfully! I will get back to you as soon as possible.')
            except BadHeaderError:
                messages.add_message(request, messages.ERROR,
                                     'Something went wrong. Please contact me at naeemukhan14@gmail.com.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Please provide phone number in correct format. For example: +971526698242.')

        return redirect('homepage')
