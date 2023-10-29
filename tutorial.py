from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
from langchain.llms import OpenAI  # help us interact with OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json


cloud_config = {"secure_connect_bundle": "secure-connect-choose-your-one-adventure.zip"}

with open("choose_your_one_adventure-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]
ASTRA_DB_KEYSPACE = "database"
OPENAI_API_KEY = "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"

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

message_history = CassandraChatMessageHistory(
    # initialize a place in our vector database
    # store the log of the chat history
    session_id="anything",
    session=session,  # connection to our database
    keyspace=ASTRA_DB_KEYSPACE,
    ttl_seconds=3600,  # we will save al of this for maximum 60 minutes
)

message_history.clear()

cass_buff_memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=message_history,
)

# this is customable, you're doing the rules
template = """
You are now the guide of a mystical journey in the Whispering Woods. 
A traveler named Elara seeks the lost Gem of Serenity. 
You must navigate her through challenges, choices, and consequences, 
dynamically adapting the tale based on the traveler's decisions. 
Your goal is to create a branching narrative experience where each choice 
leads to a new path, ultimately determining Elara's fate. 

Here are some rules to follow:
1. Start by asking the player to choose some kind of weapons that will be used later in the game
2. Have a few paths that lead to success
3. Have some paths that lead to death. If the user dies generate a response that explains the death and ends in the text: "The End.", I will search for this text to end the game

Here is the chat history, use this to understand what to say next: {chat_history}
Human: {human_input}
AI:"""

# when I use the llm it's gonna take that memory(cass_buff_memory)
# and it's gonna injected inside of prompt as chat_history
prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)

# rigth from documentation
# wrapping all this stuff that we need to do with a really to use API
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
llm_chain = LLMChain(llm=llm, prompt=prompt, memory=cass_buff_memory)

choice = "start"

while True:
    response = llm_chain.predict(human_input=choice)
    print(response.strip())

    if "The End." in response:
        break

    choice = input("Your reply: ")
