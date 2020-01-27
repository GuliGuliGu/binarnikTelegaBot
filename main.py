import telebot
import re
from telebot import types
#import json


bot = telebot.TeleBot("1019818960:AAFX1QGKzAQm6JZIQPJXT6rGyPviau_9sZQ")

print("started")
icon = "https://cdn4.iconfinder.com/data/icons/messenger-1-0-line/106/Send_Line-512.png"
beerico = "https://image.flaticon.com/icons/png/512/110/110181.png"
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(inline_query):
	#print(" All: \n" + str(inline_query))
	#print(inline_query.from_user.username)
	#print(inline_query.query)
	if inline_query.query == "beer":
 		r = types.InlineQueryResultArticle(id = '1', title = 'Beer time', description = inline_query.from_user.username + " wanna to send beer", input_message_content = types.InputTextMessageContent(message_text= inline_query.from_user.username + " send some beer for someone. Take it please 🍺"), thumb_url=beerico, thumb_width=48, thumb_height=48)
		
	else:
	    try:
	        #r = types.InlineQueryResultArticle(id = '1', title = 'Result', description = "Я " + inline_query.from_user.username + " " + inline_query.query, input_message_content=types.InputTextMessageContent(message_text= "Я " + inline_query.from_user.username + " " + inline_query.query))
	        r = types.InlineQueryResultArticle(id = '1',  title = 'Something like this:', description = text_to_bits(inline_query.query), input_message_content=types.InputTextMessageContent(message_text=text_to_bits(inline_query.query)), thumb_url=icon, thumb_width=48, thumb_height=48)
	        if inline_query.from_user.username == "Ultiis":
        		r = types.InlineQueryResultArticle(id = '1', title = 'Something like this:', description = text_to_bits(inline_query.query), input_message_content=types.InputTextMessageContent(message_text = "ко-ко-ко-ко-КО!"))
	        

	        
	        #arr = json.loads(inline_query)
	        
	        #print("Really all( \n" + str(inline_query.__dict__))
	    except Exception as e:
	        print(e)
	        print(" All: \n" + str(inline_query))
	bot.answer_inline_query(inline_query.id, [r])
        






def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    try:
    	return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) 
    except Exception as e:
     	return "Something wrong"




@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.text == "beer" or message.text == "пива" or message.text == "пиво" or message.text == "Пива" or message.text == "Beer" or message.text == "Пиво":
    	bot.send_message(message.chat.id, "Here is your beer") 
    	bot.send_message(message.chat.id, "🍺")  
    else:
    	try:
    		bot.send_message(message.chat.id, text_from_bits(message.text)) 
    	except Exception as e:
    		bot.send_message(message.chat.id, "I'm so sorry, but you sent me some shit") 






#if __name__ == '__main__':
bot.polling()






input("Press enter to exit ;)")




#







#bot.polling ()





