import openai
import streamlit as st

# Set OpenAI API key
st.sidebar.subheader("OpenAI API Key")
openai.api_key = st.sidebar.text_input("API Key", type="password")

# Define GPT-3 parameters
model_engine = "davinci"
temperature = 0.7
max_tokens = 256

# Define prompt for GPT-3
prompt = "Create a D&D character with the following characteristics:"

# Define attributes for D&D character
attributes = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma"
]

# Define point buy cost for each attribute score
point_buy_cost = {
    8: 0,
    9: 1,
    10: 2,
    11: 3,
    12: 4,
    13: 5,
    14: 7,
    15: 9
}

# Define character classes for D&D
classes = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard"
]

# Define character backgrounds for D&D
backgrounds = [
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Entertainer",
    "Folk Hero",
    "Guild Artisan",
    "Hermit",
    "Noble",
    "Outlander",
    "Sage",
    "Sailor",
    "Soldier",
    "Urchin"
]

# Define function to calculate remaining point buy points
def calculate_remaining_points(attribute_scores):
    remaining_points = 27
    for score in attribute_scores.values():
        remaining_points -= point_buy_cost[score]
    return remaining_points

# Define function to create a D&D character
def create_character(prompt, attributes, classes, backgrounds):
    # Get attribute scores from GPT-3
    attribute_scores = {}
    for attribute in attributes:
        attribute_prompt = f"What is the {attribute} score?"
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt + attribute_prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        score = response.choices[0].text.strip()
        attribute_scores[attribute] = int(score)

    # Calculate remaining point buy points
    remaining_points = calculate_remaining_points(attribute_scores)

    # Get character class from GPT-3
    class_prompt = "What is the character's class?"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + class_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        presence_penalty=0.5,
        frequency_penalty=0.5,
        stop=classes
    )
    character_class = response.choices[0].text.strip()

    # Get character background from GPT-3
    background_prompt = "What is the character's background?"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt + background_prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        presence_penalty=0.5,
        frequency_penalty=0.5,
        stop=backgrounds
    )
    background = response.choices[0].text.strip()

    # Generate character backstory from GPT-3
    backstory_prompt = "Write a backstory for the character"
