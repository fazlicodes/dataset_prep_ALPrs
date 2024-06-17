import os
import openai
import json
import pdb
from tqdm import tqdm

#openai.api_key = ""
json_name = "patternnet_60ish.json"

category_list = [
    "airplane",
    "baseball field",
    "basketball court",
    "beach",
    "bridge",
    "cemetery",
    "chaparral",
    "christmas tree farm",
    "closed road",
    "coastal mansion",
    "crosswalk",
    "dense residential",
    "ferry terminal",
    "football field",
    "forest",
    "freeway",
    "golf course",
    "harbor",
    "intersection",
    "mobile home park",
    "nursing home",
    "oil gas field",
    "oil well",
    "overpass",
    "parking lot",
    "parking space",
    "railway",
    "river",
    "runway",
    "runway marking",
    "shipping yard",
    "solar panel",
    "sparse residential",
    "storage tank",
    "swimming pool",
    "tennis court",
    "transformer station",
    "wastewater treatment plant"
]


print(len(category_list))
all_responses = {}
vowel_list = ['A', 'E', 'I', 'O', 'U']

for category in tqdm(category_list):

	if category[0] in vowel_list:
		article = "an"
	else:
		article = "a"

	prompts = []
	prompts.append("Describe a satellite photo of " + article + " " + category)
	prompts.append("Describe " + article + " " + category + " as it would appear in an aerial image")
	prompts.append("How does " + article + " " + category + " look like in an satellite photo?")
	prompts.append("How can you identify " + article + " " + category + "  in an aerial photo?")
	prompts.append("Describe the satellite photo of " + article + " "  + category)
	prompts.append("Describe an aerial photo of "  + article + " "  + category)
	# prompts.append("Describe how you can distinguish an aerial image of "  + article + " "  + category + " from other scene images")
	# prompts.append("Describe a medical image of "  + article + " "  + category )

	all_result = []
	for curr_prompt in prompts:
		response = openai.Completion.create(
		    engine="gpt-3.5-turbo-instruct",
		    prompt=curr_prompt,
		    temperature=.99,
			max_tokens = 50,
			n=13,
			stop="."
		)

		for r in range(len(response["choices"])):
			result = response["choices"][r]["text"]
			all_result.append(result.replace("\n\n", "") + ".")

	all_responses[category] = all_result

with open(json_name, 'w') as f:
	json.dump(all_responses, f, indent=4)