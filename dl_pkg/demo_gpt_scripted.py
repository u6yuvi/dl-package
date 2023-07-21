import gradio as gr
import torch
import tiktoken

# model
loaded_model = torch.jit.load("models/hp_gpt_scripted.pt", map_location="cpu")
loaded_model.eval()

# tokenizer
cl100k_base = tiktoken.get_encoding("cl100k_base")

# In production, load the arguments directly instead of accessing private attributes
# See openai_public.py for examples of arguments for specific encodings
tokenizer = tiktoken.Encoding(
    # If you're changing the set of special tokens, make sure to use a different name
    # It should be clear from the name what behaviour to expect.
    name="cl100k_im",
    pat_str=cl100k_base._pat_str,
    mergeable_ranks=cl100k_base._mergeable_ranks,
    special_tokens={
        **cl100k_base._special_tokens,
        "<|im_start|>": 100264,
        "<|im_end|>": 100265,
    }
)

def text_completion(text: str) -> str:
    input_enc = torch.tensor(tokenizer.encode(text))
    with torch.no_grad():
        out_gen = loaded_model.model.generate(input_enc.unsqueeze(0).long(), max_new_tokens=32)
    decoded = tokenizer.decode(out_gen[0].cpu().numpy().tolist())
    return decoded

demo = gr.Interface(
    fn=text_completion,
    inputs=gr.Textbox(lines=5, placeholder="Enter text here..."),
    outputs="text",
)

demo.launch(share=True,server_name = "0.0.0.0", server_port= 80)