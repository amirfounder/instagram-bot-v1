from src.file_to_database_manager.domains.InstagramFileToDataManager import InstagramFileToDataManager

igdm = InstagramFileToDataManager()
responses = igdm.get_instagram_responses()
for response in responses:
  print(response)