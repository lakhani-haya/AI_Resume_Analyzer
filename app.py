import streamlit as st
import time

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("🧠 AI Resume Analyzer")
st.write("Paste your resume text below and get instant feedback on clarity, conciseness, and relevance.")

resume_text = st.text_area("✍️ Paste your resume text here:", height=300)

if st.button("🔍 Analyze Resume"):
    if not resume_text.strip():
        st.warning("Please paste some resume text before analyzing.")
    else:
        with st.spinner("Analyzing your resume with AI..."):
            time.sleep(2)  # simulate delay

            # MOCKED FEEDBACK – replace this with Hugging Face call later
            feedback = {
                "Clarity": "Your resume is generally clear. Consider breaking long paragraphs into bullet points.",
                "Conciseness": "The resume is concise, but you could remove older, less relevant roles to tighten it.",
                "Relevance": "Your experience aligns well with marketing roles. Highlight more metrics to show impact."
            }

        st.success("✅ Analysis Complete")
        st.subheader("📋 Feedback")
        for category, comment in feedback.items():
            st.markdown(f"**{category}:** {comment}")

# Ensure the script runs only with Streamlit, not on import
if __name__ == "__main__":
    pass  # Streamlit runs the script directly, so nothing needed here
