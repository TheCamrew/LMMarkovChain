import markovify
import sys

# Read text from file
if len(sys.argv) < 3 and len(sys.argv) > 4:
    sys.exit("Usage: python generator.py sample.txt order startword[opt]")

with open(sys.argv[1]) as f:
    text = f.read()

# Train model
text_model = markovify.Text(text, state_size = int(sys.argv[2]))

count = 1

def get_text():
    if len(sys.argv) == 3:
        return text_model.make_sentence()
    else:
        return text_model.make_sentence_with_start(sys.argv[3], strict=False)
    

# Generate sentences
try:
    gen = get_text()
except markovify.text.ParamError as e:
    sys.exit(e)

while gen == None:
    gen = get_text()
    count += 1
    print(count)

print()
print(gen)