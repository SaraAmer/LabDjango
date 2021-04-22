# Generated by Django 3.2 on 2021-04-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210422_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isbn',
            name='Book_title',
        ),
        migrations.AddField(
            model_name='isbn',
            name='Author_name',
            field=models.CharField(default='sara', max_length=50),
            preserve_default=False,
        ),
    ]