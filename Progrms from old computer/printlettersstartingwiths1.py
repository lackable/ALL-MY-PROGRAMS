st="Print only the words starting with s in this sentence"
letter = []
splitst = st.split()
for letters in splitst:
    if letters[0] == 's':
       letter.append(letters)

print(letter)
