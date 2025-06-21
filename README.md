# AI Resume Analyzer

AI Resume Analyzer
description: >
  A lightweight NLP-powered app that analyzes resume text and provides actionable feedback on clarity, conciseness, and relevance. 
  Built with Streamlit and Hugging Face Transformers.

tags:
  - NLP
  - Streamlit
  - Hugging Face
  - Resume Analysis
  - Transformers
  - Python

tech_stack:
  - category: Programming Language
    tools: [Python]
  - category: Libraries
    tools: [Streamlit, Transformers, Torch]
  - category: NLP Model
    tools: [distilbert-base-uncased-finetuned-sst-2-english]
  - category: IDE
    tools: [VS Code]
  - category: Runtime
    tools: [Localhost via Streamlit]
  - category: Optional Deployment
    tools: [Streamlit Community Cloud]

features:
  - Paste your resume into a simple browser interface
  - Get AI-generated feedback on clarity, conciseness, and relevance
  - Runs locally with no paid API required
  - Easy to modify or extend to compare job descriptions

install:
  - pip install -r requirements.txt
  - streamlit run app.py

requirements:
  - streamlit
  - transformers
  - torch

how_it_works: >
  The app uses Hugging Face's sentiment-analysis pipeline to classify the tone of different parts of the resume.
  The beginning, ending, and full text are each evaluated separately to provide category-specific feedback.

future_improvements:
  - PDF upload and parsing
  - Job description matching
  - Visual scoring or comparison dashboards
  - Deployment to Streamlit Cloud or other platforms

author:
  name: Your Name
  links:
    - label: LinkedIn
      url: https://linkedin.com/in/your-profile
    - label: Portfolio
      url: https://yourportfolio.com

license: MIT
