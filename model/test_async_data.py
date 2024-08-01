import asyncio
from pprint import pprint
import spacy
from geopy.geocoders import Nominatim
import json
import os

# Load the SpaCy model
nlp = spacy.load("en_core_web_trf")

# Read the text file and split it into chapters
chapters = []
chapter_num = 0
file_path = './data/JamesJoyce-Ulysses_Ans.txt'

with open(file_path, "r", encoding='utf-8-sig') as file:
    for line in file:
        if line.strip().startswith(f'[ {chapter_num + 1} ]'):
            chapter_num += 1
            chapters.append('')
        else:
            chapters[chapter_num - 1] += line

# Split each chapter into sentences
chapters_v2 = [chapter.split('\n\n') for chapter in chapters]

# Clean up and filter out empty lines
chapters_v3 = [[line.strip().replace('\n', ' ') for line in chapter if line.strip()] for chapter in chapters_v2]

async def get_gpe(chapter, num):
    print(f'RUN chapter {num}')
    if not os.path.exists('./dist/'):
        os.makedirs('./dist/')
    
    geolocator = Nominatim(user_agent="damn boy")
    ret = {}

    for line_num, line in enumerate(chapter):
        text = nlp(line)
        for ent in text.ents:
            if ent.label_ == "GPE":
                if ent.text not in ret:
                    ret[ent.text] = {"nominatim": [], "lines": [], "count": 0, 'text': []}
                    query = f"{ent.text}, Ireland"
                    location = geolocator.geocode(query)
                    if location:
                        ret[ent.text]["nominatim"] = [location.latitude, location.longitude]
                    else:
                        print(ent.text, "Location not found")
                ret[ent.text]["lines"].append(line_num)
                ret[ent.text]["text"].append(line)
                ret[ent.text]["count"] += 1

    json_output = json.dumps(ret, indent=4)
    
    with open(f'./dist/chapter_{num}.json', 'w') as f:
        f.write(json_output)

async def process_chapters(chapters):
    tasks = [get_gpe(chapter, num) for num, chapter in enumerate(chapters[:18], start=1)]
    asyncio.gather(*tasks)

# Run the event loop using the SelectorEventLoop
asyncio.set_event_loop(asyncio.SelectorEventLoop())
asyncio.run(process_chapters(chapters_v3))