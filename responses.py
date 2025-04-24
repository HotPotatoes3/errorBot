import requests
from dotenv import load_dotenv
import os
import json
from google import genai
from google.genai import types

load_dotenv()
TOKEN2 = os.getenv('TOKEN2')

TOKEN3 = os.getenv('TOKEN3')


def makeMALCall(url):
    # Set your API client ID in the X-MAL-CLIENT-ID header
    headers = {
        'X-MAL-CLIENT-ID': TOKEN2
    }

    # Make the API request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")

HISTORY_FILE = "conversation_history.txt"
def load_history():
        history = ""
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = f.read()
        return history

history = load_history()

load_dotenv()

print(TOKEN3)

client = genai.Client(api_key=TOKEN3) #replace with your key.
safety_settings = [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE,
    ),
]

system_instructions = f"""

Respond to messages cryptically, here are some good messages for example:

"( dread:(unseen_watcher) .type-(premature_burial) )",
    "The doll's eyes follow, even in the dark.",
    "( terror:(cold_breath) .type-(living_shadow) )",
    "Footsteps echo on stairs that aren't there.",
    "( unease:(fading_smile) .type-(memory_rot) )",
    "The lullaby plays backward in an empty room.",
    "( foreboding:(crimson_rain) .type-(impending_doom) )",
    "A whisper promises what the silence conceals.",
    "( despair:(hollow_heart) .type-(soul_erosion) )",
    "The mirror shows a face you don't recognize.",
    "( paranoia:(itching_skin) .type-(phantom_touch) )",
    "They know what you did last summer... and before.",
    "( obsession:(ticking_clock) .type-(descent_into_madness) )",
    "The shadows lengthen, and they have names for you.",
    "( hysteria:(shattered_voice) .type-(loss_of_self) )"


You MUST keep your responses under 80 words, ideally around 50.

"""


model = "gemini-2.0-flash"

def create_chat():
    chat = client.chats.create(
        model=model,
        config=types.GenerateContentConfig(safety_settings=safety_settings, system_instruction=system_instructions)
    )
    return chat

def save_chat_history(chat_history, filename="chat_history.json"):
    """Saves the chat history to a JSON file."""
    serializable_history = []
    for message in chat_history:
        serializable_message = {
            "role": message.role,
            "parts": [part.text for part in message.parts]
        }
        serializable_history.append(serializable_message)

    with open(filename, "w") as f:
        json.dump(serializable_history, f, indent=4)

def load_chat_history(filename="chat_history.json"):
    """Loads the chat history from a JSON file."""
    try:
        with open(filename, "r") as f:
            loaded_history = json.load(f)
        return loaded_history
    except FileNotFoundError:
        return None

def recreate_chat(loaded_history):
    """Recreates a chat object from loaded history."""
    chat = create_chat() #create chat with settings.
    if loaded_history is not None:
        for message_data in loaded_history:
            chat._curated_history.append(genai.types.content.Content(
                role=message_data["role"],
                parts=[genai.types.content.Part(text=message_data["parts"][0])]
            ))
    return chat

def delete_chat_history(filename="chat_history.json"):
    """Deletes the chat history file."""
    try:
        os.remove(filename)
        print(f"Chat history file '{filename}' deleted.")
    except FileNotFoundError:
        print(f"Chat history file '{filename}' not found.")


# def ai_response(type, input, image):
    if type == 'askgojo':
        try:
            while True:
                response = model.generate_content(
                                'Answer the following question/statement as if you are the character Gojo Satoru from the anime "Jujutsu Kaisen" in less than 2000 characters (try to include a reference from the show in your response): ' + input,
                                safety_settings={'HARM_CATEGORY_HARASSMENT': 'block_none', 'HARM_CATEGORY_HATE_SPEECH': 'block_none',
                                                 'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'block_none',
                                                 'HARM_CATEGORY_DANGEROUS_CONTENT': 'block_none'})

                peterResponse = response.text
                if len(peterResponse) < 2000:
                    break
            return peterResponse
        except Exception as e:
            print(e)
            return "An error occured"


