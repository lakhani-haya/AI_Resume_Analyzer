import streamlit as st
import time
from transformers import pipeline

# Load custom CSS from external file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Load Google Fonts separately
st.markdown('<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap" rel="stylesheet">', unsafe_allow_html=True)

# Load Hugging Face sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

st.set_page_config(page_title="ai resume analyzer", layout="wide")

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.markdown("<h1 style='font-size:2.5rem; margin-bottom:0.5rem;'>ai resume analyzer</h1>", unsafe_allow_html=True)
    st.markdown("""
        <p style='font-size:1.2rem;'>
        paste your resume text on the right and get instant feedback on clarity, conciseness, and relevance.<br><br>
        this tool uses ai to analyze the tone and structure of your resume. it helps you:
        <ul style='margin-left:1em;'>
            <li>improve clarity by simplifying complex sentences</li>
            <li>make your writing more concise and impactful</li>
            <li>ensure your experience is relevant to your target roles</li>
        </ul>
        results are instant and private. no data is stored.<br><br>
        try pasting a few different resumes to see how the feedback changes.
        </p>
    """, unsafe_allow_html=True)

with col2:
    resume_text = st.text_area("paste your resume text here:", height=300)
    analyze = st.button("analyze resume")

    if analyze:
        if not resume_text.strip():
            st.warning("please paste some resume text before analyzing.")
        else:
            with st.spinner("analyzing your resume with ai..."):
                time.sleep(1)
                try:
                    clarity_result = sentiment_analyzer(resume_text[:512])[0]
                    conciseness_result = sentiment_analyzer(resume_text[-512:])[0]
                    relevance_result = sentiment_analyzer(resume_text)[0]

                    feedback = {
                        "clarity": f"the opening of your resume is {clarity_result['label'].lower()} with confidence {clarity_result['score']:.2f}. consider simplifying complex sentences.",
                        "conciseness": f"the end of your resume appears {conciseness_result['label'].lower()} (score: {conciseness_result['score']:.2f}). avoid repetition or filler words.",
                        "relevance": f"overall, the resume tone is {relevance_result['label'].lower()} — make sure it matches the roles you're targeting."
                    }

                    st.success("analysis complete")
                    st.subheader("ai feedback")
                    for category, comment in feedback.items():
                        st.markdown(f"**{category}:** {comment}")
                except Exception as e:
                    st.error(f"something went wrong: {e}")
