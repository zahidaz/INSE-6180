from datasets import load_dataset
import transformers
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
)
import evaluate
import numpy as np
import torch
# transformers.logging.set_verbosity_info()
data_file = "/Users/zahid/Downloads/shared/PRIVACY&DATAMINING/ml/dataset/dataset.psv"
out_dir = "/Users/zahid/Downloads/shared/PRIVACY&DATAMINING/ml/dataset"
model_name = "bert-base-cased"  
column_names = ["text", "label"]

metric = evaluate.load("accuracy")

def build_and_split_dataset(data_file):
    dataset = load_dataset(
        "csv",
        data_files=data_file,
        delimiter="|",
        column_names=column_names,
    )
    # small dataset, so just use the same data for train and test
    dataset["test"] = dataset["train"]
    return dataset

def tokenize_function(examples, tokenizer):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

def get_trainer(model, tokenized_datasets, training_args):
    return Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
        compute_metrics=compute_metrics,
    )


def predict_label(input, model):
    inputs = tokenizer(input, return_tensors="pt", truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_label = torch.argmax(logits, dim=-1).item()
    return predicted_label
   


if __name__ == "__main__":
    dataset = build_and_split_dataset(data_file)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenized_datasets = dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)
    print(tokenized_datasets)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    training_args = TrainingArguments(
        output_dir=out_dir,
        eval_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        num_train_epochs=5,
        weight_decay=0.01,
        logging_dir=f"{out_dir}/logs",
        logging_steps=1,
        use_cpu=True,
    )
    
    trainer = get_trainer(model, tokenized_datasets, training_args)
    trainer.train()
    trainer.save_model(out_dir)
    print(trainer.evaluate())

    test_dataset = tokenized_datasets["test"]

    for i in range(len(test_dataset)):
        text = test_dataset[i]["text"]
        label = test_dataset[i]["label"]
        predicted_label = predict_label(text, model)
        # print(f"Label: {label}, Predicted: {predicted_label}")

