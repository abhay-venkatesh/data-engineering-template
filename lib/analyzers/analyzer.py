from PIL import Image
from pathlib import Path
import torchvision.transforms as transforms
import numpy as np
import os


class Analyzer:
    def __init__(self, config):
        self.config = config

    def verify(self, dataset, max_examples=4):
        split = Path(dataset.root).stem
        examples_path = Path(self.config["stats folder"], split, "examples")
        if not os.path.exists(examples_path):
            os.makedirs(examples_path)

        # Get img, target pairs
        for i, (img, target) in enumerate(dataset):
            img = transforms.ToPILImage()(img)
            img.save(Path(examples_path, "img-" + str(i) + ".jpg"))

            target = target.numpy()
            target = Image.fromarray(np.uint8(target * 100))
            target.save(Path(examples_path, "target-" + str(i) + ".jpg"))

            if i + 1 == max_examples:
                break
