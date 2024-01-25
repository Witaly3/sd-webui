import gradio as gr

from ml_sd.ml import image_generation
from config import GRADIO_SHARE


def launch_gradio() -> None:
    prompt = gr.Textbox(label="prompt")
    neg_prompt = gr.Textbox(label="neg_prompt")

    gradio_interface = gr.Interface(
        fn=image_generation,
        inputs=[prompt, neg_prompt],
        outputs="image",
        title="Generate A.I. image using Distill Stable Diffusion 😁",
    )
    gradio_interface.launch(share=GRADIO_SHARE)
