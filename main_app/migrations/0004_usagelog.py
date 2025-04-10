# Generated by Django 5.1.7 on 2025-04-05 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_product_skincareproduct_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_time', models.DateTimeField()),
                ('usage_category', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening'), ('weekly', 'Weekly')], max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usage_logs', to='main_app.skincareproduct')),
            ],
        ),
    ]
