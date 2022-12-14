import exrex

your_regex = '\+7-(\d{3})-\\1-13-60' # +7-000-000-13-60 обратите внимание на \1 обращение к первой группе необходимо экранировать \\1 аналогично символ + \+

# print(exrex.getone('\d{4}-\d{4}-\d{4}-[0-9]{4}'))
# print(list(exrex.generate('\d{1}-\d{1}-\d{2}-[0-9]{1}',3))) # beware of out of ram situation a (10^4)^4 eats out 16GB
# комментарий для тех кому интересен или знаком Пайтон:
#  generate возвращает объект генератор, следовательно вместо того чтобы заполнять память формируя полный список лучше использовать генерацию в цикле (тогда одновременно в ОЗУ хранится только 1 сгенерированная строка)

# print(list(exrex.generate('\+7-\d{3}-\d{3}-13-60'))) # возможные телефонные номера РФ заканчивающиеся на 13-60 (10^6 штук)
with open('out.txt','w') as out:
    
    for str in exrex.generate(your_regex): 
        out.write(str+'\n')
        # print(str)

