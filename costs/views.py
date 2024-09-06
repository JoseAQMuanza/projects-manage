# Django Imports
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import Project, Service


# My Views
def home(request):
  return render(request, 'home.html')

# Insert project in database
def projects(request):      
  if request.method == 'GET':
    projects = {'projects': Project.objects.all()}
    return render(request, 'projects.html', projects)
  
  elif request.method == 'POST':
    newproject = Project()
    name = request.POST.get('name')
    budget =  request.POST.get('budget')
    categories = request.POST.get('categories') 
    validation_response = projectvalidaton(name, budget, categories, request)
    if validation_response:
      return validation_response
    
    try:                  
      newproject.name = name
      newproject.budget = str(f'{float(request.POST.get('budget')):,.2f}')
      newproject.categories = categories
      newproject.save()    
    except:        
        return render(request, 'errorpage.html')
    else:    
      projects = {'projects': Project.objects.all()}        
      messages.success(request, 'Project created with success!')
      return render(request, 'projects.html', projects)

# View Eterprise
def enterprise(request):  
  return render(request, 'enterprise.html')


# View Contacts
def contact(request):
  return render(request, 'contact.html')


# View Registration project
def createproject(request):
  return render(request, 'createproject.html')

# Page of error
def errorpage(request):
  return render(request, 'errorpage.html')


def delete(request, id):    
    proj = get_object_or_404(Project, id_project=id)
    if request.method == 'GET':    
      try:        
        proj.delete()
      except:
        return render(request, 'errorpage.html')
      else:              
        messages.success(request, 'Project deleted with success!')                                              
        return redirect(reverse('projects'))


def edit(request, id):  
  # Pegando o Projeto
  getproject = get_object_or_404(Project, id_project=id)

  # Caso seja uma requição GET
  if request.method == 'GET':   
    # Pegando os dados do projeto selecionado          
    newproject = newelement(getproject)     
    # Analisando se Existem serviços no projeto
    if getproject.service.exists():
      services = getproject.service.all()       
      return render(request, 'edit.html', {'project': newproject, 'services': services})
    else:
      return render(request, 'edit.html', {'project': newproject})  
  # se for uma requição POST
  elif request.method == 'POST':        
    servicename = request.POST.get('servicename')
    servicecost = request.POST.get('servicecost')
    description = request.POST.get('servicedescription')
    # Salidando os campos do serviço
    service_validation = servicevalidaton(id, servicename, servicecost, description, request)
    if service_validation:
      return service_validation
    # Tentando salvar o serviço na base de dados
    cost = float(request.POST.get('servicecost'.replace(',', '')))
    budg = float(getproject.budget.replace(',', ''))    
    if cost > budg:
      print(budg, cost)
      messages.error(request, 'Valor cost biggest budget!'.upper())
      return redirect( reverse('edit', args=[id]))
    else:    
      try:
        budget = budg - cost
        getproject.budget =  str(f'{(budget):,.2f}')
        getproject.save()
        service = Service()
        service.project = getproject
        service.name = servicename
        service.cost = str(f'{float(request.POST.get('servicecost')):,.2f}')
        service.description = description
        service.save()    
      except:
        return render(request, 'errorpage.html')
      else:          
        newproject = newelement(getproject)
        services = getproject.service.all()
        messages.success(request, 'Service created with success!')
        return render(request, 'edit.html', {'project': newproject, 'services': services})    

def projectedit(request, id):  
  getproject = get_object_or_404(Project, id_project=id)
  if request.method == 'POST':    
    name = request.POST.get('')
    validation_response = projectvalidaton()
    return HttpResponse(getproject.budget)

# Delete Service
def deleteservice(request, id, ids):
  if request.method == 'GET':
    try:
      service = Service.objects.get(id=ids)
      service.delete()
    except:
      return redirect(reverse('errorpage'))
    else:
      messages.success(request, 'Service deleted with success!')
      return redirect(reverse('edit', args=[id]))


def projectvalidaton(projectname, projectbudget, projectcategoris, request):
  if projectname == '':      
      messages.error(request, 'Enter project name!'.upper())
      return render(request, 'createproject.html', {'name': projectname, 'budget': projectbudget, 'categories': projectcategoris})         
  elif projectbudget == '':                  
      messages.error(request, 'Enter budgete amout!'.upper())      
      return render(request, 'createproject.html', {'name': projectname, 'budget': projectbudget, 'categories': projectcategoris})      
  elif projectcategoris == 'Select one option':
      messages.error(request, 'Select a categories Valid!'.upper())
      return render(request, 'createproject.html', {'name': projectname, 'budget': projectbudget, 'categories': projectcategoris})      
  return None


def servicevalidaton(id, servicename, servicecost, servicedescription, request):
  if servicename == '':      
      messages.error(request, 'Enter service name!'.upper())      
      return redirect(reverse('edit', args=[id]))
  elif servicecost == '':                  
      messages.error(request, 'Enter cost amout!'.upper())      
      return redirect(reverse('edit', args=[id]))
  elif int(servicecost) < 0:                  
      messages.error(request, 'negative amout!'.upper())      
      return redirect(reverse('edit', args=[id]))
  elif servicedescription == '':
      messages.error(request, 'Enter service description!'.upper())
      return redirect(reverse('edit', args=[id]))
  return None


def newelement(project):
  newproject = {
    'id': project.id_project,
    'name': project.name,
    'budget': str(f'{float(project.budget.replace(',', '')):,.2f}'),
    'categories': project.categories          
  }  

  return newproject