from typing import Dict, List, Tuple

import numpy as np


def custom_predict(y_prob: np.ndarray, threshold: float, index: int) -> np.ndarray:
    """Custom predict function that defaults
    to an index if conditions are not met.

    Args:
        y_prob (np.ndarray): _description_
        threshold (float): _description_
        index (int): _description_

    Returns:
        np.ndarray: _description_
    """
    y_pred = [np.argmax(p) if max(p) > threshold else index for p in y_prob]
    return np.array(y_pred)


def predict(texts: List, artifacts: Dict) -> List:
    """Predict tags for given texts.

    Args:
        texts (List): _description_
        artifacts (Dict): _description_

    Returns:
        List: _description_
    """
    x = artifacts["vectorizer"].transform(texts)
    y_pred = custom_predict(
        y_prob=artifacts["model"].predict_proba(x),
        threshold=artifacts["args"].threshold,
        index=artifacts["label_encoder"].class_to_index["other"],
    )
    tags = artifacts["label_encoder"].decode(y_pred)
    predictions = [
        {
            "input_text": texts[i],
            "predicted_tags": tags[i],
        }
        for i in range(len(tags))
    ]
    return predictions
