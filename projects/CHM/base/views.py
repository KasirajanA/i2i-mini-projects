from django.shortcuts import render


class BaseView:  

    def home(request):
        """Returns to Base html page"""
        return render(request, 'base.html')

    def admin(request):
        """Returns to admin panel page"""
        return render(request, 'admin.html')    

    def employee(request):
        """Returns to employee panel page"""
        return render(request, 'employee.html')    