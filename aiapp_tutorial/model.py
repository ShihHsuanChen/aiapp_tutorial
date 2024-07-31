from typing import List, Tuple

import timm
import torch
from PIL import Image
from imagenet_stubs.imagenet_2012_labels import label_to_name


class InferModel:
    def __init__(self,
            model_name: str,
            **kwargs,
            ):
        # load model by timm
        model = timm.create_model(model_name, pretrained=True)
        self.model = model.eval()

        # get model specific transforms (normalization, resize)
        data_config = timm.data.resolve_model_data_config(model)
        self.transforms = timm.data.create_transform(**data_config, is_training=False)

    # TODO: make this batch
    @torch.no_grad
    def inference(self,
            image: Image.Image,
            topk: int = 5,
            ) -> List[Tuple[str, float]]:
        """
        Do single Inference

        Arguments:
            - images: (list) List of Pillow image objects
            - top_k: (int) get top-k highest probability labels
        Returns: (list) List of (class_name, probability) tuple
        """
        output = self.model(self.transforms(image).unsqueeze(0))  # unsqueeze single image into batch of 1

        topk_probabilities, topk_class_indices = torch.topk(output.softmax(dim=1), k=topk)
        # batch_size = 1
        topk_class_indices = topk_class_indices.cpu().numpy().tolist()[0]
        topk_probabilities = topk_probabilities.cpu().numpy().tolist()[0]
        result = []
        for idx, prob in zip(topk_class_indices, topk_probabilities):
            result.append((label_to_name(idx), prob))
        return result


def load_model(model_name: str, **kwargs):
    print(f'load model {model_name}')
    return InferModel(model_name, **kwargs)
