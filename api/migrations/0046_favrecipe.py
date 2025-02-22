# Generated by Django 3.0 on 2021-06-12 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20210607_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_of_recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
