import json
import openai

# Load the JSON file
with open('/l/users/sanoojan.baliah/Felix/dataset_prep/descriptions/EuroSAT.json', 'r') as file:
    data = json.load(file)
# openai.api_key = ""
classes = []
print("Keys in the JSON file:")
for key in data.keys():
    classes.append(key)
all_responses = {}
for key in classes:
    class_name = key
    desc = []
    for value in data[key]:
        desc.append(value)
    desc_para = "\n".join(desc)
    # print(desc_para)

    message = f'Identify descriptive sentences for the class {class_name} from either a satellite or aerial photo. Choose the top 25 concise and informative sentences. Include sentences mentioning both "a satellite photo" and "an aerial photo". Ensure each sentence is clear and relevant. Your output should consist of exactly 25 selected sentences forming a coherent paragraph. Choose from the following options:\n{desc_para}'
    # chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": message}], # You need to format your message as a part of a conversation with "system" and "user" messages.
        max_tokens=2000,
        )       
    # reply = chat.choices[0].message.content
    # print(reply)
    all_result = []

    choices = response.get("choices", [])

    # Iterate through each choice and print its content
    for choice in choices:
        content = choice.get("message", {}).get("content", "")
        # Split the content into sentences based on periods
        sentences = [sentence.strip() for sentence in content.split(".")]
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence]
        # Append each sentence to the list
        number_of_sentences = len(sentences)
        if number_of_sentences!=25:
            new_message = "Selectly exactly 25 sentences"
            
        all_result.extend(sentences)
        break
        
    all_responses[class_name] = all_result
    break
with open("test.json", 'w') as f:
    json.dump(all_responses, f, indent=4)
    # exit()
    # breakpoint()