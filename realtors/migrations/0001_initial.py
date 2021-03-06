# Generated by Django 3.2.4 on 2021-06-16 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('photo', models.ImageField(upload_to='realtors')),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=30)),
                ('is_mvp', models.BooleanField(default=False)),
                ('hire_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
