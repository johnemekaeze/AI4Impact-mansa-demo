# Mansa Igbo Text-to-Speech Demo

Two small Python scripts that turn Igbo text into spoken audio using the [Mansa API](https://mymansa.ai). One uses a male voice, the other a female voice. Each saves a `.wav` file you can play.

The sample text is a short mobile-money safety message:

> Ndewo nụ! Tupu ị zipụ ego site na ekwentị gị, lelee aha onye ị na-ezitere ya nke ọma. Ekwela ka onye ọ bụla mara nọmba nzuzo gị. Ọ bụrụ na onye ọ bụla akpọọ gị na-arịọ maka ya, kwụsị oku ahụ ozugbo.

## Requirements

- Python 3.8 or newer. Nothing else to install; the scripts use only Python's built-in libraries.
- A Mansa API key.

## Setup

1. Clone this repository and open the folder.
2. Copy the example settings file:

   ```bash
   cp .env.example .env        # macOS / Linux
   copy .env.example .env      # Windows
   ```

3. Open `.env` and fill in your values:

   ```
   MANSA_API_BASE_URL=https://api.mymansa.ai
   MANSA_API_KEY=your-api-key-here
   ```

   Don't use quotes, and don't put a slash at the end of the URL. Values in `.env` override any settings with the same names in your terminal.

## Usage

```bash
python mansa_tts_male.py      # saves speech_male.wav
python mansa_tts_female.py    # saves speech_female.wav
```

Each script prints how long the request took and saves the audio next to the script. A request usually takes 20–30 seconds.

To make the scripts say something else, change the `"text"` value in each script.

## Troubleshooting

| Message | What it means |
| --- | --- |
| `FileNotFoundError: ... .env` | You haven't created `.env` yet. See Setup step 2. |
| `KeyError: 'MANSA_API_BASE_URL'` or `'MANSA_API_KEY'` | That line is missing from `.env`. |
| `getaddrinfo failed` | The URL is wrong or still a placeholder, or your internet connection dropped. |
| `Request failed: 401` | The API key is wrong, incomplete or expired. |
| `Response was not WAV audio` | The server replied with a message instead of audio. The message is printed below. |

## Security

`.env` holds your API key and is listed in `.gitignore`, so Git won't upload it. Never commit it or share it. Only `.env.example`, which has placeholder values, belongs in the repository.
