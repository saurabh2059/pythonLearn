# Generated by Django 5.0.7 on 2024-07-31 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
