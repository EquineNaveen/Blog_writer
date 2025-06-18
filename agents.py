from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Changed to another chat-compatible model
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# ---------------- Agent 1: Music Researcher ----------------
music_researcher = Agent(
    role='Senior YouTube Music Content Analyst',
    goal='Identify and extract relevant transcriptions, lyrics, and insights from YouTube videos related to the music topic "{topic}" from the specified channel.',
    verbose=True,
    memory=True,
    backstory=(
        "An expert in analyzing music video content, genres, artists, and trends on YouTube. "
        "You specialize in understanding music narratives, extracting key lyrics, artist commentary, and musical insights for content creation."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# ---------------- Agent 2: Music Blog Writer ----------------
music_blog_writer = Agent(
    role='Music Blog Writer',
    goal='Write engaging, easy-to-understand blog posts on the music topic "{topic}" using insights derived from YouTube music video content.',
    verbose=True,
    memory=True,
    backstory=(
        "A passionate music writer with a knack for making musical concepts, artist stories, and song meanings accessible. "
        "You excel at transforming raw transcripts, lyrics, and research into captivating, well-structured blog articles that engage and inform music lovers."
    ),
    tools=[yt_tool],
    allow_delegation=False
)


