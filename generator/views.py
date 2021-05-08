from django.shortcuts import render
from django.views import View
import random
# Create your views here.

class index(View):
    template_name="base.html"
    def get(self,request):
        return render(request,self.template_name)
        
    def post(self,request):
        password=''
        character=list('abcdefghijklmnopqrstuvwxyz')
        pass_len =int(request.POST.get('length'))
        
        if request.POST.get('uppercase'):
            character.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ') 
        if request.POST.get('number'):
            character.extend('0123456789')     
        if request.POST.get('special'):
            character.extend('!@#$%^&*~') 

        for x in range(pass_len):
            password += random.choice(character)
            
        return render(request,self.template_name,{'context' : password})
        
