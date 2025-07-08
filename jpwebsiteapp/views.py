from django.shortcuts import render

# Create your views here.

# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Leadership Page
def leadership(request):
    return render(request, 'leadership.html')

# Achievements Page
def achievements(request):
    return render(request, 'achievements.html')

# Events Page
def events(request):
    return render(request, 'events.html')

# Join the Movement Page
def join_movement(request):
    return render(request, 'join_movement.html')

# Donate Page
def volunteer(request):
    return render(request, 'volunteer.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Blog Page
def blog(request):
    return render(request, 'blog.html')

# views.py
def big4_home(request):
    # This could come from DB later!
    raw_data = "Manufacturing:87,Affordable Housing:72,Healthcare:65,Food Security:91"
    pillars = []
    for item in raw_data.split(','):
        name, value = item.split(':')
        pillars.append({'name': name.strip(), 'value': int(value.strip())})

    context = {
        'pillars': pillars,
    }
    return render(request, 'big4_home.html', context)


def manufacturing_view(request):
    return render(request, 'big4/manufacturing.html')

def housing_view(request):
    return render(request, 'big4/housing.html')

def healthcare_view(request):
    return render(request, 'big4/healthcare.html')

def food_security_view(request):
    return render(request, 'big4/food_security.html')

# Search Results Page (Optional)
def search(request):
    query = request.GET.get('q', '')
    # Add logic for handling the search query and return results
    return render(request, 'search_results.html', {'query': query})
