from django.shortcuts import render, redirect
from django.contrib import messages  
from .models import StudentLead

def public_dashboard(request):
    error_message = None

    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email_address = request.POST.get('email')
        country = request.POST.get('target_country')

        if StudentLead.objects.filter(email=email_address).exists():
            error_message = "A student with this email address has already applied!"
        else:
            StudentLead.objects.create(
                first_name=f_name,
                last_name=l_name,
                email=email_address,
                target_country=country
            )
            # Trigger the success message before redirecting
            messages.success(request, f"Success! {f_name}'s application has been added.")
            return redirect('dashboard')

    all_leads = StudentLead.objects.all().order_by('-created_at')
    context = {
        'leads': all_leads,
        'error': error_message
    }
    
    return render(request, 'core/dashboard.html', context)