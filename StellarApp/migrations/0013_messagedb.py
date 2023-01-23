# Generated by Django 4.1.2 on 2023-01-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StellarApp', '0012_alter_addproductdb_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='messagedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Subject', models.CharField(blank=True, max_length=100, null=True)),
                ('Message', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]