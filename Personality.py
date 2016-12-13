import json
import os
from watson_developer_cloud import PersonalityInsightsV3

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username='1f6819ef-5a1f-45cf-88b9-b4dfd9ddf982',
    password='0cFCCWqY2CSP')

script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
rel_path = 'personality-v3.json'
file_path = os.path.join(script_dir, rel_path)

with open(file_path) as profile_json:
    profile = personality_insights.profile(
        profile_json.read(), content_type='application/json',
        raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))