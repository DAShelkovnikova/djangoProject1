# Generated by Django 5.1.1 on 2024-09-12 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название категории', max_length=100, verbose_name='Наименование категории')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название продукта', max_length=100, verbose_name='Наименование продукта')),
                ('description', models.TextField(help_text='Введите описание продукта', verbose_name='Описание продукта')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение продукта', null=True, upload_to='products/photo', verbose_name='Изображение продукта')),
                ('price', models.IntegerField(help_text='Введите цену за покупку', verbose_name='Цена за покупку')),
                ('created_at', models.DateField(blank=True, help_text='Укажите дату создания', null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateField(blank=True, help_text='Укажите дату последнего изменения', null=True, verbose_name='Дата последнего изменения')),
                ('views_counter', models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик просмотров')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('category', models.ForeignKey(blank=True, help_text='Введите название категории продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['category', 'name'],
            },
        ),
    ]
