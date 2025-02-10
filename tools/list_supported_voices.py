from huggingface_hub import HfApi

api = HfApi()
files = api.list_repo_tree("hexgrad/Kokoro-82M", repo_type="model", revision="main", path_in_repo="voices")
model_names = [file.path.split('/')[-1].replace('.pt', '') for file in files if file.path.endswith('.pt')]

# for model in model_names:
#     print(model)

import csv

# CSV data as a string for demonstration purposes
csv_data = """acro,name,pipeline,espeak-ng
en,American English,a,en-us
en,British English,b,en-gb
jp,Japanese,j,ja
cn,Mandarin Chinese,z,cmn
es,Spanish,e,es
fr,French,f,fr-fr
in,Hindi,h,hi
it,Italian,i,it
br,Brazilian Portuguese,p,br-pt
"""

# Convert the CSV data to a list of dictionaries
csv_reader = csv.DictReader(csv_data.strip().split("\n"))
csv_list = list(csv_reader)

# Populate the voice_menu dictionary
voice_menu = {}
for voice_name in model_names:
    for row in csv_list:
        if voice_name[0] == row['pipeline']:
            voice_menu[f"{voice_name} ({row['acro']})"] = {
                "pipeline": row['pipeline'],
                "name": voice_name,
                "lang": row['espeak-ng']
            }

# Print the voice_menu dictionary with commas, except for the last item
print("voice_menu = {")
items = list(voice_menu.items())
for i, (key, value) in enumerate(items):
    if i < len(items) - 1:
        print(f'   "{key}": {value},')
    else:
        print(f'   "{key}": {value}')
print("}")
