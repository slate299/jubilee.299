from django.contrib import admin
from .models import NewsItem, NewsImage, Event, EventImage, County, Volunteer, Project

# ✅ Inline for News extra images
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_featured')
    inlines = [NewsImageInline]


# ✅ Inline for Event extra images
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'featured')
    inlines = [EventImageInline]

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'county', 'created_at']
    list_filter = ['county', 'created_at']
    search_fields = ['full_name', 'email', 'phone']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('category',)