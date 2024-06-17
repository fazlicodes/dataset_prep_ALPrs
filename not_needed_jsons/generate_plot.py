# Found existing installation: urllib3 2.1.0
#     Uninstalling urllib3-2.1.0:
#       Successfully uninstalled urllib3-2.1.0

import fiftyone as fo
import fiftyone.brain as fob
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("cifar10", split="test")
session = fo.launch_app(dataset)