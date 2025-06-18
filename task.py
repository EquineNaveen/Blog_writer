from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# ---------------- Research Task ----------------
music_research_task = Task(
  description=(
    "Research the music topic '{topic}' by identifying and analyzing relevant music videos from the specified YouTube channel. "
    "Extract meaningful content, lyrics, artist commentary, and key musical insights from the most suitable video."
  ),
  expected_output=(
    "A well-structured, three-paragraph summary report containing the main musical takeaways, context, and highlights "
    "from the selected YouTube music video on the topic '{topic}'."
  ),
  tools=[yt_tool],
  agent=blog_researcher,
)

# ---------------- Music Blog Writing Task ----------------
music_write_task = Task(
  description=(
    "Using the research and extracted musical insights from YouTube, create an engaging and informative music blog article "
    "on the topic '{topic}'. Focus on clarity, musical storytelling, and artist or song context."
  ),
  expected_output=(
    "A complete music blog post based on the video content around '{topic}', with a compelling introduction, "
    "clear explanations of musical elements, and a well-structured narrative formatted for publication."
  ),
  tools=[yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'
)
