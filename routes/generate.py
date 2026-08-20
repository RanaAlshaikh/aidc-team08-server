import time
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "HuggingFaceTB/SmolLM2-135M-Instruct"
PATH = "/generate"

tok = AutoTokenizer.from_pretrained(MODEL, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(MODEL, local_files_only=True)

def handle():
    messages = [
        {"role": "user", "content": "In one sentence, what is a data centre for?"}
    ]
    ids = tok.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")
    t0 = time.perf_counter()
    out = model.generate(ids, max_new_tokens=40, do_sample=False)
    dt = time.perf_counter() - t0
    input_len = ids.shape[-1]
    n = out.shape[-1] - input_len
    return {
        "model": MODEL,
        "sample": tok.decode(out[0][input_len:], skip_special_tokens=True).strip(),
        "seconds": round(dt, 2),
        "tokens_per_sec": round(n / dt, 1)
    }
