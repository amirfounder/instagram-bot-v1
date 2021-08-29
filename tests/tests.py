import sys
sys.path.append('C:\\Users\\Amir Sharapov\\Code\\amirfounder\\programs\\1')


from src.data_manager.domains.InstagramDataManager import InstagramDataManager


# Tests and sandbox mode here.

igdm = InstagramDataManager()
igdm.get_responses_from_file()