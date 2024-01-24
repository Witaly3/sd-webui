import gc
import torch

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from io import BytesIO

from ml_sd.ml import image_generation


router = APIRouter(prefix="/image", tags=["image"])


@router.post("/generate")
def generate_image(prompt: str, n_prompt: str) -> StreamingResponse:
    gen_image = image_generation(prompt=prompt, n_prompt=n_prompt)

    gc.collect()
    torch.cuda.empty_cache()

    memory_stream = BytesIO()
    gen_image.save(memory_stream, format="PNG")
    memory_stream.seek(0)

    return StreamingResponse(memory_stream, media_type="image/png")
