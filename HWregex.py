from pprint import pprint
import re
import csv


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

updated_contact_list = []
names_list = []


for contact in contacts_list:
    s = ','
    new_contact = s.join(contact)
    pattern = "([А-ЯЁ][а-яё]+)(\s|\,)([А-ЯЁ][а-яё]+)(\s|,+)([А-ЯЁ][а-яё]+)?(,+)([А-ЯЁ]+[а-яё]*)?(,+)" \
        "([a-zа-яёА-ЯЁ –]*)?(,+)(8\s|\+7\s\(|\s|\(|\+7|8\()?(\d{3})?(\)\s|\-|\))?(\d{3})?(-)?(\d{2})?(-)?" \
            "(\d{2})?(\s\(|\s)?(доб\.)?(\s)?(\d{4})?(\,|\)\,)?(\w+\.?\w+\@\w+\.\w+)?"
    res = re.sub(pattern, r"\1, \3, \5, \7, \9, +7(\12)\14-\16-\18 \20\22, \24", new_contact)
    pattern2 = "\s\,"
    res2 = re.sub(pattern2, r",", res)
    pattern3 = "\,{2,10}"
    res3 = re.sub(pattern3, r",", res2)
    res3_split = res3.split(',')
    last_name = res3_split[0]
    updated_contact_list.append(res3_split)
    names_list.append(last_name)

unique_names_list = []
for name in names_list:
    if name in unique_names_list:
        pass
    else:
        unique_names_list.append(name)

names_dict = {}

for name in unique_names_list:
    name_index_list = []
    for contact in updated_contact_list:
        if name in contact:
            name_index_list.append(updated_contact_list.index(contact))
    names_dict[name] = name_index_list

for name, i in names_dict.items():
    if len(i) == 2:
        updated_contact_list[i[0]] += updated_contact_list[i[1]]

for contact in updated_contact_list:
    if len(contact) <= 7 and ' +7()--' in contact:
        updated_contact_list.remove(contact)

new_list = []
final_list = []

for contact in updated_contact_list:
    if contact != updated_contact_list[0]:
        contact_list = []
        s = ''
        new_contact = s.join(contact)
        contact_list.append(new_contact)
        new_list.append(contact_list)
    else:
        final_list.append(contact)

for contact in new_list:
    pattern = "([А-ЯЁ][а-яё]+)(\s)([А-ЯЁ][а-яё]+)(\s)([А-ЯЁ][а-яё]+)(\s)([А-ЯЁа-яё]*)(\+7\(\)\-\-)?(\s)" \
        "([a-zа-яёА-ЯЁ –]*)?(\+7\(\)\-\-)?(\+7\(\d{3}\)\d{3}\-\d{2}\-\d{2})?(\s)?([А-ЯЁ])?([а-яё]+\s)?([А-ЯЁ])" \
            "?([а-яё]+\s)?([А-ЯЁ])?([а-яё]+\s)?([А-ЯЁа-яё]+)?(\s)?([a-z][а-яёА-ЯЁ –]+)?(\sдоб\.\d{4})?(\s)" \
            "(\+7\(\)\-\-)?([А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s\+7\(\)\-\-\s)?(\w+\.?\w+\@\w+\.\w+)?"
    res = re.sub(pattern, r"\1, \3, \5, \7, \22\10, \12\23, \27", contact[0])
    pattern1 = "\,\s\,"
    res1 = re.sub(pattern1, r",", res)
    pattern2 = "\s\,"
    res2 = re.sub(pattern1, r",", res1)
    new_contact = res2.split(', ')
    final_list.append(new_contact)

final_list[0][0].split(' ')

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(final_list)
