# Generated by Django 3.2.5 on 2021-07-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(blank=True, choices=[('front-end', 'front-end'), ('back-end', 'back-end'), ('IOS', 'IOS'), ('Android', 'Android')], default='', max_length=20),
        ),
    ]
