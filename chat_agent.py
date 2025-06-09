import chainlit as cl
from index_wikipages import create_index
from utils import get_apikey

index = None
agent = None

@cl.on_chat_start
async def on_chat_start():
    global index
    # Settings
    settings = await cl.ChatSettings(
        [
            Select(
                id = "Model", 
                label="OpenAI - Model", 
                values = ["gpt-3.5-turbo"], 
                initial_index=0,
            ),
            TextInput(
                id = "WikiPageRequest",
                label = "Request Wikipage"
            )
            ,
        ]
    ).send()


def wikisearch_engine(index):
    pass


def create_react_agent(MODEL):
    pass


@cl.on_settings_update
async def setup_agent(settings):
    pass


@cl.on_message
async def main(message: str):
    pass
