# Generated by Django 4.0.4 on 2022-05-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
