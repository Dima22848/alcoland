# Generated by Django 4.2.1 on 2023-05-20 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menulist_slug_alter_alcogol_name_alter_menulist_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alcogol',
            name='related_to_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menulist', verbose_name='Вид алкоголя'),
        ),
        migrations.AlterField(
            model_name='alcogol',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.type', verbose_name='Подвид алкоголя'),
        ),
        migrations.AlterField(
            model_name='snacks',
            name='related_to_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menulist', verbose_name='Закуски'),
        ),
        migrations.AlterField(
            model_name='type',
            name='related_to_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menulist', verbose_name='Вид алкоголя'),
        ),
    ]
