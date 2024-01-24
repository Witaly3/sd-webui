import torch

from diffusers import StableDiffusionPipeline
from diffusers.utils import load_image


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from PIL import Image


model_id_or_path = "runwayml/stable-diffusion-v1-5"

# lora_model_id_or_path = "patrickvonplaten/lora_dreambooth_dog_example"


ip_adapter_image = load_image(
    "https://user-images.githubusercontent.com/24734142/266492875-2d50d223-8475-44f0-a7c6-08b51cb53572.png"
)


pipe = StableDiffusionPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float16)
pipe.safety_checker = None
pipe.requires_safety_checker = False

pipe.to("cuda")

pipe.load_ip_adapter("h94/IP-Adapter", subfolder="models", weight_name="ip-adapter_sd15.bin")

# pipe.load_lora_weights(lora_model_id_or_path)

# pipe.enable_xformers_memory_efficient_attention()

generator = torch.Generator(device="cuda").manual_seed(0)


def image_generation(prompt: str, n_prompt: str) -> "Image":
    image = pipe(
        prompt=prompt, negative_prompt=n_prompt, ip_adapter_image=ip_adapter_image, generator=generator,
    ).images[0]

    return image
