from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="adv-11/gemma-3-1b-it-Q4_K_M-GGUF",
	filename="gemma-3-1b-it-q4_k_m.gguf",
)

llm.create_chat_completion(
	messages = [
		{
			"role": "user",
			"content": "What is the capital of France?"
		}
	]
)