from django.contrib import admin
from .models import NewsItem, NewsImage, Event, EventImage, County, Volunteer, Project, Concern, Testimonial, HeroSlide, HighlightSlide, Category

# ✅ Inline for News extra images
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_featured')
    inlines = [NewsImageInline]

# ✅ Register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

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

@admin.register(Concern)
class ConcernAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'second_name',
        'surname',
        'phone_number',
        'email',
        'submitted_at',
    )
    search_fields = (
        'first_name',
        'second_name',
        'surname',
        'phone_number',
        'email',
        'issues',
        'other_issues',
    )
    list_filter = ('submitted_at',)
    readonly_fields = ('submitted_at',)

admin.site.register(Testimonial)
admin.site.register(HeroSlide)
admin.site.register(HighlightSlide)