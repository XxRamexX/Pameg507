from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

        send_mail(
            subject=subject,
            message=full_message,
            from_email='Solicitudes@gmail.com',
            recipient_list=['theyammatos@gmail.com'],  # A dónde se enviará
            fail_silently=False,
        )
        messages.success(request, "¡Mensaje enviado correctamente!")
        return redirect('contact')  # Cambia por la URL que quieras recargar

    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')
