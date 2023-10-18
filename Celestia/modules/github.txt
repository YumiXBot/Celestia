from Celestia import Celestia
from pyrogram import filters
from github import Github
import openai


GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
REPO_OWNER = 'YOUR_GITHUB_USERNAME'
REPO_NAME = 'YOUR_GITHUB_REPOSITORY'





github = Github(GITHUB_TOKEN)
repo = github.get_repo(f'{REPO_OWNER}/{REPO_NAME}')


openai.api_key = OPENAI_API_KEY



CONVERSATION_STATE = {}


@Celestia.on_message(filters.command("createcode"))
def create_code(client, message):
    message.reply_text("Please describe the code you want to create, and I'll generate it for you.")
    CONVERSATION_STATE[message.chat.id] = {"state": "generate_code"}

def generate_code(client, message):
    chat_id = message.chat.id
    description = message.text

    try:
        # Use ChatGPT to generate code based on the description
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate code: {description}",
            max_tokens=200  # Adjust as needed
        )

        generated_code = response.choices[0].text

        # Create a new file in a folder (e.g., 'code_folder') with a random name
        folder_name = 'code_folder'  # You can change this
        file_name = f'code_{chat_id}.py'  # Generate a unique file name
        content = generated_code

        repo.create_file(f'{folder_name}/{file_name}', "Created by Telegram Bot", content)
        response_text = (
            f"Code file created in '{folder_name}' with name '{file_name}'.\n"
            "You can find your code on GitHub."
        )
    except Exception as e:
        response_text = f"An error occurred: {str(e)}"

    # Send a response
    message.reply_text(response_text)
    # Remove the conversation state
    if chat_id in CONVERSATION_STATE:
        del CONVERSATION_STATE[chat_id]






