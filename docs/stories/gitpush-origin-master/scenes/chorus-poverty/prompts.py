"""Round 1 prompts for the chorus "Skid Row Britain" (Kai, 10 Nov): the economic twin of Outbreak Night.
Writes moodboard.json rows [beat, id, look, prompt]. The look column names the light and the camera, so Kai picks both.
Files: <media>/moodboard/<id>.jpg (two candidates per prompt: <id>-a / -b in r1/, renamed by the runner).
  python3 prompts.py
"""
import json, pathlib

_STOCK = ("photographed like a feature film on 35mm stock: fine grain, deep shadows that stay dark, no lens flare, "
          "no bloom, no teal-orange grade. 16:9. No writing anywhere in the frame: no signs, banners, logos, number "
          "plates or screen text. No children.")
DUSK = "Winter dusk in a near-future Britain, cold blue-grey light, the only warm colour the small orange fires of braziers and camping stoves; " + _STOCK
GREY = "Flat grey overcast winter daylight in a near-future Britain, muted cold colour, drizzle in the air; " + _STOCK
NIGHT = "Winter night in a near-future Britain, the streetlights dead, lit only by braziers, camping lanterns and the glow of the city's towers; " + _STOCK

ROWS = [
 # MW, the motorway is a town (the kick: the biggest frame)
 ('MW', 'MW1-a', 'dusk · straight-down drone, the graphic grid',
  "Straight down from a drone high above an eight-lane British motorway that has become a town: no traffic, every "
  "lane filled edge to edge with tents, blue tarps, sleeping cars with blankets in the windows and cooking fires, "
  "washing strung between the crash barriers, thousands of small figures moving between them, smoke drifting "
  "across the lanes. " + DUSK),
 ('MW', 'MW1-b', 'grey · long lens up the carriageway, compressed to the horizon',
  "A very long telephoto lens looking straight up a British motorway from a footbridge: a shanty town of tarps, "
  "pallet huts and tents fills every lane for miles, compressed into one dense wall climbing a hill to the "
  "horizon, people in heavy coats walking down the central reservation carrying water containers, a dead gantry "
  "overhead. " + GREY),
 ('MW', 'MW1-c', 'night · aerial over Spaghetti Junction, a city of fires',
  "High aerial at night over a vast stacked British motorway interchange of curving concrete flyovers: every deck "
  "is a camp, hundreds of small fires and lanterns tracing the curves of the flyovers like a map of the roads, "
  "the town beyond completely dark except for one cluster of brightly lit office towers on the skyline. " + NIGHT),

 # QU, the queue
 ('QU', 'QU1-a', 'grey · aerial, a queue across Westminster Bridge',
  "Aerial over the Thames in London: a single queue of people four abreast stretches across the whole length of "
  "Westminster Bridge, round Parliament Square and away up the Embankment out of frame, thousands of people in "
  "winter coats and hoods waiting, at its head one small white van with its back doors open handing out bread. " + GREY),
 ('QU', 'QU1-b', 'dusk · long lens down a terraced street, the queue to the horizon',
  "Long lens at eye level down a straight Victorian terraced street on a hill in a northern English town: a "
  "queue of adults on the pavement runs the length of the street, over the brow of the hill and on to the "
  "horizon, people holding plastic bags and flasks, some sitting on the kerb, a church hall door lit at the very "
  "front. Breath steaming. " + DUSK),
 ('QU', 'QU1-c', 'grey · wide, a queue across a frozen field to one lorry',
  "Wide shot across frosted farmland in the English Midlands: a queue of thousands of people snakes back and "
  "forth across the whole field like a festival crowd with nothing to celebrate, all facing one parked articulated "
  "lorry with its side open where volunteers pass out sacks of potatoes. A power station's cooling towers on the "
  "horizon. " + GREY),

 # PK, the parks
 ('PK', 'PK1-a', 'dusk · high and wide, Hyde Park a shanty city with the skyline',
  "From a high window looking over Hyde Park in London at dusk: the whole park, lawns and avenues of plane trees, "
  "has become a shanty city of tarps, tents and pallet shacks to the horizon, hundreds of thin columns of cooking "
  "smoke rising, and beyond it the towers of the City lit bright in every window. " + DUSK),
 ('PK', 'PK1-b', 'grey · from Primrose Hill, people on the bench, London below',
  "From the top of Primrose Hill, behind a row of people in sleeping bags sitting along the benches, looking out "
  "over London: every park, square and playing field in sight is grey with tents, and smoke from thousands of "
  "small fires lies over the city in a flat haze. " + GREY),
 ('PK', 'PK1-c', 'night · a village green, the pub dark, a camp round the war memorial',
  "An English village green at night: the pub dark, the church dark, the whole green filled with tents and "
  "parked cars people are living in, a ring of adults round a brazier at the foot of a stone war memorial, the "
  "only light the fire and a few camping lanterns. " + NIGHT),

 # ST, indoors
 ('ST', 'ST1-a', 'grey · wide from the gallery, a station concourse as a dormitory',
  "From a high gallery in a vast Victorian railway terminus in London: the whole concourse under the iron and "
  "glass roof is a dormitory, thousands of sleeping bags and camp beds laid in rows on the floor, no trains at the "
  "platforms, the departure boards dark, grey daylight falling through the roof glass. " + GREY),
 ('ST', 'ST1-b', 'dusk · the national stadium, the pitch a camp',
  "Wide from the top tier of a huge British football stadium: the pitch and the running track are covered edge "
  "to edge in tents and camp beds, people queueing at portable water tanks along the touchline, the giant "
  "floodlights off, the stands empty and grey, smoke from cooking stoves hanging under the roof. " + DUSK),
 ('ST', 'ST1-c', 'night · down the nave of a cathedral, sleeping bags to the altar',
  "Down the length of a Gothic English cathedral nave at night: the pews pushed aside and the stone floor "
  "covered in sleeping bags and blankets right up to the altar, hundreds of people asleep, candles and camping "
  "lanterns the only light on the pillars, breath in the cold air. " + NIGHT),

 # ES, the estates
 ('ES', 'ES1-a', 'grey · down a suburban street, every house evicted',
  "Down a 1930s suburban street of semi-detached houses in the rain: every single house has steel shutters over "
  "its windows and door, and every front garden is piled with the family's furniture, mattresses, a sofa, boxes "
  "and lamps under bin bags, a few adults standing by their piles, a line of grey vans at the kerb. " + GREY),
 ('ES', 'ES1-b', 'dusk · a council tower block, every window boarded but one',
  "Low angle up a 1960s council tower block at dusk: every window on every floor boarded with grey steel sheets "
  "except one, where a single lamp still glows, and at its foot on the grass a camp of tents and furniture "
  "where the tenants now live. " + DUSK),
 ('ES', 'ES1-c', 'grey · long lens, a terrace with every door left open',
  "Long lens down a terrace of red-brick two-up two-down houses: every front door is open, the houses empty, "
  "and the pavement is lined both sides with the contents of the whole street, beds, wardrobes, washing machines, "
  "a woman in a dressing gown sitting in an armchair on the pavement looking at her house. " + GREY),

 # HS, the high street
 ('HS', 'HS1-a', 'night · the length of a high street, someone in every doorway',
  "Down the full length of a British market-town high street at night: every shop has its shutters down, and "
  "in every single doorway, all the way to the vanishing point, someone is sleeping in a sleeping bag, a few "
  "candles and lanterns, wet pavement. " + NIGHT),
 ('HS', 'HS1-b', 'grey · a shopping centre atrium turned into a camp',
  "Inside a two-storey British shopping centre, every shop unit dark behind its grille: the atrium floor and both "
  "galleries are packed with tents, laundry hung from the balconies, people sitting on the dead escalators, grey "
  "daylight from the glass roof. " + GREY),
 ('HS', 'HS1-c', 'dusk · a seaside promenade, shelters and beach full',
  "A British seaside promenade at dusk in winter: the Victorian shelters, the bandstand and the beach below "
  "are covered in tents and tarps, the pier's lights dead, the sea grey, and people walking the promenade "
  "with everything they own in shopping trolleys. " + DUSK),

 # FI, the fires
 ('FI', 'FI1-a', 'night · a frozen street of oil-drum fires',
  "A long straight terraced street at night with snow on the ground: a burning oil drum every twenty metres down "
  "the middle of the road, each one with a ring of adults in coats and blankets round it holding out their "
  "hands, the houses behind all dark. " + NIGHT),
 ('FI', 'FI1-b', 'night · under the flyover, one bonfire, a crowd',
  "Under a concrete motorway flyover at night: a huge bonfire of pallets and broken furniture, hundreds of "
  "people in a wide ring around it, faces lit orange, the concrete pillars receding into darkness behind them "
  "with tents between every pillar. " + NIGHT),
 ('FI', 'FI1-c', 'dusk · close, hands and faces round a brazier',
  "Close at a brazier made from a cut-down steel drum at dusk: the hands of five adults held out to the "
  "flames, a grey-stubbled man in a supermarket uniform fleece, a woman with a hospital lanyard still round her "
  "neck, behind them out of focus a field of tents. " + DUSK),

 # FC, through the fence (who gained, the machines that work)
 ('FC', 'FC1-a', 'night · crowd at the fence of a lit automated warehouse',
  "At night outside a vast automated distribution warehouse, its whole side open and blazing with white light, "
  "robot arms and conveyors working inside with not one person among them: a crowd of hundreds of people in "
  "coats stand pressed against the tall chain-link fence in the dark, looking in. " + NIGHT),
 ('FC', 'FC1-b', 'grey · factory gate shut, a crowd outside, the plant running',
  "A British car factory's main gate in the rain, the barrier down and chained, a crowd of former workers in "
  "work jackets standing outside it, and beyond the fence the long factory sheds lit inside and running, rows of "
  "orange robot arms visible through the open bay doors, no people inside. " + GREY),
 ('FC', 'FC1-c', 'dusk · a data centre in fields, the camp against its fence',
  "A huge windowless data centre in green English fields at dusk, its cooling fans turning, security lights "
  "bright on its white walls: right up against its perimeter fence a camp of tents and parked cars, cooking "
  "fires, people sitting with their backs to the fence where it is warm from the exhaust vents. " + DUSK),

 # GL, everywhere in Britain (one beat each)
 ('GL', 'GL1-a', 'grey · Manchester, the canal under the railway arches',
  "Manchester: a canal towpath running under a long row of red-brick Victorian railway arches, every arch "
  "bricked-in space turned into a home of tarps and pallets, narrowboats moored nose to tail full of people, "
  "mill buildings dark behind. " + GREY),
 ('GL', 'GL1-b', 'dusk · Glasgow, the Clyde, camps below the tenements',
  "Glasgow at dusk: along the river Clyde below sandstone tenements and the shipyard cranes, both banks are "
  "lined with tents and tarps for a mile, fires along the water's edge, the tenements' windows dark. " + DUSK),
 ('GL', 'GL1-c', 'grey · the Welsh valleys, tents up the hillside',
  "A South Wales valley: long terraces of houses stepping up the hillside with their windows boarded, and above "
  "them the whole green hillside up to the old pit head is dotted with tents and smoke, people walking up the "
  "path with water. " + GREY),
 ('GL', 'GL1-d', 'night · Blackpool, the illuminations dead, caravans on the sand',
  "A northern seaside resort at night: the tower and the illuminations dead and dark, the long beach below the "
  "promenade filled with caravans, tents and parked cars people are living in, small fires along the tideline. " + NIGHT),

 # HA, hands (the inserts; the twin of Outbreak's cup)
 ('HA', 'HA1-a', 'grey · macro, rain filling a paper cup held out',
  "Macro close-up of a paper coffee cup held out from a sleeping bag on a wet pavement by a bare, chapped hand: "
  "the cup is empty of coins and slowly filling with rain, drops making rings on the water inside, the rim "
  "sharp, the passing legs behind soft and out of focus. " + GREY),
 ('HA', 'HA1-b', 'dusk · close, keys dropped through a letterbox',
  "Close on the brass letterbox of a front door from inside the hall: a hand pushing a bunch of house keys "
  "through it from outside, the keys about to drop onto a doormat already covered in unopened letters, the hall "
  "behind empty of furniture. " + DUSK),
 ('HA', 'HA1-c', 'night · overhead, coins counted short on a kitchen table',
  "Overhead on a kitchen table at night lit by one camping lantern: two hands counting a small pile of pound "
  "coins and pennies into stacks, beside them a single tin of beans and a stack of opened envelopes, the "
  "electricity off. " + NIGHT),
 ('HA', 'HA1-d', 'grey · close, a work lanyard in the gutter',
  "Close at kerb level on a wet British street: a work ID lanyard and badge lying in the gutter water, the photo "
  "on it turned face down, rain running past it, out of focus behind a line of people's boots walking past in a "
  "queue. " + GREY),

 # TW, who it was for (the button, into the banks)
 ('TW', 'TW1-a', 'night · the City lit above a tent city on the Thames foreshore',
  "London at night from the south bank of the Thames: in the foreground the river's mud foreshore and the "
  "embankment covered with tents and small fires, and across the water the towers of the City blaze with light "
  "in every window, every floor bright and busy with screens, not one person at a desk. " + NIGHT),
 ('TW', 'TW1-b', 'dusk · from Greenwich hill, a camp in the foreground, Canary Wharf lit',
  "From the hill in Greenwich Park at dusk, past a camp of tents and a brazier in the foreground with people "
  "wrapped in blankets watching: across the river the cluster of glass towers on the Isle of Dogs glows warm and "
  "fully lit, cranes still building another one. " + DUSK),
 ('TW', 'TW1-c', 'night · straight up a glass tower from a doorway on the street',
  "From a sleeping bag in the doorway at the foot of a glass office tower at night, looking straight up its "
  "side: every floor above lit cold white, rows of empty desks and glowing screens and server racks, nobody "
  "anywhere inside, the tower climbing into low cloud. A pair of worn trainers in the bottom of the frame. " + NIGHT),
 ('TW', 'TW1-d', 'night · aerial, a dark city of fires and one lit district',
  "High aerial over a big British city at night: no streetlights anywhere, the whole city dark but for "
  "thousands of tiny orange fires, and in the middle one district of glass towers and data halls fully lit, "
  "bright as day, like an island. " + NIGHT),
]

