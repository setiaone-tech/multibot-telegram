import telebot
import requests
from menu import Menu
from PIL import Image
from io import BytesIO
import datetime
from telebot import util
import random

ses = requests.session()

def log(message):
    user = message.chat.username
    nama_awal = message.chat.first_name
    nama_akhir = message.chat.last_name
    ttd = datetime.datetime.now().strftime('%d-%B-%Y')
    text_log = '{}, {}, {}, {}\n'.format(ttd, user, nama_awal, nama_akhir)
    log_bot = open('log_bot.txt', 'a')
    log_bot.write(text_log)
    log_bot.close()
    

api = "1308184622:AAHXswbVtZaCEe1cKxJ9bmubS-uEdq1ygWs"
apikey = "c575e69107640a760ad21c7f"
bot = telebot.TeleBot(api, threaded = False)
headers = {
        'Cache-Control':'max-age=0'
        }

@bot.message_handler(commands=['start'])
def send_welcome(message):
    log(message)
    bot.reply_to(message, "Ketik /menu untuk melihat full command ya")
    
@bot.message_handler(commands=['menu'])
def send_menu(message):
    log(message)
    chat_id = message.chat.id
    bot.reply_to(message, Menu(), parse_mode='Markdown')
    ran = random.randint(0, 1)
    if ran == 0:
        bot.send_message(chat_id, 'Ingin berdonasi? langsung klik <a href="https://saweria.co/DPNoober">disini</a>', parse_mode='HTML')

