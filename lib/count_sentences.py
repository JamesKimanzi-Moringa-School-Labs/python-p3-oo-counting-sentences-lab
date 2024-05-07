class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the value by '.', '?', and '!'
        # Count the number of non-empty substrings after splitting
        return len([sentence for sentence in filter(None, self.value.split('.!?'))])

# Example usage:
my_string = MyString("Hello, world!")
print(my_string.is_sentence()) 
print(my_string.is_question())  
print(my_string.is_exclamation())  
print(my_string.count_sentences())  