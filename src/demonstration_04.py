"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    # Your code here
    emoji_dict = {"smile": ":D",
                  "grin": ":)",
                  "sad": ":(",
                  "mad": ":P"}
    # split sentence into words
    words = list(txt.split(" "))
    # Iterating on every word from the dict
    for i in range(len(words)):
        if words[i] in emoji_dict:
            words[i] = emoji_dict[words[i]]
    # Re-adding the whitespace
    new_text = " ".join(words)
    return new_text

print(emotify("Make me smile"))
print(emotify("Make me grin"))

