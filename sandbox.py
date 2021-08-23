from src.data_manager.domains.InstagramDataManager import InstagramDataManager

igdm = InstagramDataManager()
responses = igdm.get_instagram_responses()
for response in responses:
  print(response)