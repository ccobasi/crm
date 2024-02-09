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

from django.shortcuts import render, redirect
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
            return redirect('dashboard')

        return render(request, self.template_name, {'form': form})

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)

    return render(request, 'lead/leads_list.html', {'leads': leads})

@login_required
def leads_detail(request, pk):
    lead = Lead.objects.filter(created_by=request.user).get(pk=pk)

    return render(request, 'lead/leads_detail.html', {
        'lead': lead,
    })