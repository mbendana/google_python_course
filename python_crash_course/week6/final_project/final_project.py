#import wordcloud

def calculate_frequencies(file_contents):
	# Here is a list of punctuations and uninteresting words you can use to process your text
	punctuations = ''''·!()-[]{};:'"\,<>./?@#$%^&*_~,'''
	uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

	# LEARNER CODE START HERE
	#def remove_punctuations(file_contents):
	for char in punctuations:
		if char in file_contents:
			text = file_contents.replace(char, "")

	word_count = {}
	for word in text.split(" "):
		if word in uninteresting_words:
			continue
		if word not in word_count:
			word_count[word] = 1
		else:
			word_count[word] += 1

	return word_count
	#return remove_punctuations

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

frequencies = calculate_frequencies(text)
print(frequencies)

#cloud = wordcloud.WordCloud()
#cloud.generate_from_frequencies(frequencies)
#cloud.to_file("myfile.jpg")

