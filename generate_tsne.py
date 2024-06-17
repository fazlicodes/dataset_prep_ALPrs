import torch
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from PIL import Image
import clip
import json
import os
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader

# Load the pre-trained CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

class CustomDataset(Dataset):
    def __init__(self, data, root_dir, transform=None):
        self.data = data
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name, label, _ = self.data[idx]
        img_path = os.path.join(self.root_dir, img_name)
        image = Image.open(img_path).convert('RGB')
        if self.transform:
            image = self.transform(image)
        return image, label, img_path  # Return image path along with image and label

# Define transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load JSON file
with open('/l/users/sanoojan.baliah/Felix/svl_adapter/data/eurosat/eurosat_split.json', 'r') as f:
    data = json.load(f)

# Create custom dataset
dataset = CustomDataset(data['train'], root_dir='/l/users/sanoojan.baliah/Felix/svl_adapter/data/eurosat/2750', transform=transform)

# Extract embeddings for images
def generate_clip_embeddings_with_paths(dataset):
    image_embeddings = []
    image_paths = []
    labels = []
    for image, label, path in dataset:
        image_paths.append(path)
        image_tensor = preprocess(image).unsqueeze(0).to(device)
        with torch.no_grad():
            image_embedding = model.encode_image(image_tensor)
        image_embeddings.append(image_embedding.cpu().numpy())
        labels.append(label)
    return np.concatenate(image_embeddings), labels, image_paths

embeddings, labels, image_paths = generate_clip_embeddings_with_paths(dataset)

# Reduce dimensionality using t-SNE
tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

# Plot the t-SNE embeddings with colors based on class labels
plt.figure(figsize=(10, 8))
for i, label in enumerate(set(labels)):
    indices = np.where(np.array(labels) == label)[0]
    plt.scatter(embeddings_2d[indices, 0], embeddings_2d[indices, 1], label=f'Class {label}')

# Add labels for the data points
for i, image_path in enumerate(image_paths):
    plt.annotate(image_path, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.title('t-SNE plot of CLIP embeddings')
plt.xlabel('t-SNE dimension 1')
plt.ylabel('t-SNE dimension 2')
plt.legend()
plt.show()
