from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import NewsItem, Event, County, Volunteer, Project

#create your views here

#home view
def home(request):
    featured_news = NewsItem.objects.filter(is_featured=True).order_by('-date')[:5]
    featured_events = Event.objects.filter(featured=True).order_by('date')[:5]
    counties = County.objects.all().order_by('name')

    # If AJAX POST
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location_id = request.POST.get('location')
        skills = request.POST.get('skills')

        county = get_object_or_404(County, id=location_id)

        Volunteer.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            county=county,
            skills=skills
        )

        return JsonResponse({'status': 'success'})

    return render(request, 'home.html', {
        'featured_news': featured_news,
        'featured_events': featured_events,
        'counties': counties
    })


# About Page
def about(request):
    return render(request, 'about.html')

# Leadership Page
def leadership(request):
    return render(request, 'leadership.html')

# Achievements Page
def achievements(request):
    projects = Project.objects.all()
    return render(request, 'achievements.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'project_detail.html', {'project': project})

def events(request):
    all_events = Event.objects.all().order_by('date')  # Upcoming events first
    return render(request, 'events.html', {
        'events': all_events,
    })

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

# Concerns Page
def concerns(request):
    return render(request, 'concerns.html')

# News page
def news(request):
    news_items = NewsItem.objects.all().order_by('-date')
    categories = ['All News', ...]
    hero_image = 'party_images/Uhurupartyleader.jpg'
    return render(request, 'news.html', {
        'news_items': news_items,
        'categories': categories,
        'hero_image': hero_image,
    })
   
# big4_page
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
