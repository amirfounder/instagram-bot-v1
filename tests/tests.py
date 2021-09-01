import sys
sys.path.append('C:\\Users\\Amir Sharapov\\Code\\amirfounder\\programs\\1')


from src.data_manager.domains.InstagramDataManager import InstagramDataManager


# Tests and sandbox mode here.

igdm = InstagramDataManager()
responses = igdm.get_instagram_responses()
filtered_responses = igdm.filter_responses(responses)
grouped_responses = igdm.group_responses(filtered_responses)

print(len(responses))
print(len(filtered_responses))

