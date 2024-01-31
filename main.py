#REMOVE PASS AND FIX THE FUNCTION
def build_dictionary(words):
    word_counts = {}
    for word in words:
        if word in word_counts.keys():
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

# REMOVE PASS AND FIX THE CODE TO:
if __name__ == '__main__':
    user_input = input("Enter your input: ")
    words = user_input.split()
    word_counts = build_dictionary(words)
    for key in sorted(word_counts.keys()):
        print(key,"-",word_counts[key])
    