# codePortfolio
# Project name: Youtube video summary creator with Gen AI Llama 2
>Readme for CS50 - Introduction to python final project.

## Concept
- Enter a youtube video url and get its summary.<br/>
- This entire project is made with open source components.<br/>
- After youtube video url is entered in python, we first get its transscript with youtube-transcript-api. Alternatively youtube API can be used but it has a daily limit.<br/>
- After that we use requests to get the youtube video web page. This webpage is converted to text format and passed to beautiful soup which helps to find the video title.<br/>
- After getting the video title and transcript, they are passed as a prompt to llama model. Content window size is set to 10000 after testing.<br/>
- Llama 2 7B model is chosen for this project. This decision has been made due to following CPU constraints as it is run locally.<br/>
- Another way to run llama 2 is on replicate using their server and GPUs but after ~75 requests it will start charging for each request, so it was decided to run Lama Gen AI locally.<br/>
- We are using quantized LLMs so that they can be run locally on laptop CPU free of cost.<br/>
- The model has to be run twice or more on a same youtube video to get the best summary.<br/>

## Limits:
- Based on context window size and CPU capacity of the laptop we can get summary of max 45 min video.<br/>
- Only english videos can be summarised.<br/>

## youtube video
https://www.youtube.com/watch?v=WwNOVcBU1Jg
