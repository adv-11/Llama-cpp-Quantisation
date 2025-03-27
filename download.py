

from huggingface_hub import snapshot_download
model_id="meta-llama/Llama-3.2-3B-Instruct"

snapshot_download(repo_id=model_id, local_dir="adv-hf",
                  local_dir_use_symlinks=False, revision="main")

