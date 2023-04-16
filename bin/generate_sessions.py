"""
Generate 2023 session md and tweet CSV from pretalx schedule
Requires `TOKEN` environment variable (pretalx API token)
"""
from argparse import ArgumentParser
import csv
import json
import os
from pathlib import Path
import random
import re
from urllib.parse import urljoin

import requests

BASE_PATH = Path(__file__).parent.parent 

def api_get(path):
    api_url = urljoin("https://pretalx.com/api/v2", path)
    resp = requests.get(api_url, headers={"Authorization": f"Token {os.getenv('TOKEN')}"})
    return resp.json()


def get_talks(refetch=False):
    selections_path = BASE_PATH / "talks.json"
    def _relevant_session_type(talk):
        if talk['submission_type'] == "Talk":
            return True
        return talk['submission_type']['en'] in ["Workshop", "Keynote"]

    if selections_path.exists() and refetch is False:
        return json.load(selections_path.open())
    else:
        resp = api_get("events/djangocon-europe-2023/talks/?limit=50")
        submissions = {
            result["code"]: result for result in resp["results"] if _relevant_session_type(result) 
        }
        with selections_path.open("w") as out:
            json.dump(submissions, out)
        return submissions


def get_speakers(talk_codes, refetch=False):
    speakers_path = BASE_PATH / "speakers.json"
    if speakers_path.exists() and refetch is False:
        return json.load(speakers_path.open())
    else:
        resp = api_get("events/djangocon-europe-2023/speakers/?limit=200")
        speakers = {
            result["code"]: result for result in resp["results"] if any(sub in talk_codes for sub in result['submissions'])
        }
        with speakers_path.open("w") as out:
            json.dump(speakers, out)
        return speakers


def update_info(talk, speakers):
    formatted = {
        "title": talk["title"],
        "slug": re.sub(r'\W+', '-', talk["title"]).strip('-').lower(),
        "url": f"https://pretalx.com/djangocon-europe-2023/talk/{talk['code']}",
        "type": talk["submission_type"] if isinstance(talk["submission_type"], str) else talk["submission_type"]["en"],
        "state": talk["state"],
        "speakers": [speaker["name"] for speaker in talk["speakers"]],
        "slot": talk["slot"]
    }
    formatted["title"] = formatted["title"].replace("Keynote: ", "")
    first_speaker = talk["speakers"][0]
    formatted["photo_url"] = speakers[first_speaker["code"]]["avatar"]
    return formatted


def generate_session_md(session):
    speakers = "\n".join([f"  - {speaker}" for speaker in session["speakers"]])
    markdown = f"""---
hidden: false
layout: session-speaker-template
speakers: 
{speakers}
permalink: /sessions/{session['slug']}/
session_type: {session['type']}
session_title: "{session['title']}"
photo_url: {session['photo_url']}
twitter: null
website: null
---

"""
    with open(BASE_PATH / "_sessions" / f"{session['slug']}.md", "w") as outfile:
        outfile.write(markdown)


def generate_tweet(talk):
    emoji = {
        "Talk": "🎙",
        "Workshop": "🎙",
        "Keynote": "⭐️",
    }
    content = f'''{emoji[talk['type']]} {talk['type'].upper()}: "{talk['title']}" by {" & ".join(talk['speakers'])}
    
Grab your ticket!
https://2023.djangocon.eu/tickets
'''
    thumbnail_url = f"https://2023.djangocon.eu/sessions/{talk['slug']}"
    return content, thumbnail_url

def generate_tweet_csv(formatted_talks):
    # randomly shuffle the talks before we generate the tweet content
    random.shuffle(formatted_talks)
    with open(BASE_PATH / "tweets.csv", "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Content", "thumbnail_url"])
        for talk in formatted_talks:
            writer.writerow(generate_tweet(talk))


def main(refetch=False):
    talks = get_talks(refetch=refetch)
    speakers = get_speakers(talks.keys(), refetch=refetch)    
    formatted_talks = [update_info(talk, speakers) for talk in talks.values()]
    
    for talk in formatted_talks:
        generate_session_md(talk)
    
    generate_tweet_csv(formatted_talks)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.description = """
    Build session thumbnails and csv of tweet content from pretalx schedule
    """
    parser.add_argument(
        "--refetch", "-r", action="store_true", 
        help="Fetch schedule info from pretalx"
    )
    parsed = parser.parse_args()
    main(parsed.refetch)
