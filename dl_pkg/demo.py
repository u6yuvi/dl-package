from typing import List, Tuple

import torch
import hydra
import gradio as gr
import requests
from omegaconf import DictConfig
# from PIL import Image
from torchvision import transforms
from torch.nn import functional as F

from dl_pkg import utils

log = utils.get_pylogger(__name__)

def demo(cfg: DictConfig) -> Tuple[dict, dict]:
    """Demo function.
    Args:
        cfg (DictConfig): Configuration composed by Hydra.

    Returns:
        Tuple[dict, dict]: Dict with metrics and dict with all instantiated objects.
    """

    assert cfg.demo_ckpt_path

    log.info("Running Demo")

    log.info(f"Instantiating scripted model <{cfg.demo_ckpt_path}>")
    model = torch.jit.load(cfg.demo_ckpt_path)

    log.info(f"Loaded Model: {model}")


    def recognize_cifar_image(image,cfg):
        transform = transforms.Compose([transforms.ToTensor(),
            #transforms.Resize((cfg.model.net.img_size, cfg.model.net.img_size)),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5),)])

        image = transform(image)

        response = requests.get("https://gist.githubusercontent.com/u6yuvi/2b1af8e3d92ee21b14f0ed47352b1c45/raw/3e5a45a641f5db4f5ccd93097249349ceeaa19d5/cifar10labels.txt")
        labels = response.text.split("\n")
        image = torch.tensor(image, dtype=torch.float).unsqueeze(0)
        model.eval()
        with torch.no_grad():   
            preds = model(image)
        prob = F.softmax(preds, dim=1)
        #top_p, top_class = prob.topk(5, dim = 1)
        prob = prob[0].tolist()
        return {str(label): prob[idx] for idx, label in enumerate(labels)}


    demo = gr.Interface(fn=recognize_cifar_image,
             inputs=gr.Image(type="pil",shape=(cfg.model.net.img_size, cfg.model.net.img_size)),
             outputs=gr.Label(num_top_classes=10),
             ).launch()

    demo.launch(server_name = "0.0.0.0", server_port= 8080)

@hydra.main(
    version_base="1.2", config_path="../configs", config_name="demo_traced.yaml"
)
def main(cfg: DictConfig) -> None:
    demo(cfg)

if __name__ == "__main__":
    main()