# Generated by Django 4.0.5 on 2022-06-19 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('letter', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PublishingCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('state_or_city', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_year', models.CharField(max_length=4)),
                ('pages', models.PositiveIntegerField()),
                ('subject', models.CharField(max_length=250)),
                ('author_id', models.ManyToManyField(to='biblioteca.author')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.place')),
                ('publishing_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.publishingcompany')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
