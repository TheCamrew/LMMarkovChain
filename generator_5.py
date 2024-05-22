import markovify
import sys

# Read text from file
if len(sys.argv) != 3:
    sys.exit("Usage: python generator.py sample.txt startword")
with open(sys.argv[1]) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text)

# Input phrase
input_phrase = sys.argv[2]

print()
for i in range(5):
    print(text_model.make_sentence_with_start(input_phrase, strict=False))
    print()
