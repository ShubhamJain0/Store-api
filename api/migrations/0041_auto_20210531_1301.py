# Generated by Django 3.0 on 2021-05-31 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20210530_0827'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InactiveUserId',
        ),
        migrations.RemoveField(
            model_name='itemsdata',
            name='user',
        ),
        migrations.DeleteModel(
            name='ResetPassUserId',
        ),
        migrations.DeleteModel(
            name='ItemsData',
        ),
    ]
