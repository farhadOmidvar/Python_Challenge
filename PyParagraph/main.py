# PyPraragraph
import os
import re

select_file = input("Select Paragraph,(1)or(2)or(3):")
file_name = f"paragraph_{select_file}.txt"
print(file_name)
file_path = os.path.join('raw_data',file_name)
try:
	text_file = open(file_path)
except:
	print('The file cannot be opened:',file_name)
	exit()
paragraph = text_file.read()
counter = 0
for line in paragraph:
	line.rstrip()
	counter += 1
print(counter)
new_paragraph = paragraph.replace(" ","")
# Approximate word count
word_count = len(re.findall('\\w+', paragraph))
# Approximate sentence count
sentence_count = len(re.split("(?<=[.!?]) +", paragraph))
letter_count = len(new_paragraph)

paragraph_analysis = f"""
Paragraph Analysis
--------------------
Approximate Word Count: {word_count}
Approximate Sentence Count: {sentence_count}
Average Letter Count : {letter_count / word_count}
Average Sentence Lenght: {word_count / sentence_count}
"""
print(paragraph_analysis)