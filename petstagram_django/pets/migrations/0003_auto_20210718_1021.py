# Generated by Django 3.2.3 on 2021-07-18 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_like_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='image_url',
        ),
        migrations.AddField(
            model_name='pets',
            name='image',
            field=models.ImageField(default='', upload_to='pets'),
            preserve_default=False,
        ),
    ]
