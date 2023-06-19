# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

string = "Высокоуровневый язык программирования общего назначения с динамической строгой типизацией \
        и автоматическим управлением памятью, ориентированный на повышение производительности разработчика,\
        читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[27].\
        Язык является полностью объектно-ориентированным в том плане, что всё является объектами[25]. \
        Необычной особенностью языка является выделение блоков кода пробельными отступами[28]. Синтаксис ядра \
        языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к \
        документации[27]. Сам же язык известен как интерпретируемый и используется в том числе для \
        написания скриптов[25]. Недостатками языка являются зачастую более низкая скорость работы и \
        более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, \
        написанным на компилируемых языках, таких как C или C++[25][27]."

words_list = string.replace('.','').replace(',', '').replace('[', ' ').replace(']', ' ').lower().split()
print(words_list)


new_string = ''
for word in string:
    if word.isalpha() or word == ' ':
        new_string += word
w_list = new_string.split()


dict_words = {}

for frequency, word in enumerate(w_list, start=1):
    word_count = w_list.count(word)
    dict_words[word] = word_count

sorted_dict = dict(sorted(dict_words.items(), key=lambda x:x[1], reverse=True))

print('10 самых частых слов и количество их появлений в тексте: ')
for word in list(sorted_dict)[0:10]:
    print(f'"{word}": {sorted_dict.get(word)}')
    