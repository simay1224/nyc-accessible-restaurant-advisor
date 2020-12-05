# Generated by Django 3.1.2 on 2020-12-04 01:20

import accessible_restaurant.models
import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_user', models.BooleanField(default=False)),
                ('is_restaurant', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=128)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('img_url', models.URLField(blank=True, default='https://i.pinimg.com/originals/4e/24/f5/4e24f523182e09376bfe8424d556610a.png', max_length=250)),
                ('rating', models.FloatField(blank=True, default=0)),
                ('review_count', models.FloatField(blank=True, default=0)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=9)),
                ('address', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('zip_code', models.CharField(blank=True, max_length=16)),
                ('phone', models.CharField(blank=True, max_length=32)),
                ('compliant', models.BooleanField(default=False)),
                ('price', models.CharField(blank=True, max_length=5)),
                ('category1', models.CharField(blank=True, max_length=128)),
                ('category2', models.CharField(blank=True, max_length=128)),
                ('category3', models.CharField(blank=True, max_length=128)),
                ('main_category1', models.CharField(blank=True, max_length=128)),
                ('main_category2', models.CharField(blank=True, max_length=128)),
                ('main_category3', models.CharField(blank=True, max_length=128)),
                ('cuisine', models.CharField(blank=True, max_length=128)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='default.jpg', upload_to='user_profile_pics')),
                ('phone', models.BigIntegerField(blank=True, default=1234567889, validators=[accessible_restaurant.models.User_Profile.validate_phone])),
                ('address', models.CharField(blank=True, max_length=128)),
                ('borough', models.CharField(choices=[('Manhattan', 'Manhattan'), ('Brooklyn', 'Brooklyn'), ('Queens', 'Queens'), ('The Bronx', 'The Bronx'), ('Staten Island', 'Staten Island'), ('Not Applicable', 'Not Applicable')], default='None Selected', max_length=128)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('zip_code', models.PositiveSmallIntegerField(blank=True, default=12345, validators=[accessible_restaurant.models.User_Profile.validate_zip])),
                ('state', models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('District of Columbia', 'District of Columbia'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], default='None Selected', max_length=128)),
                ('auth_status', models.CharField(choices=[('certified', 'Certified'), ('pending', 'Pending'), ('uncertified', 'Uncertified')], default='uncertified', max_length=16)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dining_pref1', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Non-Alcoholic Drinks', 'Non-Alcoholic Drinks'), ('Alcoholic Drinks', 'Alcoholic Drinks'), ('Dessert', 'Dessert'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('dining_pref2', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Non-Alcoholic Drinks', 'Non-Alcoholic Drinks'), ('Alcoholic Drinks', 'Alcoholic Drinks'), ('Dessert', 'Dessert'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('dining_pref3', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Non-Alcoholic Drinks', 'Non-Alcoholic Drinks'), ('Alcoholic Drinks', 'Alcoholic Drinks'), ('Dessert', 'Dessert'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('budget_pref', models.CharField(choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$'), ('$$$$', '$$$$'), ('No Preference', 'No Preference')], default='No Preference', max_length=15)),
                ('location_pref', models.CharField(choices=[('Near Home', 'Near Home'), ('Within My Borough', 'Within My Borough'), ('Outside My Borough', 'Outside My Borough'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('dietary_pref', models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Gluten-Free', 'Gluten-Free'), ('Salads Available', 'Salads Available'), ('None', 'None')], default='None', max_length=20)),
                ('cuisine_pref1', models.CharField(choices=[('Asian', 'Asian'), ('American', 'American'), ('Caribbean', 'Caribbean'), ('European', 'European'), ('Indian', 'Indian'), ('Latin American', 'Latin American'), ('Mediterranean', 'Mediterranean'), ('Middle Eastern', 'Middle Eastern'), ('Southern', 'Southern'), ('No Preference', 'No Preference')], default='No Preference', max_length=16)),
                ('cuisine_pref2', models.CharField(choices=[('Asian', 'Asian'), ('American', 'American'), ('Caribbean', 'Caribbean'), ('European', 'European'), ('Indian', 'Indian'), ('Latin American', 'Latin American'), ('Mediterranean', 'Mediterranean'), ('Middle Eastern', 'Middle Eastern'), ('Southern', 'Southern'), ('No Preference', 'No Preference')], default='No Preference', max_length=16)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upreferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('review_context', models.TextField()),
                ('rating', models.PositiveIntegerField(blank=True, default=0)),
                ('level_entry_rating', models.PositiveIntegerField(blank=True, default=0)),
                ('wide_door_rating', models.PositiveIntegerField(blank=True, default=0)),
                ('accessible_table_rating', models.PositiveIntegerField(blank=True, default=0)),
                ('accessible_restroom_rating', models.PositiveIntegerField(blank=True, default=0)),
                ('accessible_path_rating', models.PositiveIntegerField(blank=True, default=0)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relate_busid', to='accessible_restaurant.restaurant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(default='default.jpg', upload_to='restaurant_profile_pics')),
                ('phone', models.CharField(blank=True, max_length=32)),
                ('address', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('zip_code', models.CharField(blank=True, max_length=16)),
                ('state', models.CharField(blank=True, max_length=32)),
                ('is_open', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='accessible_restaurant.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='accessible_restaurant.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='ApprovalPendingUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_documents', models.FileField(upload_to='documents/pdfs/')),
                ('auth_status', models.CharField(choices=[('approve', 'Approve'), ('pending', 'Pending'), ('disapprove', 'Disapprove')], default='N/A', max_length=16)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovalPendingRestaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_documents', models.FileField(upload_to='documents/pdfs/')),
                ('auth_status', models.CharField(choices=[('approve', 'Approve'), ('pending', 'Pending'), ('disapprove', 'Disapprove')], default='N/A', max_length=16)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_rest', to='accessible_restaurant.restaurant')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auth_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
