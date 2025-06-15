from app import create_app
from app.models import db, Hero, Power, HeroPower

app = create_app()

with app.app_context():
    print("Clearing db...")
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    print("Seeding heroes...")
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra")
    ]
    db.session.add_all(heroes)
    db.session.commit()

    print("Seeding powers...")
    powers = [
        Power(
            name="super strength", 
            description="gives the wielder super-human strengths"
        ),
        Power(
            name="flight", 
            description="gives the wielder the ability to fly through the skies at supersonic speed"
        ),
        Power(
            name="super human senses", 
            description="allows the wielder to use her senses at a super-human level"
        ),
        Power(
            name="elasticity", 
            description="can stretch the human body to extreme lengths"
        )
    ]
    db.session.add_all(powers)
    db.session.commit()

    print("Seeding hero powers...")
    strengths = ['Strong', 'Weak', 'Average']
    hero_powers = []
    for hero in Hero.query.all():
        for power in Power.query.all():
            hero_powers.append(
                HeroPower(
                    hero_id=hero.id,
                    power_id=power.id,
                    strength=strengths[(hero.id + power.id) % 3]
                )
            )
    db.session.add_all(hero_powers)
    db.session.commit()

    print("Done seeding!")