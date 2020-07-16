# Generated by Django 2.1.5 on 2020-01-12 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('Telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('Fax', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PriceSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location1', models.CharField(max_length=255)),
                ('location2', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='industry',
            name='industry_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationSet', to='industry.IndustryName'),
        ),
        migrations.AddField(
            model_name='industry',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationSet', to='industry.Location'),
        ),
    ]
