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
    # print(res3)
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
    counter = 0
    name_index_list = []
    for contact in updated_contact_list:
        if name in contact:
            name_index_list.append(updated_contact_list.index(contact))
    names_dict[name] = name_index_list

# print(names_dict)

updated_contact_list[2] += updated_contact_list[4]
updated_contact_list[7] += updated_contact_list[8]

for contact in updated_contact_list:
    s = ','
    contact = s.join(contact)
    print(contact)

pattern1 = "(Мартиняхин)(\,\s)(Виталий)(\,\s)(Геннадьевич)(\,\s)(ФНС)(\,\s)(\+7\(495\)913\-00\-37)(\,\s\,)" \
"(Мартиняхин)(\,\s)(Виталий)(\,\s)(Геннадьевич)(\,\s)(ФНС)(\,\s)" \
"(cоветник отдела Интернет проектов Управления информационных технологий)(\,\s)(\+7\(\)\-\-\,)"
update1 = re.sub(pattern1, r"\1, \3, \5, \7, \19, \9", updated_contact_list[2])

pattern2 = "(Лагунцов)(\,\s)(Иван)(\,\s)(Алексеевич)(\,\s)(Минфин)(\,\s)(\+7\(495\)913\-11\-11\sдоб\.0792)" \
        "(\,\s\,)(Лагунцов)(\,\s)(Иван)(\,\s)(\+7\(\)\-\-\,\s)(Ivan.Laguntcov@minfin.ru)"
update2 = re.sub(pattern2, r"\1, \3, \5, \7, \9, \16", updated_contact_list[7])

updated_contact_list.remove(updated_contact_list[8])
updated_contact_list.remove(updated_contact_list[4])

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(updated_contact_list)
