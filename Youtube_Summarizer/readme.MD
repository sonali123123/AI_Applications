# Video Captioning & Summarization Application

This repository contains a Streamlit web application that automatically generates captions and summaries for educational videos. By combining video-to-audio conversion, transcription using OpenAI's Whisper model, and advanced text processing with LangChain, the app helps educators and learners quickly extract key information from video content.

---

## Features

- **Video to Audio Conversion:** Converts uploaded video files (mp4, mov, avi) to audio (mp3) using pydub.
- **Transcription:** Uses OpenAI's Whisper model to transcribe the audio into text.
- **Text Summarization:** Summarizes the transcribed text with a map-reduce approach via LangChain.
- **Caption Generation:** Generates a concise caption (in no more than 5 words) for the video content.
- **Interactive UI:** Built with Streamlit, offering a user-friendly interface for video upload, processing, and result display.

---

## Project Structure

- **`app.py`**  
  The main Streamlit application that handles file uploads, orchestrates video processing, and displays the generated summary and caption.

- **`audio_to_txt.py`**  
  Contains functions to:
  - Extract audio from a video file and convert it to an MP3.
  - Transcribe the audio into text using the Whisper model.

- **`caption.py`**  
  Contains the logic for generating a short caption for the transcribed speech using LangChain with ChatOllama.

- **`summary.py`**  
  Contains the logic for summarizing the transcribed text using LangChain with ChatOllama.

---

## Installation

### Prerequisites

- Python 3.7 or higher.
- [FFmpeg](https://ffmpeg.org/) (required by pydub for audio processing).

## Setup

1. Clone the Repo:

https://github.com/sonali123123/AI_Applications.git
cd Youtube_Summarizer


### Install Dependencies

Install the necessary Python packages using pip:

```bash
pip install -R REQUIREMENTS.TXT
