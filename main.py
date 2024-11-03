import argparse
from classifier import classify_text

def main():
    parser = argparse.ArgumentParser(description="Classify text based on topic.")
    parser.add_argument("input_text", type=str, help="Text to classify")
    args = parser.parse_args()

    try:
        result = classify_text(args.input_text)
        print(result)
    except Exception as e:
        print(f"An error occurred during classification: {e}")

if __name__ == "__main__":
    main()
