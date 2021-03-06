# Generated by Django 3.0.4 on 2020-06-16 07:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluate', '0007_auto_20200531_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialTechnique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('brand', models.CharField(max_length=100, verbose_name='Markası')),
                ('tip', models.CharField(max_length=100, verbose_name='Tip')),
                ('launched_year', models.DateTimeField(verbose_name='Buraxılış ili')),
                ('registration_plate', models.CharField(max_length=7, verbose_name='Dövlət qeydiyyat nişanı')),
                ('ban', models.CharField(max_length=100, verbose_name='Ban')),
                ('color', models.CharField(max_length=50, verbose_name='Rəngi')),
                ('fuel_type', models.CharField(max_length=50, verbose_name='Yanacaq növü')),
                ('dwarf_number', models.CharField(max_length=100, verbose_name='Mükərrikin nömrəsi')),
                ('engine_capacity', models.CharField(max_length=100, verbose_name='Mühərrikin həcmi')),
                ('texpassport_number', models.CharField(max_length=100, verbose_name='Tex pasportun nömrəsi')),
                ('texpassport_issuedate', models.DateTimeField(verbose_name='Tex pasportun verilmə tarixi')),
                ('walking', models.CharField(max_length=100, verbose_name='Yürüş')),
                ('wheels', models.CharField(max_length=100, verbose_name='Təkərləri')),
                ('flashlights', models.CharField(max_length=100, verbose_name='Fənərləri')),
                ('salon', models.CharField(max_length=100, verbose_name='Salon')),
                ('wings', models.CharField(max_length=100, verbose_name='Qanadlar')),
                ('doors', models.CharField(max_length=100, verbose_name='Qapılar')),
                ('accumulator', models.CharField(max_length=100, verbose_name='Akumlyator')),
                ('gearbox', models.CharField(max_length=100, verbose_name='Sürətli ötürücü qutusu')),
                ('engine', models.CharField(max_length=100, verbose_name='Mühərriki')),
                ('buffers', models.CharField(max_length=100, verbose_name='Buferlər')),
                ('bottles', models.CharField(max_length=100, verbose_name='Şüşələr')),
                ('air_conditioner', models.BooleanField(verbose_name='Kondisioner')),
                ('airbags', models.BooleanField(verbose_name='Təhlükəsizlik yastıqları')),
                ('centralized_management_system', models.BooleanField(verbose_name='Mərkəzləşdirilmiş idarə etmə sistemi')),
                ('audio_system', models.BooleanField(verbose_name='Audio sistem')),
                ('general_condition', models.CharField(max_length=255, verbose_name='Ümumi vəziyyəti')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_specialtechnique', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='SemiTrailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('brand', models.CharField(max_length=100, verbose_name='Markası')),
                ('tip', models.CharField(max_length=100, verbose_name='Tip')),
                ('launched_year', models.DateTimeField(verbose_name='Buraxılış ili')),
                ('registration_plate', models.CharField(max_length=7, verbose_name='Dövlət qeydiyyat nişanı')),
                ('ban', models.CharField(max_length=100, verbose_name='Ban')),
                ('color', models.CharField(max_length=50, verbose_name='Rəngi')),
                ('texpassport_number', models.CharField(max_length=100, verbose_name='Tex pasportun nömrəsi')),
                ('texpassport_issuedate', models.DateTimeField(verbose_name='Tex pasportun verilmə tarixi')),
                ('wheels', models.CharField(max_length=100, verbose_name='Təkərləri')),
                ('flashlights', models.CharField(max_length=100, verbose_name='Fənərləri')),
                ('salon', models.CharField(max_length=100, verbose_name='Salon')),
                ('wings', models.CharField(max_length=100, verbose_name='Qanadlar')),
                ('doors', models.CharField(max_length=100, verbose_name='Qapılar')),
                ('buffers', models.CharField(max_length=100, verbose_name='Buferlər')),
                ('refrigerator', models.BooleanField(verbose_name='Refrejerator(Soyuducu)')),
                ('centralized_management_system', models.BooleanField(verbose_name='Mərkəzləşdirilmiş idarə etmə sistemi')),
                ('general_condition', models.CharField(max_length=255, verbose_name='Ümumi vəziyyəti')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_semitrailer', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='OtherTransportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('technical_indicators', ckeditor.fields.RichTextField(verbose_name='Texiniki Göstəriciləri(Ümumi məlumat)')),
                ('technical_characteristics', ckeditor.fields.RichTextField(verbose_name='Texiniki Xarakterizəsi(Ümumi məlumat)')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_othertransportation', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='OtherMoveableState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('order_name', models.CharField(max_length=255, verbose_name='Adı')),
                ('color', models.CharField(max_length=100, verbose_name='Rəngi')),
                ('general_information', ckeditor.fields.RichTextField(verbose_name='Ümumi məlumat')),
                ('condition', models.CharField(max_length=255, verbose_name='Vəziyyəti')),
                ('number', models.IntegerField(verbose_name='Sayı')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_othermoveablestate', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='HouseholdAppliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('order_name', models.CharField(max_length=255, verbose_name='Adı')),
                ('color', models.CharField(max_length=100, verbose_name='Rəngi')),
                ('number', models.IntegerField(verbose_name='Sayı')),
                ('price_for_one', models.FloatField(verbose_name='Bir ədədinin qiyməti')),
                ('condition', models.CharField(max_length=255, verbose_name='Vəziyyəti')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_householdappliance', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('order_name', models.CharField(max_length=255, verbose_name='İlkin görüşdə adı')),
                ('number', models.IntegerField(verbose_name='Sayı (dəst, cüt, ədəd)')),
                ('weight', models.CharField(max_length=100, verbose_name='Lom vəziyyətdə ümumi çəkisi (qram)')),
                ('earring', models.CharField(max_length=100, verbose_name='Əyyar')),
                ('note', ckeditor.fields.RichTextField(null=True, verbose_name='Qeyd')),
                ('price_for_earring', models.FloatField(verbose_name='Əyyara görə qiymət (AZN)')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_gold', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Electronica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('order_name', models.CharField(max_length=255, verbose_name='Sifarişin adı')),
                ('number', models.IntegerField(verbose_name='Sayı')),
                ('condition', models.CharField(max_length=255, verbose_name='Vəziyyəti')),
                ('general_information', ckeditor.fields.RichTextField(verbose_name='Ümumi məlumat')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_electronica', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=255, verbose_name='Sifariş nömrəsi')),
                ('brand', models.CharField(max_length=100, verbose_name='Markası')),
                ('tip', models.CharField(max_length=100, verbose_name='Tip')),
                ('launched_year', models.DateTimeField(verbose_name='Buraxılış ili')),
                ('registration_plate', models.CharField(max_length=7, verbose_name='Dövlət qeydiyyat nişanı')),
                ('ban', models.CharField(max_length=100, verbose_name='Ban')),
                ('color', models.CharField(max_length=50, verbose_name='Rəngi')),
                ('fuel_type', models.CharField(max_length=50, verbose_name='Yanacaq növü')),
                ('dwarf_number', models.CharField(max_length=100, verbose_name='Mükərrikin nömrəsi')),
                ('engine_capacity', models.CharField(max_length=100, verbose_name='Mühərrikin həcmi')),
                ('texpassport_number', models.CharField(max_length=100, verbose_name='Tex pasportun nömrəsi')),
                ('texpassport_issuedate', models.DateTimeField(verbose_name='Tex pasportun verilmə tarixi')),
                ('walking', models.CharField(max_length=100, verbose_name='Yürüş')),
                ('wheels', models.CharField(max_length=100, verbose_name='Təkərləri')),
                ('flashlights', models.CharField(max_length=100, verbose_name='Fənərləri')),
                ('salon', models.CharField(max_length=100, verbose_name='Salon')),
                ('wings', models.CharField(max_length=100, verbose_name='Qanadlar')),
                ('doors', models.CharField(max_length=100, verbose_name='Qapılar')),
                ('accumulator', models.CharField(max_length=100, verbose_name='Akumlyator')),
                ('gearbox', models.CharField(max_length=100, verbose_name='Sürətli ötürücü qutusu')),
                ('engine', models.CharField(max_length=100, verbose_name='Mühərriki')),
                ('buffers', models.CharField(max_length=100, verbose_name='Buferlər')),
                ('bottles', models.CharField(max_length=100, verbose_name='Şüşələr')),
                ('air_conditioner', models.BooleanField(verbose_name='Kondisioner')),
                ('airbags', models.BooleanField(verbose_name='Təhlükəsizlik yastıqları')),
                ('centralized_management_system', models.BooleanField(verbose_name='Mərkəzləşdirilmiş idarə etmə sistemi')),
                ('audio_system', models.BooleanField(verbose_name='Audio sistem')),
                ('general_condition', models.CharField(max_length=255, verbose_name='Ümumi vəziyyəti')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('subcategory_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories_car', to='evaluate.SubCategory', verbose_name='Alt Kateqoriya')),
            ],
        ),
    ]
