# Generated by Django 4.2 on 2023-07-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_stafffeedback_studentfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('notice', models.TextField()),
            ],
        ),
    ]
