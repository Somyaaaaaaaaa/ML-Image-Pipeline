# Image ML Pipeline

An end-to-end, reproducible image-based machine learning pipeline built from scratch.
The project demonstrates the complete workflow of loading image data from disk,
preprocessing it, training a simple convolutional neural network, and evaluating results.

This repository focuses on correctness, clarity, and reproducibility rather than model performance.

---

## Project Overview

The pipeline follows this flow:

Data (images on disk)
→ Data Loading
→ Preprocessing
→ Model Definition
→ Training
→ Evaluation
→ Metrics

The goal is to provide a clean reference implementation of a minimal but real
image classification system.

---

## Project Structure

image-ml-pipeline/
- src/
  - main.py # Entry point for running the pipeline
  - data_loader.py # Loads images and labels from disk
  - preprocessing.py # Image resizing and preparation
  - model.py # CNN architecture definition
  - train.py # Training loop and optimization
  - evaluate.py # Model evaluation and accuracy computation
- data/
  - images/ # Image dataset (folder-per-class)
- results/ # Saved outputs 
- configs/ # Defaul configuration files 
- requirements.txt
- README.md


---

## Setup

Install dependencies:

pip install -r requirements.txt


---

## Running the Project

From the project root:

python src/main.py

----

## Results

Evaluation metrics are saved to:

results/metrics.json

This allows experiment outputs to be inspected or compared across runs.

----

This will:
- load images from `data/images`
- preprocess them to a fixed size
- train a simple CNN
- evaluate the model
- print final accuracy

---

## Notes

- This project is intentionally minimal.
- The dataset is small and accuracy is not a goal.
- The focus is on understanding and implementing the full ML pipeline correctly.
- The structure is designed to be extended with larger datasets, batching, and configuration files.
