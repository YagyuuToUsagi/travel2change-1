# Generated by Django 2.1.7 on 2019-03-25 06:07

import activities.models
import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Insert a name for your activity', max_length=255, verbose_name='title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from=['title'])),
                ('description', models.TextField(help_text='Describe the activity. (Max. 400 characters)', max_length=400, verbose_name='description')),
                ('highlights', models.TextField(help_text='List what makes this activity unique. (Max. 400 characters) \nPlease insert each highlight per line.', max_length=400, verbose_name='highlights')),
                ('requirements', models.TextField(blank=True, help_text='List all the requirements that you expect from participants. (e.g. age restrictions, required skills etc) \nPlease insert each requirement per line.', max_length=400, verbose_name='requirements')),
                ('address', models.CharField(help_text='Enter the address of the meeting place', max_length=255, verbose_name='address')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default=21.307, max_digits=9, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default=-157.858, max_digits=9, null=True, verbose_name='longitude')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0.0, help_text="Cost of participation.\nIf it's free, then leave it as 0.00 or blank", max_digits=6, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='price')),
                ('featured_photo', models.ImageField(blank=True, help_text='This photo will be featured on listings and the topof your activity page.', null=True, upload_to=activities.models.get_featured_image_filename, verbose_name='featured photo')),
                ('review_count', models.IntegerField(blank=True, default=0, verbose_name='review count')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='activity created date')),
                ('modified', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False, verbose_name='is approved')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='users.Host')),
            ],
            options={
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='ActivityPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=activities.models.get_image_filename, verbose_name='Photo')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='activities.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='LatestActivities',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='activities_latestactivities', serialize=False, to='cms.CMSPlugin')),
                ('latest_activities', models.IntegerField(default=5, help_text='The maximum number of latest activities to display')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=['name'])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('font_awesome', models.CharField(help_text='This will display an icon next to a tag. Format: fa-(icon name)', max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='region',
            field=models.ForeignKey(help_text='Choose a region where you activity will be held.', on_delete=django.db.models.deletion.CASCADE, related_name='activities', related_query_name='activity', to='activities.Region', verbose_name='region'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Select tag(s) that best describe your activity.', to='activities.Tag', verbose_name='tags'),
        ),
    ]
