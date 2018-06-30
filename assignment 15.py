#QUESTION 1

import re
email="zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"

output=re.findall("(\w+)@([A-Z0-9]+)\.([A-Z]{2,3})",email,flags=re.IGNORECASE)
print(output)

#QUESTION 2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
t=re.findall("[bB]\w+",text,flags=re.IGNORECASE)
print(t)


#QUESTION 3
import re
sentence = "A, very very; irregular_sentence"
output=re.sub("[,_;]"," ",sentence)
print(output)

#OPTIONAL QUESTION
import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
r=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|((\w+:\/\/\S+))"," ",tweet).split())
print(r)