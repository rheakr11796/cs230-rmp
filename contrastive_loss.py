import torch
def contrastive_loss(embeddings):
    """Computes the L2 distance between the two source embeddings, which are
    4D torch tensors with the first dimension representing the individual source embedding"""
    embeddings_0 = embeddings[0, :, :, :]
    embeddings_1 = embeddings[1, :, :, :]
    return torch.linalg.norm(torch.subtract(embeddings_0, embeddings_1), dim=None).item()


