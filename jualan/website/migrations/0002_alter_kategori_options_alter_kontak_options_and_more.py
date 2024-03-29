# Generated by Django 4.2.6 on 2023-11-21 02:46

import ckeditor.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': 'Kategori'},
        ),
        migrations.AlterModelOptions(
            name='kontak',
            options={'verbose_name_plural': 'Kontak'},
        ),
        migrations.AlterModelOptions(
            name='produk',
            options={'verbose_name_plural': 'Produk'},
        ),
        migrations.AlterModelOptions(
            name='profil',
            options={'verbose_name_plural': 'Profil'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'verbose_name_plural': 'Slide'},
        ),
        migrations.AlterModelOptions(
            name='statis',
            options={'verbose_name_plural': 'Statis'},
        ),
        migrations.AddField(
            model_name='produk',
            name='aktif',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='banner_satu',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=80, scale=None, size=[575, 200], upload_to='gambar/banner', verbose_name='Gambar (575 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to='gambar/banner', verbose_name='Gambar (200 x 200 pixel)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_dua',
            field=models.ImageField(blank=True, null=True, upload_to='gambar/banner'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_empat',
            field=models.ImageField(blank=True, null=True, upload_to='gambar/banner'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_lima',
            field=models.ImageField(blank=True, null=True, upload_to='gambar/banner'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_satu',
            field=models.ImageField(blank=True, null=True, upload_to='gambar/banner'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar_tiga',
            field=models.ImageField(blank=True, null=True, upload_to='gambar/banner'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='keterangan',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
