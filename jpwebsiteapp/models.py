from django.db import models

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='party_images/')  # Main image
    summary = models.TextField()
    url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)  # ✅ NEW FIELD

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news_item = models.ForeignKey(NewsItem, related_name='extra_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='party_images/extra/')

    def __str__(self):
        return f"Extra image for: {self.news_item.title}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='extra_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='events/extra/')

    def __str__(self):
        return f"Extra image for: {self.event.title}"

class County(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True)
    skills = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.county})"

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('infrastructure', 'Infrastructure'),
        ('health', 'Health'),
        ('digital', 'Digital'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, 'Other')