# Generated by Django 5.1.3 on 2024-11-28 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify_Wrapped', '0010_customuser_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='wrap',
            name='spirit_animal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
