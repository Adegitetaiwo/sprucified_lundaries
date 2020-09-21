# Generated by Django 3.0.6 on 2020-06-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='set_frequently_asked_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=350)),
                ('answer', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Set Frequently Asked Question',
            },
        ),
    ]
