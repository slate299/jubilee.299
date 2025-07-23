from django.db import models

class HeroSlide(models.Model):
    title_part_one = models.CharField(max_length=200)
    title_part_two = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hero_slides/')
    button_primary_text = models.CharField(max_length=100, default="Learn More")
    button_primary_url = models.CharField(max_length=200, default="/about/")  # ✅ switched from URLField
    button_secondary_text = models.CharField(max_length=100, default="Join Us")
    button_secondary_url = models.CharField(max_length=200, default="#join-section")  # ✅ switched from URLField
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title_part_one} {self.title_part_two}"


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


class Concern(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    issues = models.TextField()  # We'll store checked issues as a comma-separated string
    other_issues = models.CharField(max_length=255, blank=True)
    story = models.TextField(blank=True)
    thanks = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"


class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonials/')
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial {self.id}"


class HighlightSlide(models.Model):
    image = models.ImageField(upload_to="highlight_slides/")
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title