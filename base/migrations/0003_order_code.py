# Generated by Django 4.0.4 on 2022-04-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_category_remove_order_description_remove_order_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.CharField(default=1111, max_length=100),
            preserve_default=False,
        ),
    ]
