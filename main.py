"""importing re for regular expression related work"""
import re



"""Creating class Stemmer which take string with preposition and return base word removing preposition"""

class stemmer:
    """variable to store regular expression required to filter preposition"""
    regexp = "";


    """list of nepali base words"""
    data = [];

    """constructor: this reads nepali base words from data.txt and stores in data[]"""
    def __init__(self):
        file = open("data.txt","r");
        str = file.read();
        file.close();
        self.data = list(str.split());


        """This function takes preposition list and makes regular expression from it"""
    def add_preposition(self,x):
        self.regexp = r"|".join(x);
        self.regexp = r"("+self.regexp+r")";
        self.regexp = self.regexp + "$";

        """This function searches given word in data[ ] and if not found there, performs preposition removal"""
    def stem(self,y):
        y = re.sub(r"\t|\s|\n","",y);

        if y in self.data:
            return y;
        else:
            p=re.sub(self.regexp,"",y);
            return p;

#********************************************************************************************************#
"""main funtion starts this point onward"""
"""Here "A" is the list of Nepali prepositions to be passed to the model to filter preposion"""
A = ["माथि","सम्म","पारि","पछि","बमोजिम","सम्बन्धि","विरुद्ध","माझ","वरिपरि","मा","ले","ताका","बाहेक","लागि","बाट","बीच","भित्र","नजिक","को","का","कि","विपरित","बाहिर","प्रति","देखि","तिर","तर्फ","मार्फत्","सँग","बिना","लाई"];

"""Creating the instance of the model stemmer"""
mod = stemmer();

"""Passing preposition to the model"""
mod.add_preposition(A);

"""Taking input from the user"""
n = int(input("How many words do you want to input: "));


for i in range(n):
    """Taking word input"""
    word = input("Enter the word: ");

    """Printing the base word. stem function does all this work"""
    print(mod.stem(word));
