# Importing Libaries
from transformers import pipeline
import argparse

def summarizeSentences(sentences):
    """
    sentences : These are list of sentences that we want to summarize
    """

    summarize = pipeline("summarization", model = "sshleifer/distilbart-cnn-12-6")

    summarize_sentences = summarize(sentences)

    return summarize_sentences


if __name__ == "__main__":
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(description='Summarize sentences')
    
    # Add argument for sentences
    parser.add_argument('--sentence', nargs='+', type=str, help='Sentences that we want to summarize separated by commas')
    
    # Parse arguments
    args = parser.parse_args()
    # Check if --sentence argument is provided
    if args.sentence:
        # Join the list of strings into a single comma-separated string
        input_string = ",".join(args.sentence)
        
        # Split the input string by commas to get individual sentences
        sentences_list = [sentence.strip() for sentence in input_string.split(',')]

        # Call the function with the list of sentences
        summarized_sentences = summarizeSentences(sentences_list)

        print(summarized_sentences)