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

# ---------------- Agent 1: Blog Researcher ----------------
blog_researcher = Agent(
    role='Senior YouTube Content Analyst',
    goal='Identify and extract relevant transcriptions from YouTube videos related to the topic "{topic}" from the specified channel.',
    verbose=True,
    memory=True,
    backstory=(
        "An expert in analyzing video content on Artificial Intelligence, Data Science, Machine Learning, and Generative AI. "
        "You specialize in understanding video narratives and extracting key insights and transcripts for content creation."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# ---------------- Agent 2: Blog Writer ----------------
blog_writer = Agent(
    role='Technical Blog Writer',
    goal='Write compelling, easy-to-understand blog posts on the topic "{topic}" using insights derived from YouTube video content.',
    verbose=True,
    memory=True,
    backstory=(
        "A seasoned technical writer with a passion for making complex technologies accessible. "
        "You excel at transforming raw transcripts and research into captivating, well-structured blog articles that engage and educate readers."
    ),
    tools=[yt_tool],
    allow_delegation=False
)