@bot.message_handler(commands=['wiki'])
def send_wiki(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/wiki/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_message(chat_id, hasil['result'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")

@bot.message_handler(commands=['brainly'])
def send_brainly(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/brainly/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            teks = ""
            for i in range(len(hasil['result'])):
                teks += str(i+1)+". <b>Judul</b> : "+str(hasil['result'][i]['title'])+"\n<b>Link</b> : "+str(hasil['result'][i]['url'])+"\n\n"
            bot.send_message(chat_id, teks, parse_mode="HTML")
        else:
            bot.send_message(chat_id, "Eror!")
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['lirik'])
def send_lirik(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/lirik/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            split_text = util.split_string(hasil['result'], 3000)
            if len(split_text) > 1:
                for text in split_text:
                    bot.send_message(chat_id, text)
            else:
                bot.send_message(chat_id, hasil['result'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['cuaca'])
def send_cuaca(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/cuaca/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            place = hasil['result']['tempat']
            lati = hasil['result']['latitude']
            longt = hasil['result']['longitude']
            weather = hasil['result']['cuaca']
            wind = hasil['result']['angin']
            desc = hasil['result']['description']
            lembap = hasil['result']['kelembapan']
            sh = hasil['result']['suhu']
            uda = hasil['result']['udara']
            laut = hasil['result']['permukaan_laut']
            bot.send_message(chat_id, "Tempat : {}\nLatitude : {}\nLongtitude : {}\nCuaca : {}\nAngin : {}\nDeskripsi : {}\nKelembapan : {}\nSuhu : {}\nUdara : {}\nPermukaan Laut : {}".format(place, lati, longt, weather, wind, desc, lembap, sh, uda, laut))
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['sholat'])
def send_sholat(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/sholat/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            place = hasil['result']['wilayah']
            date = hasil['result']['tanggal']
            im = hasil['result']['imsak']
            sub = hasil['result']['subuh']
            ter = hasil['result']['terbit']
            dh = hasil['result']['dhuha']
            dz = hasil['result']['dzuhur']
            ash = hasil['result']['ashar']
            mag = hasil['result']['maghrib']
            isy = hasil['result']['isya']
            bot.send_message(chat_id, "Wilayah : {}\nTanggal : {}\nImsak : {}\nSubuh : {}\nTerbit : {}\nDhuha: {}\nDzuhur : {}\nAshar : {}\nMaghrib : {}\nIsya : {}".format(place, date, im, sub, ter, dh, dz, ash, mag, isy))
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['meme'])
def send_meme(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/meme"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_photo(chat_id, hasil['result'])
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['quotes'])
def send_quotes(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/quotes"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_message(chat_id, "Tokoh : {}\n\nQuotes : {}".format(hasil['result']['by'], hasil['result']['quote']))
    else:
        bot.send_message(chat_id, hasil['message'])
    
@bot.message_handler(commands=['artinama'])
def send_artinama(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/artinama/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_message(chat_id, hasil['result'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")

@bot.message_handler(commands=['jodoh'])
def send_jodoh(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/jodoh/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_photo(chat_id, hasil['result']['image'], "Positif : "+hasil['result']['positif']+"\n\nNegatif : "+hasil['result']['negatif']+"\n\nKeterangan : "+hasil['result']['deskripsi'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")

@bot.message_handler(commands=['weton'])
def send_weton(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",3)
        url = "http://lolhuman.herokuapp.com/api/weton/"+cari[1]+"/"+cari[2]+"/"+cari[3]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_message(chat_id, "Weton : {}\n\nKarakter : {}\n\nPekerjaan : {}\n\nRejeki : {}\n\nJodoh : {}".format(hasil['result']['weton'], hasil['result']['karakter'], hasil['result']['pekerjaan'], hasil['result']['rejeki'], hasil['result']['jodoh']))
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['jadian'])
def send_jadian(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",3)
        url = "http://lolhuman.herokuapp.com/api/jadian/"+cari[1]+"/"+cari[2]+"/"+cari[3]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_message(chat_id, "Karakteristik : {}\n\nKeterangan : {}".format(hasil['result']['karakteristik'], hasil['result']['deskripsi']))
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['quotenime'])
def send_quotenime(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/quotesnime"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_message(chat_id, "Quotes : {}\n\nKarakter : {}\n\nJudul : {}".format(hasil['result']['quote'], hasil['result']['character'], hasil['result']['anime']))
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['faktaunik'])
def send_faktaunik(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/faktaunik"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_message(chat_id, "Faktanyaa {}".format(hasil['result']))
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['bijak'])
def send_bijak(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/katabijak"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_message(chat_id, "{}".format(hasil['result']))
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['pantun'])
def send_pantun(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/pantun"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_message(chat_id, "{}".format(hasil['result']))
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['bucin'])
def send_bucin(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/bucin"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_message(chat_id, "{}".format(hasil['result']))
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['bucinn'])
def send_bucinn(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/katabucin"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_message(chat_id, "{}".format(hasil['result']))
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['twt'])
def send_twt(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/twitter?url="+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_video(chat_id, hasil['result'][1]['link'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['wancak'])
def send_wancak(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    url = "http://lolhuman.herokuapp.com/api/onecak"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers)
    if type(hasil.content) == bytes:
        im = Image.open(BytesIO(hasil.content))
        im.save("onecak/"+nam+"wancak.png")
        photo = open("onecak/"+nam+'wancak.png', 'rb')
        bot.send_photo(chat_id, photo)
    else:
        send_message(chat_id, "Error!")
    
@bot.message_handler(commands=['bts'])
def send_bts(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/bts"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_photo(chat_id, hasil['result'])
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['exo'])
def send_exo(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/exo"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_photo(chat_id, hasil['result'])
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['blackpink'])
def send_blackpink(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/blackpink"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_photo(chat_id, hasil['result'])
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['animefanart'])
def send_animefn(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/art"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_photo(chat_id, hasil['result'])
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['wpanime'])
def send_wpanime(message):
    chat_id = message.chat.id
    url = "http://lolhuman.herokuapp.com/api/random/wallnime"+"?apikey="+apikey
    hasil = ses.get(url, headers=headers).json()
    if hasil['status'] == 200:
        bot.send_photo(chat_id, hasil['result'])
    else:
        bot.send_message(chat_id, hasil['message'])
        
@bot.message_handler(commands=['wpsearch'])
def send_wpsearch(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/wallpaper/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_photo(chat_id, hasil['result'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['pinterest'])
def send_pinterest(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/pinterest/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_photo(chat_id, hasil['result'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['phub'])
def send_phub(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/pornhub/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("phub/"+nam+"ph.png")
            photo = open("phub/"+nam+"ph.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")

@bot.message_handler(commands=['glitch'])
def send_glitch(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/glitch/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("glitch/"+nam+"gl.png")
            photo = open("glitch/"+nam+"gl.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
    
@bot.message_handler(commands=['avenger'])
def send_avenger(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/avenger/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("avenger/"+nam+"av.png")
            photo = open("avenger/"+nam+"av.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
    
@bot.message_handler(commands=['space'])
def send_space(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/space/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("space/"+nam+"sp.png")
            photo = open("space/"+nam+"sp.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
    
@bot.message_handler(commands=['ninja'])
def send_ninja(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/ninjalogo/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("ninja/"+nam+"nj.png")
            photo = open("ninja/"+nam+"nj.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
    
@bot.message_handler(commands=['marvel'])
def send_marvel(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/marvelstudio/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("marvel/"+nam+"mvl.png")
            photo = open("marvel/"+nam+"mvl.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
    
@bot.message_handler(commands=['lion'])
def send_lion(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/lionlogo/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("lion/"+nam+"lion.png")
            photo = open("lion/"+nam+"lion.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
    
@bot.message_handler(commands=['wolf'])
def send_wolf(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/wolflogo/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("wolf/"+nam+"wolf.png")
            photo = open("wolf/"+nam+"wolf.png", 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
    
@bot.message_handler(commands=['steel3d'])
def send_steel3d(message):
    chat_id = message.chat.id
    nam = message.chat.first_name
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",2)
        url = "http://lolhuman.herokuapp.com/api/textprome/steel3d/"+cari[1]+"/"+cari[2]+"?apikey="+apikey
        hasil = ses.get(url).content
        with Image.open(BytesIO(hasil)) as im:
            im.save("steel/"+nam+"steel.png")
            photo = open('steel/'+nam+'steel.png', 'rb')
            bot.send_photo(chat_id, photo)
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['ytaudio'])
def send_ytaudio(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/ytaudio/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            judul = hasil['title']
            audio = ses.get(hasil['result'][1]['link']).content
            bit = hasil['result'][1]['bitrate']
            ukuran = hasil['result'][1]['size']
            bot.send_audio(chat_id, audio, 'Judul : '+judul+'\nBit : '+bit+'\nUkuran : '+ukuran)
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['ytvideo'])
def send_ytvideo(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/ytvideo/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            judul = hasil['title']
            video = ses.get(hasil['result'][0]['link']).content
            resolusi = hasil['result'][0]['resolution']
            ukuran = hasil['result'][0]['size']
            bot.send_video(chat_id, video)
            bot.send_message(chat_id, 'Judul : '+judul+'\nResolusi : '+resolusi+'\nUkuran : '+ukuran)
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['joox'])
def send_joox(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/joox/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            penyanyi = hasil['result']['info']['singer']
            judul = hasil['result']['info']['song']
            album = hasil['result']['info']['album']
            rilis = hasil['result']['info']['date']
            bot.send_photo(chat_id, hasil['result']['image'], 'Penyanyi : '+penyanyi+'\nJudul : '+judul+'\nAlbum : '+album+'\nRilis : '+rilis)
            bot.send_audio(chat_id, hasil['result']['audio']['192'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['ig'])
def send_ig(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/instagram?url="+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_video(chat_id, hasil['result'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['soundcloud'])
def send_soundcloud(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/soundcloud?url="+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            bot.send_audio(chat_id, hasil['result'], hasil['title'])
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['tiktokmp4'])
def send_tiktokmp4(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/tiktok?url="+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            judul = hasil['result']['title']
            desc = hasil['result']['description']
            up = hasil['result']['uploader']
            bot.send_video(chat_id, hasil['result']['link'])
            bot.send_message(chat_id, "Judul : "+judul+"\nDesc : "+desc+"\nUploader : "+up)
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['stalktiktok'])
def send_tiktok(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/stalktiktok/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            user = hasil['result']['username']
            nick = hasil['result']['nickname']
            bio = hasil['result']['bio']
            foll = hasil['result']['followers']
            back = hasil['result']['followings']
            likes = hasil['result']['likes']
            video = hasil['result']['video']
            bot.send_photo(chat_id, hasil['result']['user_picture'], "Username : "+user+"\nNickname : "+nick+"\nBio : "+bio+"\nPengikut : "+str(foll)+"\nMengikuti : "+str(back)+"\nLikes : "+str(likes)+"\nVideo : "+str(video))
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")

@bot.message_handler(commands=['stalkig'])
def send_stalkig(message):
    chat_id = message.chat.id
    bagi = message.text
    if " " in bagi:
        cari = bagi.split(" ",1)
        url = "http://lolhuman.herokuapp.com/api/stalkig/"+cari[1]+"?apikey="+apikey
        hasil = ses.get(url).json()
        if hasil['status'] == 200:
            user = hasil['result']['username']
            nick = hasil['result']['fullname']
            bio = hasil['result']['bio']
            foll = hasil['result']['followers']
            back = hasil['result']['following']
            post = hasil['result']['posts']
            bot.send_photo(chat_id, hasil['result']['photo_profile'], "Username : "+user+"\nFullname : "+nick+"\nBio : "+bio+"\nPengikut : "+str(foll)+"\nMengikuti : "+str(back)+"\nPost : "+str(post))
        else:
            bot.send_message(chat_id, hasil['message'])
    else:
        bot.send_message(chat_id, "Perintah salah! Harap gunakan spasi!")
        
@bot.message_handler(commands=['komen'])
def send_komen(message):
    chat_id = message.chat.id
    me = 617998203
    user = message.chat.username
    bagi = message.text
    hasil = bagi.split(" ",1)
    bot.send_message(me, "ID : "+str(chat_id)+"\nUsername : "+user+"\nKomen : "+hasil[1])
    
@bot.message_handler(commands=['balas'])
def send_balas(message):
    bagi = message.text
    hasil = bagi.split(" ",2)
    you = hasil[1]
    pesan = hasil[2]
    bot.send_message(you, pesan)

while True:
    try:
        print(str(datetime.datetime.now().hour)+'.'+str(datetime.datetime.now().minute)+' ==> Bot Running....')
        bot.polling()
    except:
        bot.stop_polling()
