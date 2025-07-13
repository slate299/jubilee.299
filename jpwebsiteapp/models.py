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
