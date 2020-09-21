# Generated by Django 3.0.6 on 2020-06-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerTestimony',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=190)),
                ('passport', models.ImageField(upload_to='images')),
                ('testimony', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Customer Testimony',
            },
        ),
    ]