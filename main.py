#for streamlit
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
#for streamlit

import streamlit as st
from crewai import Agent, Task, Crew, Process, LLM
import os
import warnings
from crewai_tools import SerperDevTool
warnings.filterwarnings("ignore")


os.environ['SERPER_API_KEY'] = st.secrets['SERPER_API_KEY']       
os.environ['SAMBANOVA_API_KEY'] = st.secrets['SAMBANOVA_API_KEY'] 

tool = SerperDevTool(
    n_results=1,
)

#Agents
research_agent = Agent(
    llm=LLM(
        model="sambanova/Meta-Llama-3.1-70B-Instruct",
        temperature=0.5 
    ),
    role="Research Analyst",
    goal="Extract detailed, accurate, and relevant information about a company's topic from credible sources. Company name is {name} and the topic is {topic}.",
    backstory=(
        """You are a professional research analyst specializing in company and industry analysis. 
        Your task is to use the Google Search API to extract precise and updated information about a 
        given company and topic. You focus on credibility, factual accuracy, and up-to-date insights."""
    ),
    verbose=True,
    tools=[tool],
)


blog_writer = Agent(
    llm=LLM(
        model="sambanova/Meta-Llama-3.1-70B-Instruct",
        temperature=0.7
    ),
    role="Professional Business Blogger",
    goal="Write engaging, SEO-optimized blog posts that reflect the company's voice and industry insights. Write a blog in {tone} tone for {social_media}.",
    backstory=(
        """You are an expert content writer skilled in crafting well-researched, SEO-friendly blogs that align 
        with a company’s brand voice. You use research data to structure compelling articles that engage 
        audiences while maintaining factual accuracy and industry relevance."""
    ),
    verbose=True,
    tools=[tool],
)


#Tasks
research_task = Task(
    description="Gather comprehensive and up-to-date information about the given company and topic.",
    agent=research_agent,
    expected_output="A structured research report summarizing the company’s key insights, recent developments, and industry positioning. "
)

blog_task = Task(
    description="Write a well-structured, engaging, and SEO-optimized blog post based on extracted research data. Add relevant emojis and links whenever needed.",
    expected_output="A professionally written, SEO-optimized blog post that reflects the company’s voice and expertise on the topic.",
    agent=blog_writer,
)

#Crew
crew = Crew(
    agents=[research_agent, blog_writer],
    tasks=[research_task, blog_task],
    process=Process.sequential, 
)

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Blog Writing AI",
        page_icon="✍️",
        layout="centered",
    )

    # Custom CSS for a clean UI
    st.markdown(
        """
        <style>
        .stTextInput>div>div>input {
            border-radius: 10px;
            padding: 10px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stMarkdown {
            font-size: 16px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and description
    st.title("✍️ Blog Writing AI")
    st.markdown("Generate a professional blog post tailored to your company's tone and topic.")

    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("Company Name/Link", placeholder="Enter your company name or link")
    with col2:
        topic = st.text_input("Topic", placeholder="Enter the blog topic")

    col3, col4 = st.columns(2)
    with col3:
        tone = st.text_input("Tone", placeholder="Enter the desired tone (e.g., professional, friendly)")
    with col4:
        social_media = st.text_input("Social Media", placeholder="Enter social media platform (e.g., LinkedIn, Twitter)")

    # Generate button
    if st.button("Generate Blog"):
        if not company_name or not topic or not tone or not social_media:
            st.warning("Please fill in all the fields!")
        else:
            inputs = {"name": company_name, "topic": topic, "tone": tone, "social_media": social_media}
            res = crew.kickoff(inputs)
            #print(res.raw)
            #st.write(res.raw)
            # Display the generated blog
            st.subheader("Generated Blog")
            st.markdown(res.raw)

            # Download button for the blog
            st.download_button(
                label="Download Blog",
                data=res.raw,
                file_name=f"{company_name}_blog.md",
                mime="text/markdown",
            )

if __name__ == '__main__':
    main()
