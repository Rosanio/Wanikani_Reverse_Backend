# WaniKani Reverse
The Japanese learning website [WaniKani](https://www.wanikani.com/) uses flashcards, mnemonics and the spaced repetition system to help users learn to recognize Japanese characters (Kanji) and vocabulary. However, WaniKani only displays Japanese text to the user and accepts English input. When studying a new language, it's equally important (if not more so) to be able to translate from English to Japanese. This project uses the API provided by WaniKani to display the English text of their vocabulary flashcards, and prompts the user to input the corresponding word in Japanese.

## Prerequisites
To run this app locally, you will need to have [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine. Note that you will also need to enable CORS enabled on your browser. If using Chrome, you can find an extension to do this [here](https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi?hl=en). Please note that this extension will break some popular websites, and you should disable it when you are done using WaniKani Reverse.

## Installation
First, you will need to clone this repository:

```git clone https://github.com/Rosanio/Wanikani_Reverse_Backend```

After that, navigate to the root level directory and run ```docker-compose up```. You should now be able to access the page at http://localhost:3000. 