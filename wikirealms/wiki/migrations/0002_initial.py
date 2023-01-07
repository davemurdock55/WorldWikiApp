# Generated by Django 4.1.3 on 2023-01-07 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wiki", "0001_initial"),
        ("worldbuilding", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="wikipage",
            name="realm",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="worldbuilding.realm"
            ),
        ),
        migrations.AddField(
            model_name="wikipage",
            name="users",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
