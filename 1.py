print("Question1")
import re
s1=re.split('[@.]',"zuck26@facebook.com")
print(list(s1))
s2=re.split('[@.]', "page33@google.com")
print(list(s2))
s3=re.split('[@.]',"jeff42@amazon.com" )
print(list(s3))
print('*'*10)
print('\n')

print("Question2")
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
m = re.findall('[bB]\w+', text)
print(m)
print('*'*10)
print('\n')

print("Question3")
import re
sentence = "A, very very; irregular_sentence"
o=re.sub('[_\W+]',' ',sentence)
print(o)
print('*'*10)
