from django.shortcuts import render
from django.views.generic import View


class Customer(View):
    def get(self, request):
        '''
        TODO:
        - This will reutrn list of customer
        '''
        return render(request, 'customers/customer.html')
