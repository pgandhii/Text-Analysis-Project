# Text-Analysis-Project

Please read the [instructions](instructions.md).

# Project Overview
For this project, I used two texts from Project Gutenberg, which are 'The Time Machines by H.G. Wells from 1895, and 'The Lost World' by Arthur Conan Doyle written in 1912. My goal was to explore how language, vocabulary richness, and emotional tone of science fiction writing changed between the late 19th and early 20th centuries. I used Natural Language Processing techniques, such as sentiment analysis through VADER. Through this project, I hoped to gain a better understanding of how tools can help quantify writing style and sentiment in literature and speech over time.

# Implementation
I implemented the project step-by-step, following the structure outlined in the instructions.
1. Text Cleaning & Preprocessing: I removed Gutenberg boilerplate, punctuations and digits, and converted all text to lower case.
2. Used NLTK's build in English stop word list to remove common words such as "the", "and", and "is". This helped me focus on the meaningful words.
3. Then I built a frequency dictionary to identify the most common words in eahc novel.
4. Next, I computed total number of words, number of unqiue words, average word length and vocabulary richness.
5. I created a bar chart to display the top words in each text.
6. Finally, I used VADER Sentimental Intensity Analyzer from NLTK to measure the proportion of positive, negative, and neutral language in each novel.

Throughout the process, I used ChatGPT to understand new libraries, fix code errors and clarify logic when my outputs did not appear as expected.

# Results

The results highlighted that 'The Lost World' (late 1890s) had a larger vocabulary and slightly higher positive tone, which fits its adventuruous and energetic style. The 'Time Machien', on the other hand, was slightly more neutral and technical, relfecting Well's philosophical approach to sci-fi. What surprised me was that 'said' was the top recurring in both the texts, showing how heavily the texts relied on dialogue. This was more so evident with 'The Lost World' than 'Time Machine'. These results suggest that early 20th-century adventure fiction leaned more toward action and interaction, while late 19th-century science fiction remained introspective and conceptual.

# Reflection
From a process standpoint, the assignment was well-structured in the sense that it laid out the steps very clearly, which helped me complete the assignment step-by-step, instead of getting overwhelmed by the instructions. My biggest challenge was debugging because, for a long time, when I ran my code, it produced no output. AI tools helped me trace the issue to small mistakes like typos or misplaced variables. Once I fixed those, everything clicked and I was able to see how the full pipeline connected together.

From a learning perspective, the project helped me understand how AI models process text, how tools like FactSet sentiment analysis might work behind the scenes, and how programming structure supports text based analysis. If I could redo the project, I'd start earlier to give myself more time for understanding and experimentation. Going forward, I'll apply what I learned here to approach the project in a more systematic, and incremental manner. Especially because I want to give myself the time to truly explore the content.
