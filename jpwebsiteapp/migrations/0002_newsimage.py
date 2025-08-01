# Generated by Django 5.2.4 on 2025-07-12 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jpwebsiteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='party_images/extra/')),
                ('news_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra_images', to='jpwebsiteapp.newsitem')),
            ],
        ),
    ]
