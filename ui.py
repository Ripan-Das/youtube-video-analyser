import streamlit as st
from analyzier import build_youtube_agent


st.set_page_config(
    page_title="Youtube Video Analyzier",
    layout="centered"
)

st.title("AI youtube video analylyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()


agent=get_agent()


video_url=st.text_input("Enter youtube video link")

butt=st.button("Analyze video")

if video_url and butt:
    with st.spinner("Analyzing video ..."):
        response=agent.run(
            f"analyze this video:{video_url}"
        )

    st.markdown("Analysis report of video:")
    st.markdown(response.content)