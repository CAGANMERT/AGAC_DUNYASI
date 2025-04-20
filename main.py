import discord
from discord.ext import commands
from config import token
from model import get_class

intents = discord.Intents.default()
intents.mesagge_content = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı.")

@bot.command
async def merhaba(ctx):
    print(f"Merhaba ben {bot.user}. Size doğamızda çok önemli bir yeri olan ağaçları tanıtmak için buradayım.")

@bot.command()
async def hangisi(ctx):
        if ctx.message.attachments:
            for attachment in ctx.mesagge.attachments:
                file_name = attachment.filename
                file_url = attachment.url
                await attachment.save(f"./images/{file_name}")
                await ctx.send(f"Fotoğraf, ./images/{file_name} kaydedildi.")
                result = get_class(model_path ='./keras_model.h5', labels_path="./labels.txt", image_path=f"./images/{file_name}")
                await ctx.send()
        else:
            await ctx.send("Dosya gördermezseniz maalesef yanıt veremem.")

async def mese(ctx):
    await ctx.send("Kayıngiller ailesinden olan meşe ağacı 400'ün üstünde türü olan yaprak döken ya da her zaman yeşil olan ağaçlardır. Çok büyüyen ve uzun ömürlü ağaçlardır. Meşe ağacının meyvesi palamuttur. İçindeki pelit maddesi sincap ve alakarga için önemli bir besin kaynağıdır.20 ila 30 m veya daha yükseklikte, gövdesi 2 m çapında, tacı gençlikte konik yaşlandıkça genişleyen bir orman ağacıdır. Yaprak : 6-12 x 3–5 cm boyutundaki 5-9 çiftli loplu yaprakların sinüsleri (boşluk) orta damara kadar uzanır veya ona yakın bir yerde sonlanır. Koyu yeşil yaprakların üzeri pürüzlü ve yıldız tüylüdür.")

async def cam(ctx):
    await ctx.send("Yaprak dökmeyen tek ağaç türü olan çamlar diğer ağaçlar gibi sonbaharda yaprakları taze durur ve yaz kış hep yeşildir. Bir diğer özelliği ise uzun ömürlü ve dayanıklı olmasıdır. Ayrıca iğneleri ve kendi ürünü olan kozalağı bulunur. Dayanıklı yapısı sayesinde her iklimde yaşayabilir. Çoğu çam, yangına uyarlanmıştır, yani yangının tekrarlaması, çamların, çam olmayanların hakimiyetine yol açan orman dizilerinde baskın bir rol sürdürmesine izin verir. Bu yangına adaptasyonun kesin doğası, bazı çamların sık sık düşük yoğunluklu yangınlara tolerans göstermesi ve diğerlerinin, meşcereleri yok eden yangınlara izin veren yüksek yakıt birikimleri üretme eğiliminde olması ve ardından çamların hızla yenilenmesiyle büyük ölçüde değişir. Ateşin seyrek olduğu veya hiç olmadığı habitatlarda, çam ağaçları serpantin çorakları, litosoller veya bataklıklar gibi besin açısından fakir yerlerde bulunma eğilimindedir. Düşük gölge toleransları tipik olarak kapalı bir orman gölgesinin altında büyümeyi engeller. Birçok tür çok kuraklığa toleranslıdır.")

async def ladin(ctx):
    await ctx.send("60 m bazen daha fazla boylanabilen ve 2 m'den fazla çap yapabilen düz ve dolgun gövdeli bir ağaç türüdür. Nemli havaları, derin, havalanma kapasitesi yüksek, nem içeriği fazla, kumlu ve balçık, besince zengin, humuslu serin toprakları sever. Böyle yerlerde çok iyi bir gelişme gösterir.Ladin, dayanıklı kağıt yapmak için birbirine bağlanan uzun ağaç lifleri olduğundan, kağıt yapımında en önemli ağaçlardan biridir. Lifleri ince duvarlıdır ve kuruduktan sonra ince bantlara çöker. Ladinler, kolayca ağartılır olduğundan mekanik hamurlaştırmada kullanılır.")

async def hus(ctx):
    await ctx.send("15-20 m boylanabilen, yazın yeşil, düzgün gövdeli, ağaç veya ağaççıklardır. Gövde kabuğu düzgün veya yırtılmış olarak görülür. Beyaz veya boz esmer renklidir. Dallar ince ve narin kızıl kahve renkli, yapraklar normal olarak dizilmiş, kenarları ince veya kaba dişli ya da lopludur.")

async def sakura(ctx):
    await ctx.send("Sakura kiraz çiçeği, bakımı kolay olan ve birçok yerde yetiştirilebilen bir bitkidir. Meyvesiz bir kiraz ağacıdır ancak görüntüsüyle büyüleyen özel çiçeklere sahiptir. Yaklaşık 8 ile 10 metreye kadar uzayabilen ağacın çiçekleri çok kısa sürede dalından düşer.")

async def akasya(ctx):
    await ctx.send("Akasya ağaçları ılıman iklimlerde kolay yetişen bir bitkidir. Ancak soğuğa ve kuraklığa dayanıklı olduğu için birçok bölgede yetişir. 600'den fazla çeşidi vardır. Baklagiller familyasından bir bitki olup yeşil yapraklıdır. Türüne göre beyaz, kırmızı ya da sarı renkli çiçekler açar.")

bot.run("TOKEN")