# Generated by Django 4.0.4 on 2022-05-26 10:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction_ecommerce_app', '0002_alter_article_initial_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('best_price', models.IntegerField()),
                ('finish_at', models.DateTimeField(default=datetime.datetime(2022, 5, 26, 10, 57, 50, 176157))),
                ('is_finnished', models.BooleanField(default=False)),
                ('actual_best_buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction_ecommerce_app.article')),
            ],
        ),
    ]
