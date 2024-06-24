# Importing Libaries
from transformers import pipeline
import argparse

def predictMaskedWords(sentences):
    """
    sentences : These are list of masked sentence on which we want to predict masked words
    """

    mlm = pipeline("fill-mask", model = "distilroberta-base")

    masked_words = mlm(sentences)

    return masked_words

if __name__ == "__main__":
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(description='predict masked word')
    
    # Add argument for sentences
    parser.add_argument('--sentence', nargs='+', type=str, help='Sentences for mask word prediction separated by commas')
    
    # Parse arguments
    args = parser.parse_args()
    # Check if --sentence argument is provided
    if args.sentence:
        # Join the list of strings into a single comma-separated string
        input_string = ",".join(args.sentence)
        
        # Split the input string by commas to get individual sentences
        sentences_list = [sentence.strip() for sentence in input_string.split(',')]

        # Call the function with the list of sentences
        generated_sentences = predictMaskedWords(sentences_list)

        print(generated_sentences)


