import json
import urllib.request

req_local = urllib.request.Request("http://localhost:8000/generate", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req_local) as resp:
    gen_data = json.loads(resp.read().decode())

print("Generated locally:", gen_data)

payload = {
    "team": "8",
    "by": "Sadeem AlBoqami",
    "model": gen_data["model"],
    "image": "ghcr.io/ranaalshaikh/aidc-team08-server:latest",
    "tokens_per_sec": gen_data["tokens_per_sec"],
    "sample": gen_data["sample"]
}

data_bytes = json.dumps(payload).encode("utf-8")
req_board = urllib.request.Request(
    "https://aidc.nadir.sh/model",
    data=data_bytes,
    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
    method="POST"
)

with urllib.request.urlopen(req_board) as resp:
    print("The Board Response:", resp.status, resp.read().decode())
