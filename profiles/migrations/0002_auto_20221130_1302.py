# Generated by Django 3.0 on 2022-11-30 12:02

from django.db import migrations


def migrate_profiles(apps, schema_editor):
    old_table = apps.get_model('oc_lettings_site', 'Profile')
    new_table = apps.get_model('profiles', 'Profile')

    objs = list()

    fields = ('favorite_city',
              'user_id')

    for data in old_table.objects.all():
        favorite_city = data.favorite_city
        user_id = data.user_id
        profile = new_table(favorite_city=favorite_city,
                            user_id=user_id)
        objs.append(profile)

    new_table.objects.bulk_create(objs)


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_profiles, migrations.RunPython.noop),
    ]