# Two candidates per prompt (flow_generate_batch numOutputs 2): rows 0-17 went to moodboard/r1/NN-a|b.jpg, rows 18-35 to
# moodboard/r1b/NN-a|b.jpg. Each candidate is its own mood-board card, id <prompt id><1|2> (MW1-a1, MW1-a2), copied to
# moodboard/<id>.jpg with its recipe card.
import shutil
MEDIA = pathlib.Path('/mnt/d/badcode-videos/gitpush-origin-master/clips/chorus-poverty/moodboard')
out_rows = []
for i, (beat, pid, look, prompt) in enumerate(ROWS):
    src_dir, n = (MEDIA / 'r1', i) if i < 18 else (MEDIA / 'r1b', i - 18)
    for c, suf in (('a', '1'), ('b', '2')):
        cid = pid + suf
        src = src_dir / f'{n:02d}-{c}.jpg'
        if src.exists():
            shutil.copyfile(src, MEDIA / f'{cid}.jpg')
            if src.with_suffix('.jpg.prov.json').exists():
                shutil.copyfile(src.with_suffix('.jpg.prov.json'), MEDIA / f'{cid}.jpg.prov.json')
        out_rows.append([beat, cid, look, prompt])
out = pathlib.Path(__file__).with_name('moodboard.json')
out.write_text(json.dumps(out_rows, indent=1))
ROWS = out_rows
print(len(ROWS), 'rows ->', out)
