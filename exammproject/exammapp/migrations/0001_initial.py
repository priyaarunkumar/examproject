# Generated by Django 3.2.10 on 2022-04-05 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250, unique=True)),
                ('desc1', models.TextField(unique=True)),
                ('image', models.ImageField(upload_to='pic')),
            ],
        ),
    ]
