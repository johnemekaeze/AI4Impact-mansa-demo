import json
import os
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))

# Load settings from the .env file next to this script (the key is never printed).
with open(os.path.join(HERE, ".env"), encoding="utf-8-sig") as env_file:
    for line in env_file:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip().strip('"').strip("'")

request = urllib.request.Request(
    os.environ["MANSA_API_BASE_URL"].rstrip("/") + "/v1/tts",
    data=json.dumps({
        "text": "Ndewo nụ! Tupu ị zipụ ego site na ekwentị gị, lelee aha onye ị na-ezitere ya nke ọma. Ekwela ka onye ọ bụla mara nọmba nzuzo gị. Ọ bụrụ na onye ọ bụla akpọọ gị na-arịọ maka ya, kwụsị oku ahụ ozugbo.",
        "language": "igbo",
        "voice": "igbo_female",
    }).encode(),
    headers={
        "Authorization": "Bearer " + os.environ["MANSA_API_KEY"],
        "Content-Type": "application/json",
    },
)

start = time.time()
try:
    with urllib.request.urlopen(request, timeout=900) as response:
        audio = response.read()
except urllib.error.HTTPError as error:
    print("Request failed:", error.code, error.read().decode(errors="replace")[:500])
    raise SystemExit(1)

print(f"Response received in {time.time() - start:.1f} s")
if audio[:4] != b"RIFF":  # the reply body should be the WAV itself
    print("Response was not WAV audio:", audio[:500].decode(errors="replace"))
    raise SystemExit(1)

with open(os.path.join(HERE, "speech_female.wav"), "wb") as output:
    output.write(audio)

print("Saved speech_female.wav")
