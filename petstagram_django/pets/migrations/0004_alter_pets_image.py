# Generated by Django 3.2.3 on 2021-07-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20210718_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets',
            name='image',
            field=models.ImageField(default='pets/default.jpg', upload_to='pets'),
        ),
    ]
