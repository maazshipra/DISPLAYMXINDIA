# Generated by Django 4.1.7 on 2023-03-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_enquiry_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='Product',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
