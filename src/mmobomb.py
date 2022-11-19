from requests import get

class MMOBomb:
	def __init__(self) -> None:
		self.api = "https://www.mmobomb.com/api1"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
		}
	
	def get_games(self) -> dict:
		return get(
			f"{self.api}/games",
			headers=self.headers).json()
	
	def get_games_by_platform(
			self,
			platform: str = "pc") -> dict:
		return get(
			f"{self.api}/games?platform={platform}",
			headers=self.headers).json()
	
	def get_games_by_category(
			self,
			category: str) -> dict:
		return get(
			f"{self.api}/games?category={category}",
			headers=self.headers).json()
	
	def get_games_by_tag(self, tag: str) -> dict:
		return get(
			f"{self.api}/games?tag={tag}",
			headers=self.headers).json()
	
	def sort_games(self, sort: str) -> dict:
		return get(
			f"{self.api}/games?sort-by={sort}",
			headers=self.headers).json()
	
	def get_games_by_all(
			self,
			platform: str = "browser",
			category: str = "mmorpg",
			sort: str = "release-date") -> dict:
		return get(
			f"{self.api}/games?platform={platform}&category={category}&sort-by={sort}",
			headers=self.headers).json()
	
	def filter_games(
			self,
			platform: str = "pc",
			tag: str = "3d.mmorpg.fantasy.pvp") -> dict:
		return get(
			f"{self.api}/filter?tag={tag}&platform={platform}",
			headers=self.headers).json()
		
	def get_game_details(self, game_id: int) -> dict:
		return get(
			f"{self.api}/game?id={game_id}",
			headers=self.headers).json()
	
	def get_mmo_giveaways(self) -> dict:
		return get(
			f"{self.api}/giveaways",
			headers=self.headers).json()
	
	def get_latest_mmo_news(self) -> dict:
		return get(
			f"{self.api}/latestnews",
			headers=self.headers).json()
