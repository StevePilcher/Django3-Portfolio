# Generated by Django 3.1.7 on 2021-03-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_id',
            field=models.IntegerField(default='exit'),
            preserve_default=False,
        ),
    ]
