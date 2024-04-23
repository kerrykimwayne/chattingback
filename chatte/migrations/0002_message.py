# Generated by Django 4.2.7 on 2024-04-21 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_envoie', models.DateTimeField(auto_now_add=True)),
                ('expediteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='expediteur', to=settings.AUTH_USER_MODEL)),
                ('recepteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recepteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]