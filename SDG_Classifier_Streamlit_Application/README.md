# Sustainable Development Goals (SDG) Document Classifier

This repository contains a Streamlit-based web application for classifying documents according to the United Nations Sustainable Development Goals (SDGs). The app leverages a fine-tuned BERT model (checkpoint: `sadickam/sdg-classification-bert`) from Hugging Face to predict the most relevant SDG based on the content of uploaded PDF or DOCX files.

---

## Features

- **File Upload:** Upload up to 10 documents (PDF or DOCX) at a time.
- **Text Extraction:** Automatically extract text from PDF and DOCX files.
- **Preprocessing:** Clean and tokenize text using NLTK and regex.
- **Model Inference:** Utilize a pre-trained BERT model to predict SDGs.
- **Visualization:** Display prediction confidence for each SDG using an interactive Plotly bar chart.
- **Download Results:** Export the prediction outcomes as a CSV file.

---

## Installation

### Prerequisites

Ensure you have Python 3.7 or higher installed. Then, install the required packages using pip:

```bash
pip install -r requirements.txt
