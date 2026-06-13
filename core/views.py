from django.shortcuts import render, redirect
from .models import StudentLead

def public_dashboard(request):
    error_message = None  # We start with no errors

    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email_address = request.POST.get('email')
        country = request.POST.get('target_country')

        # CHECK 1: Does this email already exist in the database?
        if StudentLead.objects.filter(email=email_address).exists():
            # If yes, trigger an error message and skip the creation
            error_message = "A student with this email address has already applied!"
        else:
            # If no, safely create the new record
            StudentLead.objects.create(
                first_name=f_name,
                last_name=l_name,
                email=email_address,
                target_country=country
            )
            return redirect('dashboard')

    # Fetch leads to display below the form
    all_leads = StudentLead.objects.all().order_by('-created_at')
    
    # We now pass the error_message to the HTML as well
    context = {
        'leads': all_leads,
        'error': error_message
    }
    
    return render(request, 'core/dashboard.html', context)