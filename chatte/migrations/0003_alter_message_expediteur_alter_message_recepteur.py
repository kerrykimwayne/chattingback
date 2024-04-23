# Generated by Django 4.2.7 on 2024-04-21 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatte', '0002_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='expediteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expediteur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='recepteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recepteur', to=settings.AUTH_USER_MODEL),
        ),
    ]
