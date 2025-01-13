from django.db import migrations

def convert_fecha_a_anno(apps, schema_editor):
    Producto = apps.get_model('laboratorio', 'Producto')
    for producto in Producto.objects.all():
        
        if producto.f_fabricacion:
            producto.f_fabricacion = producto.f_fabricacion.year
            producto.save()

class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_alter_producto_f_fabricacion'),
    ]

    operations = [
        migrations.RunPython(convert_fecha_a_anno),
    ]
