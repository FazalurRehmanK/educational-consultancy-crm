from django.shortcuts import render, redirect
from .models import StudentLead

def public_dashboard(request):
    # 1. CHECK IF SOMEONE CLICKED SUBMIT
    if request.method == 'POST':
        # Grab the exact names from the HTML inputs
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email_address = request.POST.get('email')
        country = request.POST.get('target_country')

        # Create a brand new record in the database
        StudentLead.objects.create(
            first_name=f_name,
            last_name=l_name,
            email=email_address,
            target_country=country
            # Status defaults to 'LEAD' automatically!
        )
        
        # Refresh the page to clear the form and show the new lead
        return redirect('dashboard')

    # 2. IF NO ONE CLICKED SUBMIT, JUST SHOW THE PAGE NORMALLY
    all_leads = StudentLead.objects.all().order_by('-created_at') # Shows newest first
    context = {'leads': all_leads}
    
    return render(request, 'core/dashboard.html', context)