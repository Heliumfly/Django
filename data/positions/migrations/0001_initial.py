# Generated by Django 2.1.7 on 2019-04-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=255)),
                ('job_name', models.CharField(max_length=255)),
                ('salary_range', models.CharField(max_length=255)),
                ('working_city', models.CharField(max_length=255)),
                ('experience_required', models.CharField(blank=True, max_length=255, null=True)),
                ('education_required', models.CharField(blank=True, max_length=255, null=True)),
                ('job_type', models.CharField(max_length=255)),
                ('position_label', models.CharField(blank=True, max_length=255, null=True)),
                ('publish_time', models.CharField(max_length=255)),
                ('job_advantage', models.TextField(blank=True, null=True)),
                ('job_detail', models.TextField()),
                ('working_address', models.CharField(max_length=255)),
                ('company_lagou_url', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_field', models.CharField(max_length=255)),
                ('financing_status', models.CharField(blank=True, max_length=255, null=True)),
                ('company_size', models.CharField(blank=True, max_length=255, null=True)),
                ('company_url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'positions',
                'managed': False,
            },
        ),
    ]
