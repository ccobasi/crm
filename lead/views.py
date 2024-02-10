# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from .forms import AddLeadForm
# from .models import Lead

# @login_required
# def leads_list(request):
#     leads = Lead.objects.filter(created_by=request.user)

#     return render(request, 'lead/leads_list.html', {'leads': leads})

# @login_required
# def add_lead(request):
#     if request.method == 'POST':
#         form = AddLeadForm(request.POST)

#         if form.is_valid():
#             lead = form.save(commit=False)
#             lead.created_by = request.user
#             lead.save()

#             return redirect('dashboard')
#     else:
#         form = AddLeadForm()

#     return render(request, 'lead/add_lead.html', {'form': form})
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import AddLeadForm
from .models import Lead

class AddLeadView(View):
    template_name = 'lead/add_lead.html'

    def get(self, request):
        form = AddLeadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, "Successfully created the lead")
            return redirect('leads_list')

        return render(request, self.template_name, {'form': form})

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)

    return render(request, 'lead/leads_list.html', {'leads': leads})

@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk, created_by=request.user)
    # lead = Lead.objects.filter(created_by=request.user).get(pk=pk)

    return render(request, 'lead/leads_detail.html', {
        'lead': lead,
    })

@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk, created_by=request.user)
    lead.delete()

    messages.success(request, "Successfully deleted the lead")
    return redirect('leads_list')

@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully edited the lead")
            return redirect('leads_list')

    else:
        form = AddLeadForm(instance=lead)
        # messages.error(request, "Error editing the lead. Please check the form.")
    
    return render(request, 'lead/edit_lead.html', {'form': form, 'lead': lead})
   
