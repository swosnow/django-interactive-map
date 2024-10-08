# Generated by Django 4.2.16 on 2024-10-08 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('description_is_html', models.BooleanField(default=False)),
                ('cep', models.BigIntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
