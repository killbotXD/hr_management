# Generated by Django 3.0.7 on 2020-06-21 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20200621_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='doc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
