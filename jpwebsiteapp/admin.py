from django.contrib import admin
from .models import NewsItem, NewsImage, Event, EventImage

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
