import json

# from utils import owl

from ontobot.services import subkind
# from rules import phase
# from rules import category
# from rules import role
# from rules import rolemixin
# from rules import custom

# with open('data files/taxonomies5.json') as user_file:
#     file_contents = user_file.read()

# parsed_json = json.loads(file_contents)


class ODPFactory:

    @classmethod
    def get_ontouml_odp(cls, pattern, parsed_json):
        match pattern:
            case 'subkind':
                print(parsed_json)
                return subkind.Subkind(parsed_json)
            # case 'phase':
            #     return phase.Phase(parsed_json)
            # case 'category':
            #     return category.Category(parsed_json)
            # case 'rolemixin':
            #     return rolemixin.RMixin(parsed_json)
            # case 'role':
            #     return role.Role(parsed_json)
            # case 'custom':
            #     return custom.Custom(parsed_json)
            case _:
                return Exception('something went wrong')


# sk: subkind.Subkind = ODPFactory.get_ontouml_odp('subkind', parsed_json)
# sk.check_subkind()
# print(sk.get_subkind_list())
# print(owl.OWL.get_taxonomy_json())
