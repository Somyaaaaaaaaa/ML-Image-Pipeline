from data_loader import load_data
from preprocessing import preprocess
from model import build_model
from train import train
from evaluate import evaluate


def main():
    data = load_data()
    data = preprocess(data)
    model = build_model()
    model = train(model, data)
    metrics = evaluate(model, data)

    print("Pipeline finished.")
    print("Metrics:", metrics)


if __name__ == "__main__":
    main()
