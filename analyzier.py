from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv
from agno.models.groq import Groq
from textwrap import dedent
load_dotenv()

def build_youtube_agent():

        return Agent(
                    name="youtube agent",
                    model=Groq(id="openai/gpt-oss-120b"),
                    tools=[YouTubeTools()],
                    instructions=dedent("""You are a YouTube Agent. You help users research, understand, and create
                content for YouTube. Be accurate, practical, and concise.
        
                ## What you can do
                1. Video analysis: summarize videos, extract key points, timestamps, and
                action items from a video URL or transcript.
                2. Channel and niche research: identify trends, competitor strategies,
                popular topics, and content gaps.
                3. Content creation: generate video ideas, titles, hooks, scripts,
                descriptions, tags, and thumbnail concepts.
                4. SEO and growth: suggest keywords, titles, and posting strategies.
        
                """),
                    add_datetime_to_context=True,
                    markdown=True
                )

 
        

# agent.print_response(
#     "Analyze this video: https://youtu.be/JkaxUblCGz0?si=4jvHC5FvZ_AAbXpp",
#     stream=True,
# )