"""
	Made by Xsarz (@DXsarz)
	GitHub: https://github.com/xXxCLOTIxXx
	Telegram channel: https://t.me/DxsarzUnion
	YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q]

"""
import lib
from colored import fore, style
from threading import Thread
from json import load
from time import sleep as s
client = lib.Client()
communities = []


try:
	message = open("message.txt", encoding='utf-8').read()
	print('Piar message:\n', fore.WHITE, message, fore.PURPLE_3,'\n\n')
except Exception as error:print(fore.RED, error, fore.PURPLE_3); exit()
s(1)
try:
	for i in open("communities.txt", "r"):
		try:
			com = client.get_from_link(i)["linkInfoV2"]["extensions"]["community"]
			name = com["name"]
			id = com["ndcId"]
			communities.append(id)
			print(fore.GREEN, f'{name} added to the list of communities for advertising', fore.PURPLE_3)
		except Exception as error:print(fore.RED, error)
except Exception as error:print(fore.RED, error, fore.PURPLE_3); exit()

try:
	with open("accounts.json", "r") as file:
		accounts = load(file)
		print(fore.GREEN, f"{len(accounts)} accounts loaded", fore.PURPLE_3)
except Exception as error:print(fore.RED, error); exit()

def start_piar(client, comId, gmail, chats):
	try:client.edit_profile(comId=comId, name="Xsarz-piar-bot V1 (Бесплатные скрипты -> @DXsarz)", content=open("antiban.txt", encoding='utf-8').read())
	except Exception as error:print(error);print(fore.RED, f"\n{gmail}: Failed to change profile name and description\n", fore.PURPLE_3)
	try:
		for i in range(len(chats)):
			try:
				client.join_chat_web(chatId=chats[i], comId=comId)
				client.send_message(chatId=chats[i], comId=comId, message=message); print(fore.GREEN, f"\n{gmail}: Successful send piar message\n", fore.PURPLE_3)
			except Exception as error:print(fore.RED, f'{gmail}: Fail:\n',error, fore.PURPLE_3)
	except Exception as error:print(fore.RED, f'{gmail}: Fatal error:\n',error, fore.PURPLE_3)

def login_bots(account):
	try:
		bot_client = lib.Client()
		gmail = account['email']
		password = account['password']
		bot_client.login(email=gmail, password=password); print(fore.GREEN, f"\n{gmail}: Successful login\n", fore.PURPLE_3)
		joined_community = []
		for i in range(len(communities)):
			try: 
				bot_client.join_community(comId=communities[i]); print(fore.GREEN, f"\n{gmail}: Successful join community\n", fore.PURPLE_3)
			except:print(fore.RED, f'{gmail}: Unable to join the community\n', fore.PURPLE_3)
			chats = []
			try:
				for chats_ in client.get_public_chat_threads(size=100, comId=communities[i]):
					chats.append(chats_['threadId'])
			except Exception as error:print(fore.RED, f'{gmail}: Failed to receive chat:\n',error, fore.PURPLE_3)
			Thread(target=start_piar, args=(bot_client, communities[i], gmail, chats)).start()
	except Exception as error:print(fore.RED, f'{gmail}: This account has been stopped, error:\n',error, fore.PURPLE_3)
for i in range(len(accounts)):
	Thread(target=login_bots, args=(accounts[i],)).start()