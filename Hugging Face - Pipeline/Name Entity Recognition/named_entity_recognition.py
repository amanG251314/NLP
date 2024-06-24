# Importing Libaries
from transformers import pipeline
import argparse

def generateNameEntities(sentences):
    """
    sentences : These are list of sentences on which we want to recognise the name entity
    """

    ner = pipeline("ner", model = "dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy = "simple", device = 0) # Device 0 is for GPU

    named_entities = ner(sentences)

    return named_entities


if __name__ == "__main__":
    # Initialize ArgumentParser
    parser = argparse.ArgumentParser(description='generate named enitites')
    
    # Add argument for sentences
    parser.add_argument('--sentence', nargs='+', type=str, help='Sentences for named entity prediction separated by commas')
    
    # Parse arguments
    args = parser.parse_args()
    # Check if --sentence argument is provided
    if args.sentence:
        # Join the list of strings into a single comma-separated string
        input_string = ",".join(args.sentence)
        
        # Split the input string by commas to get individual sentences
        sentences_list = [sentence.strip() for sentence in input_string.split(',')]

         # Call the function with the list of sentences
        result = generateNameEntities(sentences_list)

        print(result)

