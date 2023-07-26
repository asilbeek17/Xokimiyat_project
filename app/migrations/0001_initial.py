# Generated by Django 4.2.3 on 2023-07-26 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': "Bog'lanish",
                'verbose_name_plural': "Bog'lanishlar",
            },
        ),
        migrations.CreateModel(
            name='Holati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='state/')),
                ('title', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Holat',
                'verbose_name_plural': 'Holati',
            },
        ),
        migrations.CreateModel(
            name='Loyiha_turlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='loyiha_turi/')),
                ('title', models.CharField(max_length=155)),
            ],
            options={
                'verbose_name': 'Loyiha_turi',
                'verbose_name_plural': 'Loyiha_turlari',
            },
        ),
        migrations.CreateModel(
            name='Shaharlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='City_image/')),
                ('image2', models.ImageField(upload_to='City_image/')),
                ('image3', models.ImageField(upload_to='City_image/')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Shahar',
                'verbose_name_plural': 'Shaharlar',
            },
        ),
        migrations.CreateModel(
            name='Tumanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='Region_image/')),
                ('image2', models.ImageField(upload_to='Region_image/')),
                ('image3', models.ImageField(upload_to='Region_image/')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Tuman',
                'verbose_name_plural': 'Tumanlar',
            },
        ),
        migrations.CreateModel(
            name='Loyihalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='', verbose_name='upload_to/Loyihalar/')),
                ('image2', models.ImageField(upload_to='', verbose_name='upload_to/Loyihalar/')),
                ('image3', models.ImageField(upload_to='', verbose_name='upload_to/Loyihalar/')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('loyiha_turi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.loyiha_turlari')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.holati')),
            ],
            options={
                'verbose_name': 'Loyiha',
                'verbose_name_plural': 'Loyihalar',
            },
        ),
    ]