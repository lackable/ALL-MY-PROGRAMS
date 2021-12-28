st = 'Print every word in this sentence that has an even number of letters'
stsplit = st.split()
for word in stsplit:
    if len(word)%2 == 0:
        print("EVEN!")
