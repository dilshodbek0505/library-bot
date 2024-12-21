# Generated by Django 5.1.4 on 2024-12-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('telegram_id', models.CharField(max_length=128, verbose_name='Telegram ID of the bot admin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]