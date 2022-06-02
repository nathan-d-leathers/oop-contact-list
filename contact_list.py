from unicodedata import name
shared_list = []

class ContactList():

    def __init__(self,name, contacts):
        self.name = name
        self.contacts = sorted(contacts,key=lambda key: key["name"])

    def __str__(self):
        return f"{self.name} : {self.contacts}"


    def find_shared_contacts(self):
        for self.name in self.contacts:
            if self.contacts._contains_(self.name):
                shared_list.append(self.name)
# not working code :(

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

friends_list = ContactList("my_friends",friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

friends_i_work_with = friends_list.find_shared_contacts(my_work_buddies)
print(shared_list)
















    # def add_contact({}):
    #     {
    #         'name ': name,
    #         'number ': number,
    #     }

    # def remove_contact({})


# blank_contact = ContactList({
#     'name': f{name}
#     'number': f{number},
# })

# paul = blank_contact('paul', 5678324569)

# print(paul)

# =--==--=-=-=-=-=-=--=-=-=-=---=-=-=-=-=-=-=
# add_contact = ContactList

# paul = add_contact('paul',555555555)
# jaul = add_contact('jaul',777777777)
# maul = add_contact('maul',333333222)

# for con in ContactList.new_contacts:
#     print(con.number)
# # output:
# 555555555
# 777777777
# 333333222
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-




# jef = ContactList('jeff', 6036444646)
# print(jef.contact)
# jef.contact = {
#     'name': jef.name,
#     'number': jef.number,
#     }

    # def contact(self,person):
    #     self.person = {
    #         'name': self.name,
    #         'number': self.number,
    #     }


# print(jef.contact)