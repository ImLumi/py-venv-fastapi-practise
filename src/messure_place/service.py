from prisma import Prisma


async def create_messure_place(data):
    db = Prisma()
    await db.connect()
    new_messure_place = await db.merohely.create({"hely": data['place'], "meres_tipusa": data['messure_type']})
    await db.disconnect()

    return new_messure_place


async def get_all():
    db = Prisma()
    await db.connect()
    all_messure_place = await db.merohely.find_many()
    await db.disconnect()
    return all_messure_place
