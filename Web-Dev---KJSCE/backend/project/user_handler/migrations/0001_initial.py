# Generated by Django 4.2.2 on 2023-08-19 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(choices=[('Comps', 'Computer Science'), ('IT', 'Information Technology'), ('EXTC', 'Electronics and Telecommunication'), ('ETRX', 'Electronics'), ('MECH', 'Mechanical')], max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('sem', models.IntegerField()),
                ('scheme_name', models.CharField(max_length=100)),
                ('credit', models.IntegerField()),
                ('hours', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.branch', to_field='branch_name')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('dept', models.CharField(max_length=100)),
                ('employee_code', models.PositiveIntegerField()),
                ('faculty_name', models.CharField(max_length=100)),
                ('employee_abbreviation', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('faculty_email', models.EmailField(max_length=100)),
                ('experience', models.PositiveIntegerField()),
                ('post', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
            options={
                'verbose_name': 'Faculty',
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'faculty'), (3, 'staff'), (4, 'admin')], primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('dept', models.CharField(max_length=100)),
                ('employee_code', models.PositiveIntegerField()),
                ('staff_name', models.CharField(max_length=100)),
                ('employee_abbreviation', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('staff_email', models.EmailField(max_length=100)),
                ('experience', models.PositiveIntegerField()),
                ('post', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.branch')),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.course')),
                ('faculty_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.faculty')),
                ('staff_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.staff')),
            ],
            options={
                'verbose_name': 'Year',
                'verbose_name_plural': 'Year',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('roll_number', models.PositiveBigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('student_contact_no', models.CharField(max_length=20)),
                ('parents_contact_no', models.CharField(max_length=20)),
                ('parent_email_id', models.EmailField(max_length=100)),
                ('proctor_Abbreviation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.faculty')),
                ('student_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_handler.branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Proctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
            options={
                'verbose_name': 'Proctor',
                'verbose_name_plural': 'Proctors',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email')),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(to='user_handler.role'),
        ),
    ]
