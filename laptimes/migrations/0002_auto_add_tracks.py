from django.db import migrations

def add_tracks(apps, schema_editor):
    Track = apps.get_model('laptimes', 'Track')
    tracks = [
        "Bahrain International Circuit (Bahrein)",
        "Jeddah Street Circuit (Arábia Saudita)",
        "Albert Park Circuit (Austrália)",
        "Shanghai International Circuit (China)",
        "Miami International Autodrome (EUA)",
        "Autodromo Enzo e Dino Ferrari (Emília-Romanha, Itália)",
        "Circuit de Monaco (Mônaco)",
        "Circuit de Barcelona-Catalunya (Espanha)",
        "Circuit Gilles Villeneuve (Canadá)",
        "Red Bull Ring (Áustria)",
        "Silverstone Circuit (Reino Unido)",
        "Hungaroring (Hungria)",
        "Circuit de Spa-Francorchamps (Bélgica)",
        "Zandvoort Circuit (Países Baixos)",
        "Monza Circuit (Itália)",
        "Marina Bay Street Circuit (Singapura)",
        "Suzuka International Racing Course (Japão)",
        "Losail International Circuit (Catar)",
        "Circuit of the Americas (EUA)",
        "Autódromo Hermanos Rodríguez (México)",
        "Interlagos Circuit (Brasil)",
        "Las Vegas Street Circuit (EUA)",
        "Yas Marina Circuit (Abu Dhabi)",
        "Circuit Paul Ricard (França)",
        "Autódromo Internacional do Algarve (Portimão) (Portugal)"
    ]
    for track in tracks:
        Track.objects.create(name=track)

class Migration(migrations.Migration):

    dependencies = [
        ('laptimes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_tracks),
    ]