# Importing Libaries
from transformers import pipeline
import argparse

def generateText(sentences):
    """
    sentences : These are list of sentence on which we want text generation
    """

    gen = pipeline("text-generation", model = "gpt2")

    completed_senteces = gen(sentences, num_return_sequences = 1, max_length = 50)

    return completed_senteces

if __name__ == "__main__":
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(description='text generate on sentences')
    
    # Add argument for sentences
    parser.add_argument('--sentence', nargs='+', type=str, help='Sentences for text generation separated by commas')
    
    # Parse arguments
    args = parser.parse_args()
    # Check if --sentence argument is provided
    if args.sentence:
        # Join the list of strings into a single comma-separated string
        input_string = ",".join(args.sentence)
        
        # Split the input string by commas to get individual sentences
        sentences_list = [sentence.strip() for sentence in input_string.split(',')]

        # Call the function with the list of sentences
        generated_sentences = generateText(sentences_list)

        print(generated_sentences)
