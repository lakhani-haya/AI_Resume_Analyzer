# AI Resume Analyzer using Hugging Face Transformers

This project uses Python and Hugging Face’s `transformers` library to analyze resume text and provide automated feedback. It demonstrates how natural language processing (NLP) can be used to support job-seekers by improving resume clarity, conciseness, and relevance — all within a minimal web-based interface.

---

## Project Objectives

- Analyze resumes using pretrained NLP models
- Provide category-specific feedback: Clarity, Conciseness, Relevance
- Build a lightweight, real-time resume analysis app using Streamlit
- Run entirely on local machine with no paid API dependencies

---

## Tools & Technologies Used

| Tool | Purpose |
|------|---------|
| **Python (Streamlit, Transformers, Torch)** | Application logic and NLP inference |
| **Hugging Face Transformers** | Sentiment classification model (`distilbert-base-uncased-finetuned-sst-2-english`) |
| **Streamlit** | Web app framework for interactive UI |
| **VS Code** | Development environment |
| **GitHub** | Project versioning and sharing |

---

## Resume Analysis Approach

1. Collected resume text via a browser-based text input
2. Split text into sections (opening, ending, full body)
3. Passed each section through a sentiment classification model using Hugging Face’s `pipeline`
4. Generated human-readable feedback for each category
5. Rendered output immediately in the browser using Streamlit

---

## What I Learned

- How to integrate Hugging Face models into real-time applications
- How to build and test NLP tools locally with no external API access
- How to structure resume text analysis using basic sentiment classification
- How to quickly prototype useful interfaces using Streamlit

---

## Sample Application UI

The Streamlit app takes pasted resume text and produces three pieces of feedback based on different segments of the document. All model inference runs locally using Hugging Face’s default sentiment pipeline.

The app includes:
- Resume input box
- One-click analysis trigger
- Model-generated feedback for:
  - Clarity (based on the intro)
  - Conciseness (based on the ending)
  - Relevance (based on full content)

### Key Takeaways:
- Using even basic sentiment models, you can extract valuable cues about tone and writing quality
- Streamlit allows rapid iteration and zero-setup sharing
- The structure allows easy extension to compare resumes to job descriptions or score against industry benchmarks

---

## Connect with Me

If you’d like to collaborate or view more projects, check out:
- [My Portfolio](https://lakhani-haya.github.io)
- [GitHub Profile](https://github.com/lakhani-haya)
- [Email](mailto:hy.lakhanii@gmail.com)

