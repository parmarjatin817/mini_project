from django.db import migrations


BLOOD_GROUPS = ("A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")


def add_blood_groups(apps, schema_editor):
    Bloodgroup = apps.get_model("bbdmsapp", "Bloodgroup")
    for bloodgroup in BLOOD_GROUPS:
        Bloodgroup.objects.get_or_create(bloodgroup=bloodgroup)


class Migration(migrations.Migration):

    dependencies = [
        ("bbdmsapp", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_blood_groups, migrations.RunPython.noop),
    ]
