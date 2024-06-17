import torch
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from PIL import Image
import clip

# Load the pre-trained CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Function to generate embeddings for images
def generate_clip_embeddings(images):
    image_tensors = torch.stack([preprocess(Image.open(image)).to(device) for image in images])
    with torch.no_grad():
        image_features = model.encode_image(image_tensors)
    return image_features.cpu().numpy()

# Sample images and their corresponding labels
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg", ...]
class_labels = [0, 1, 0, ...]  # Example labels corresponding to each image

# Generate embeddings for the sample images
embeddings = generate_clip_embeddings(image_paths)

# Reduce dimensionality using t-SNE
tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

# Plot the t-SNE embeddings with colors based on class labels
plt.figure(figsize=(10, 8))
for i, label in enumerate(set(class_labels)):
    indices = np.where(np.array(class_labels) == label)[0]
    plt.scatter(embeddings_2d[indices, 0], embeddings_2d[indices, 1], label=f'Class {label}')

# Add labels for the data points
for i, image_path in enumerate(image_paths):
    plt.annotate(image_path, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.title('t-SNE plot of CLIP embeddings')
plt.xlabel('t-SNE dimension 1')
plt.ylabel('t-SNE dimension 2')
plt.legend()
plt.show()
