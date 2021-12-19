from sklearn.metrics import normalized_mutual_info_score, adjusted_rand_score
from numpy.lib.function_base import interp
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
from typing import Optional, Tuple
import pandas as pd

def pca(data: pd.DataFrame, n_components: int = 2) -> pd.DataFrame:
    """    
    - Dimensionality Reduction Method: Principal component analysis (PCA).
    - Uses the implementation of *scikit-learn*.
    - The expected output DataFrame has n_components columns whose names are: PC0, PC1, ...
    """
    PCs = ???
    return PCs

def tsne(data: pd.DataFrame, n_components: int = 2) -> pd.DataFrame:
    """    
    - Dimensionality Reduction Method: T-distributed Stochastic Neighbor Embedding (TSNE).
    - Uses the implementation of *scikit-learn*.
    - The expected output DataFrame has n_components columns whose names are: PC0, PC1, ...
    """
    PCs = ???
    return PCs

def visualize(data: pd.DataFrame, label: Optional[pd.DataFrame] = None) -> None:
    """
    - Draw scatter plot in embedding coordinates (e.g. PCA, T-SNE).
    - Note that the color of the same label should be same, and vice versa.

    --------------------
    Parameters
    --------------------
    data
        The dataframe whose rows correspond to cells and columns to two embeddings.
    label
        Optional labels for coloring the scatter plot.
    --------------------
    """
    pass

def cluster(data: pd.DataFrame, k: Optional[int] = 8) -> pd.DataFrame:
    """
    - Cluster cells into subgroups using Kmeans.
    - Uses the implementation of *scikit-learn*.
    - The expected output DataFrame has one column named 'label'.

    --------------------
    Parameters
    --------------------
    data
        The dataframe whose rows correspond to cells and columns to two embeddings.
    k
        The number of subgroups.
    --------------------
    """
    labels = ???
    return labels

def evaluate(data: pd.DataFrame, ground_truth: pd.DataFrame) -> Tuple[float, float]:
    """
    - Evaluate the clustering performance using metrics Normalized Mutual Information (NMI) 
      and Adjusted Rand Index (ARI).
    - Uses the implementation of *scikit-learn*.

    --------------------
    Parameters
    --------------------
    data
        The labels generated according to the clustering result.
    ground_truth
        The ground truth label.
    --------------------

    --------------------
    Returns
    --------------------
    A tuple (NMI, ARI)
    --------------------
    """
    NMI = ???
    ARI = ???
    return (NMI, ARI)