# Generated by Django 3.0 on 2022-11-29 15:55

from django.db import migrations


def migrate_address(apps, schema_editor):
    old_table = apps.get_model('oc_lettings_site', 'Address')
    new_table = apps.get_model('lettings', 'Address')

    objs = list()

    fields = ('number',
              'street',
              'city',
              'state',
              'zip_code',
              'country_iso_code')

    for data in old_table.objects.all():
        number = data.number
        street = data.street
        city = data.city
        state = data.state
        zip_code = data.zip_code
        country_iso_code = data.country_iso_code
        address = new_table(number=number,
                            street=street,
                            city=city,
                            state=state,
                            zip_code=zip_code,
                            country_iso_code=country_iso_code)
        print(address)
        objs.append(address)

    new_table.objects.bulk_create(objs)


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_address, migrations.RunPython.noop),
    ]
