from crewai import Crew,Process
from agents import music_researcher,music_blog_writer
from task import music_research_task,music_write_task


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[music_researcher, music_blog_writer],
  tasks=[music_research_task, music_write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'Sabrina carpenter song taste'})
print(result)