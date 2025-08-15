from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import NewsItem, Event, County, Volunteer, Project, Testimonial, HeroSlide, HighlightSlide
from .forms import ConcernForm
from itertools import zip_longest

#create your views here

def home(request):
    hero_slides = HeroSlide.objects.all().order_by('order')
    featured_news = NewsItem.objects.filter(is_featured=True).order_by('-date')[:5]
    highlight_slides = HighlightSlide.objects.all().order_by('order')
    featured_events = Event.objects.filter(featured=True).order_by('date')[:5]
    counties = County.objects.all().order_by('name')
    testimonials = Testimonial.objects.all()

    volunteer_success = False

    if request.method == 'POST':
        # Check which form submitted: use name="form_type"
        form_type = request.POST.get('form_type')
        if form_type == 'volunteer':
            full_name = request.POST.get('fullName')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            location_id = request.POST.get('location')
            skills = request.POST.get('skills')

            if full_name and email and phone and location_id and skills:
                county = get_object_or_404(County, id=location_id)
                Volunteer.objects.create(
                    full_name=full_name,
                    email=email,
                    phone=phone,
                    county=county,
                    skills=skills
                )
                volunteer_success = True

    return render(request, 'home.html', {
        'featured_news': featured_news,
        'featured_events': featured_events,
        'counties': counties,
        'testimonials': testimonials, 
        'hero_slides': hero_slides,
        'highlight_slides': highlight_slides,
        'volunteer_success': volunteer_success,
    })

# About Page
def about(request):
    return render(request, 'about.html')

# Leadership Page
def leadership(request):
    return render(request, 'leadership.html')

# Legacy Page
def legacy(request):
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    return render(request, 'legacy.html', {
        'featured_projects': featured_projects
    })

# Achievements Page
def achievements(request):
    categories = Project.CATEGORY_CHOICES
    projects = Project.objects.all()  # Get all projects
    featured_projects = Project.objects.filter(is_featured=True)[:3]

    return render(request, 'achievements.html', {
        'categories': categories,
        'projects': projects,
        'featured_projects': featured_projects,
    })

# Project Detail Page
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

def concerns(request):
    success = False

    if request.method == 'POST':
        form = ConcernForm(request.POST)
        if form.is_valid():
            concern = form.save(commit=False)
            concern.issues = ', '.join(form.cleaned_data['issues'])
            concern.save()
            success = True  # ✅ flag for template
            form = ConcernForm()  # Clear the form after submit
    else:
        form = ConcernForm()

    return render(request, 'concerns.html', {'form': form, 'success': success})

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
def big4(request):
    return render(request, 'big4.html')

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
