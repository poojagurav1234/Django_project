import json
import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import ATMSite, State, City

def uploadfile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            
            if 'Contact Details' in df.columns:
                for index, row in df.iterrows():
                    state, _ = State.objects.get_or_create(name=row['State'])
                    city, _ = City.objects.get_or_create(name=row['City'], state=state)
                    
                    contact_details_str = row['Contact Details']
                    contact_details = json.loads(contact_details_str.replace("'", "\""))
                    
                    # Try to get existing site by site_id
                    try:
                        site = ATMSite.objects.get(site_id=row['ID'])
                        # Update existing site
                        site.name = row['Name']
                        site.address = row['Address']
                        site.state = state
                        site.city = city
                        site.contact_details = contact_details
                        site.save()
                    except ATMSite.DoesNotExist:
                        # Create new site if it doesn't exist
                        ATMSite.objects.create(
                            name=row['Name'],
                            site_id=row['ID'],
                            address=row['Address'],
                            state=state,
                            city=city,
                            contact_details=contact_details
                        )
                
                return redirect('site_list')
            else:
                return render(request, 'upload_file.html', {'form': form, 'error_message': 'Contact Details column is missing'})
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})

def site_list(request):
    sites = ATMSite.objects.all()
    return render(request, 'site_list.html', {'sites': sites})
