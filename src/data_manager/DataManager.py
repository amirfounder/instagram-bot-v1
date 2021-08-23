from src.data_manager.domains.InstagramDataManager import InstagramDataManager


class DataManager:

  def __init__(self) -> None:
    self.instagram_data_manager = InstagramDataManager()
  
  @classmethod
  def run(self):
    self.manage_instagram_data()

  def manage_instagram_data(self):
    self.instagram_data_manager
