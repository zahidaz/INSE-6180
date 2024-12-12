import os
import torch

# Dataset paths
ROOT_PATH = "/Users/zahid/downloads/shared/privacy and data mining/ml"
DATASET_PATH = f"{ROOT_PATH}/dataset/dataset.tsv"
MODEL_SAVE_PATH = f"{ROOT_PATH}/saved_model"
FILE_TO_PREDICT = f"{ROOT_PATH}/dataset/mal/9.trace"

# Model and tokenizer configurations

# MODEL_NAME = "distilbert-base-uncased"
# MODEL_NAME = "gpt2"
# MODEL_NAME = "bert-base-cased"
MODEL_NAME = "roberta-base"

MAX_LENGTH = 512


TRAINING_ARGS = {
    "output_dir": f"{MODEL_SAVE_PATH}",
    "learning_rate": 2e-5,
    "per_device_train_batch_size": 4,
    "per_device_eval_batch_size": 4,
    "num_train_epochs": 3,
    "weight_decay": 0.01,
    "eval_strategy": "epoch",
    "save_strategy": "epoch",
    "logging_dir": f"{MODEL_SAVE_PATH}/logs",
    "logging_steps": 10,
    "load_best_model_at_end": True,
    "metric_for_best_model": "accuracy",
    "save_total_limit": 2,
    "use_cpu": not torch.cuda.is_available(),
}

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
