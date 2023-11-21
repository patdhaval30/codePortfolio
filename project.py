from youtube_transcript_api import YouTubeTranscriptApi
import requests
import sys
from bs4 import BeautifulSoup
from llama_cpp import Llama


def main():
    url = input("Enter youtube video url to be summarized: ").strip()
    transcript = get_youtube_video_transcripts(url)
    title = get_youtube_video_title(url)
    connect_to_llama(transcript, title)


def get_youtube_video_transcripts(url):
    try:
        id = url.split(sep="=")[1]
    except:
        sys.exit("Enter a correct youtibe URL")
    completeText = ""
    transcript = YouTubeTranscriptApi.get_transcript(id)
    for text in transcript:
        completeText = completeText + text["text"].strip() + " "
    return completeText


def get_youtube_video_title(url):
    try:
        response = requests.get(url)
    except:
        sys.exit("Enter a correct youtibe URL")
    soup = BeautifulSoup(response.text, "lxml")
    title = soup.find("title").text.strip()
    return title[:-9]


def connect_to_llama(transcript, title):
    print(title)
    print(transcript)
    prompt = f"Title of the document is {title}. Document contains following text: {transcript}. What are the important points from the document?"
    try:
        LLM = Llama(model_path="./llama-2-7b.Q8_0.gguf", n_ctx=7000)

        # set max_tokens to 0 to remove the response size limit
        output = LLM(prompt, max_tokens=500)
        print(output["choices"][0]["text"])
        return True
    except:
        return False


if __name__ == "__main__":
    main()
