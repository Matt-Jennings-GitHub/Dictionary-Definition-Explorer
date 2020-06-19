# Modules
from PyDictionary import PyDictionary
import nltk
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt

# Functions
def clean(string):
    for char in [',',';',':','.','-','(',')','`',"'",'"']:
        string = string.replace(char,'')
    return string

# Setup Dictionary
dictionary=PyDictionary()
nltk.download('stopwords')
simple_words = stopwords.words('english')

# Word variables
known_words = set()
unknown_words = set()
score = 0 # Represents the total words that must be learned

# Parent Word
init_word = input("Initial Word: ")
definition = clean(list(dictionary.meaning(init_word).values())[0][0])
#print(definition)
for word in definition.split(" "):
    if word not in simple_words and len(word) > 1 :
        unknown_words.add(word)

# Display
fig,ax = plt.subplots(1,2)
fig.suptitle('Learning Word: "{}"'.format(init_word),fontweight='bold')
def format_axes():
    ax[0].clear()
    ax[0].set_title('Padding',c='white',size=20)
    ax[0].set_xlabel('Padding',c='White',size=20)
    fig.text(0.52, 0.05, 'Iteration Number', ha='center')
    ax[0].set_ylabel('Total Words Learned',c='black')
    #ax[1].set_xlabel('Iteration',c='black')
    ax[1].clear()
    ax[1].set_ylabel('Remaining Words To Learn',c='black')

plt.ion()
plt.show()

iteration = 0
ax0_out_array = []
ax1_out_array = []
# Child Words
while len(unknown_words) > 0:
    word = unknown_words.pop()
    known_words.add(word)

    try:
        print("Learnt: {}".format(word))
        definition = clean(list(dictionary.meaning(word).values())[0][0])
        
        for word in definition.split(" "):
            if (word not in known_words.union(simple_words)) and (len(word) > 1) :
                unknown_words.add(word)
                score += 1

        # Display
        iteration += 1
        spacing = 1
        if iteration % spacing == 0 :
            format_axes()
            ax0_out_array.append(score)
            ax0_in_array = np.arange(0,iteration,spacing)
            ax[0].plot(ax0_in_array, ax0_out_array, color='cyan')

            ax1_out_array.append(len(unknown_words))
            ax1_in_array = np.arange(0,iteration,spacing)
            ax[1].plot(ax1_in_array, ax1_out_array, color='cyan')

            fig.tight_layout()
            plt.draw()
            plt.pause(0.01)

    except:
        print("Error with: {}".format(word))
        

print("Total Score for {}: {}".format(init_word,score))
    
