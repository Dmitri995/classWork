# Generated by Django 4.0 on 2024-01-12 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='заголовок')),
                ('description', models.TextField(verbose_name='Содержание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_auth.profile', verbose_name='профиль')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'публикации',
                'db_table': 'records',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ImagesRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='records/')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='my_auth.record')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
                'db_table': 'images2record',
            },
        ),
    ]
