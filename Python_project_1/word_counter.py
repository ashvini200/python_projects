# word_counter.pyh

# Function to count words in the given text
def count_words(text):
    """
    """
    words = text.split()
    return len(words)

def main():
    """
    """
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ")
    
    # Check if the input is empty
    if not user_input.strip():
        print("Input is empty. Please enter some text.")
    else:
        # Count the words in the input text
        word_count = count_words(user_input)
        # Display the word count
        print("Word Count:", word_count)

if __name__ == "__main__":
    main()
