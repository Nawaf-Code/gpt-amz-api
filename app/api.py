from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from bs4 import BeautifulSoup

import requests

app = FastAPI()

class ProductReviewLink(BaseModel):
    url: str

@app.post("/analyze-reviews")
async def analyze_reviews(product: ProductReviewLink):
    try:
        demo_rev = [
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nافضل سماعة اشتريتها نسبة العزل فيها ممتاز جودة الصوت ممتازة مريحة في اللبس وسعرها ممتاز\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالسماعة رائعة وجودة الصوت والعزل فوق المتوقع..\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nالسلبيات: الصوت مكتوم لكن ممكن تعديله من البرنامج الخاص السماعه مزعجه لو الجو حار اذنك هاتتعرقالمايك مش احسن حاجه كمان لايوجد زر لتشغيلايجابيات : عزل الضوضاء عالم تانىالصوت مجسم رائعمريحه للاذن فترات طويلهالبطاريه اسبوع مع تفعيل عازل الضوضاءجوده تصنيع ممتازه يجى معاها حافظه شيك للسماعهاسم برنامج التشغيلsoundcore\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nسماعة ممتازة سعرها عند جرير غالي وعند امازون رخيص يفرق 50 ريال او اكثر\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالسماعة خفيفه ومريحه وصوتها صافي والعزل بالمقارنه بسعرها ممتاز انصحكم فيها وبقوه\n"
        },
        {
            "rating": "3.0 ",
            "title": None,
            "content": "\nبشكل عام جميلة جداالعزل روعة والشفافية حلوةبس فيه ملاحظة لما تشغل العزل ومافي شيء شغال بالسماعة يسبب ضغط على السمع بالنسبة للصوت مزعج احيانابالنسبة للراحة مريحة\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nسماعة مميزة ومريحة وميزة الغاء الازعاج شغال\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nعزل الصوت فيها ممتاز و الصوت جدا واضحمريحه اثناء الاستخدام و خفيفه\n"
        },
        {
            "rating": "5.0 ",
            "title": "Fantastic headphones at this price range.",
            "content": "\nI'm not really a sound expert, so as many of you can certainly relate, I usually skip parts where the person doing a headphone review talks about the bass and sound quality. However, even to my inexperienced ears, this was paradise. The headphones sound quality shone through, and I found myself dropping my hyperx cloud II headphones (which are 5 times the price) whenever I am not gaming. Sound never escapes the headphones, which is a great plus whenever you really wanna jam on max audio. I tried to maximise the audio output and stood next to someone I knew, and he confirmed he heard nothing.The headphones are also very comfortable, and I almost always forget their presence. They are very light and rest well on the head. The size changing mechanism is very practical and ergonomic.I got this at a deal for around 50$, which was an absolute bargain. I debated splurging and going for the soundcore space ones, but I really don't think I need something better than this one.The control buttons are very practical and easy-to-use. The design is also very sleek and of high build quality. The ANC switch can be a little annoying to deal with since sometimes you just keep holding it with your hand while trying to reach the other buttons, but it is a minor inconvenience.Speaking of the ANC, the ANC allows little to no audio through, and the transparency mode even amplifies the surrounding voices in a way that didn’t feel noisy.All in all, it's a great purchase and one that I'm sure most people who are looking for bluetooth headphones would not regret. Sound experts could find faults with this headphone, but I honestly think the majority of people wouldn't.\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nعزل الصوت ممتاز و عند الشحن تجلس فترات طويله وما احتاج اشحنها كثير\n"
        },
        {
            "rating": "5.0 ",
            "title": "Powerful and Amazing Sound",
            "content": "\nVery high quality, Sound is amazing especially the deep bass, ling battery life\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nمن أفضل السماعات الي جربتها عزل وراحة وسعر وكمية شحن لدرجة عادي بالاسبوع مره فقط ما تناسب الجيم بسبب انزلاقها من الراس بسبب نعومتها لكن الباقي 10/10\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nجيد\n"
        },
        {
            "rating": "5.0 ",
            "title": "Long lasting battery im using it for four days now and it’s still high",
            "content": "\nThe noise cancellation is on point you cant hear anybody around you\n"
        },
        {
            "rating": "5.0 ",
            "title": "Just perfect",
            "content": "\nJust perfect\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتازة عزل ممتاز للأستخدام مريحه للأذن\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nصوتها عالي العزل تمام وتشتغل مع الايفون تمام انصح بيها 👍🏼\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nماشاء الله جودة صوت وعزل فخم\n"
        },
        {
            "rating": "5.0 ",
            "title": "Price",
            "content": "\nIf you wear glasses, i will suggest you to try it out first before buying it but in this price range this is a very very good product\n"
        },
        {
            "rating": "4.0 ",
            "title": "Best Value for Money imo",
            "content": "\nFirst of all, these headphones are considered to be one of the best value-for-money options out there. Here are the advantages and disadvantages:1. The sound quality is acceptable, but you need to choose the right equalizer mode that suits the type of content you're listening to, such as music, movies, or YouTube videos.2. The Soundcore app provides a very smooth experience with a clean and easy-to-use interface. Bluetooth pairing is quick, but for some reason, NFC pairing didn't work for me.3. The headphone pads are comfortable and won't cause discomfort unless you wear them for a long period of time.4. The quality of materials used is the weakest aspect of these headphones. They feel okay in your hands, but there are some unsettling finishing sounds. Considering the price, it's understandable, but I feel like they could fall apart at any moment due to the weak and cheap plastic.5. I didn't like the default equalizer settings in the Soundcore app, but once you customize your own, the experience becomes significantly better, in my opinion.6. The noise cancellation is good if you prefer it, and you can quickly switch between two noise cancellation modes. Indoor noise cancellation is quite effective, but you might need some time to get used to the pressure sensation, similar to being on a plane.7. The headphone case is solid and made of good material, providing excellent protection for the headphones.Overall, it's a good choice if you're looking for a budget noise-canceling option with good sound quality, a user-friendly app, and a long-lasting battery. The only downsides are the cheap feel of the materials used and the short length of the Type-C USB cable.\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nاشكر البائع على سرعة الشحن من افضل السماعات اللي جربتها للعزل والسعر بطل\n"
        },
        {
            "rating": "4.0 ",
            "title": "The Quality of the sound is so good.",
            "content": "\nThe only problem with this, is that if you are outside and the wind is strong, the whistling of the wind is disturbing because you can heard the  wind clairly, even with noise canceling on. onestly, it's not like the first time I bought the TOSHIBA brand, even if the wind is strong, you won't really notice that there is a strong wind. But when it comes to the sound quality, Yes.., I love it..😘 and lastly, the of this design of this  headphone is very cute, lovely and  admirable.Thank you so mush...😘🙋‍♂️NOT BAD.\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nالسماعة صوتها خرافي والعزل حلو على سعرها\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nاعجبتني واخذتها بناءا على التعليقات الايجايية وفعلا كان فيه مصداقيةوحتى سعرها ممتاز جداًصرلها معي تقريبا اسبوع وكم يوم ✔️\n"
        },
        {
            "rating": "5.0 ",
            "title": "Great product",
            "content": "\nI liked the product and price\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nحلوه\n"
        },
        {
            "rating": "5.0 ",
            "title": "Hmmmm",
            "content": "\nNice very good item\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nاحسن سماعات جربته من نحيت البيس من نحيت الوضوح لاكن المايك حقها ردي اي هواء لو بسيط يخرب الي تكلمه بينزعج فا إذ بتشتري لاتشتري علشان المكالمات\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nالمنتج ممتاز مقارنة بالسعر\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nقوية بتعجبكم 👍😍\n"
        },
        {
            "rating": "5.0 ",
            "title": "Best at it’s price",
            "content": "\nI really recommend for this price it’s got almost every feature u need the noise cancellation is great the mic is decent not that bad overall it’s great value\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتاز انصح به شريته بالعرض بسعر179\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nاستخدمها لي شهر تقريبا بالنادي واحيانا بالبيتالايجابيات : البطارية ( احط العزل دائما ومع استخدام ساعتين يوميا تقريبا تقعد اكثر من اسبوع ) بالضبط ماادري لكن تطول مره.الصوت: جيد جداالعزل : مايعزلك تماما لكن عزلها كويس مثلا :(بالنادي يشغلون موسيقى وانا اكون حاط السماعه على العزل اسمعها لكن ضعيف واذا شغلت شي بالسماعه تصير اقل الموسيقى )الاتصال بالبلوتوث سرييييع جداالعيوب :اذا حطيت السماعه وماهو شغال شي احيانا قليله اسمع صفير بإذني اليسار ، يمكن لاني استخدم سماعه ثانيه داخل الاذن ( استخدمها عند النوم)\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nفيه ٣ مستويات للعزل اخر مستوى قارنته مع سماعه سوني مقاربه جدا لها من ناحيه العزل والصوت والشحنعلى سعرها ممتازه جدا\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nسنه بعدين انكسرت ما تنفع للتمارين ابدا كبير وزنها مره مره لكن العزل وكل شي مره تمام على سعرها حلوه مره وانكسرت بعد سنه بس كسر بسيط باقي استخدمها وكل شي تمام\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nمنتج جيد و وسهل في الاقتران مع التليفونالمايك سيء و لا يمكن التحدث من خلاله بوضوح أبدا\n"
        },
        {
            "rating": "5.0 ",
            "title": "👍🏻",
            "content": "\n👍🏻\n"
        },
        {
            "rating": "5.0 ",
            "title": "good headset",
            "content": "\nGreat quality once compared with Price.\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتازه جدا وحلوه\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالعزل ماشاء الله شي اسطوري\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالمنتج وفى احتياجي بشكل كامل العزل حلو السماعه خفيفه وما تقل على الراس و مرنه و البطاريه ما تخلص بسرعه بس لو فيها زر تحكم للمايك عشان القيمنق\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nجدا سماعة ممتازة في جميع خدماتها عدا وزنها جدا خفيف لدرجة مايثبت بالرأس\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nكنت متخوف منها من تجارب سابقة و لكن بعد قراءت المراجعات قمت بالشراء و لم اندم و اعتبرها استثمار ناجح تقدر انك توصل عليها اكثر من جهاز و التطبيق للجوال ممتاز و سهل الاستخدامو السعر جدا مناسب 179 على الجودة التي تتمتع به السماعة\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالعزل ممتاز وضوح الصوت مقارنه بالسعر جيد جدا\n"
        },
        {
            "rating": "5.0 ",
            "title": "Recommend",
            "content": "\nGreat battery & transparencyI would recommend it to anyone\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nعزلها ممتاز وجيد وبطاريتها ما تنفذ بسرعه وتجي نفس الشكل بالضبط / محتوياتها : سماعة ، سلك للشحن ، بوكس للسماعة في حال الحفظ او في حال السفر وما تبيها تنكسر ، تعليمات .تشحن بسرعه وتقعد معك بالأيام ، لهم تطبيق خاص تقدر تتحكم بدرجات العزل وقوة الصوت اسمه نفس اسم شركة السماعة واخيرًا سعرها مناسب جدًا ومرات يكون عليها خصومات لذلك أستغلوها\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nجيد جيدا\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nاشتريت 2 و هاذي الثالثة\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nسعرها مناسب لأدائها\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nكجودة اشوف سعر مناسب لكن الغريب هو لمن استخدمه على جوال في صوت \"تش\" يطلع خصوصا لمن اكون على السناب .. عموما انا راضي ومايتكرر كثير الا في ظروف غريبة وانا متاكد انها مشكلة بنظام السماعات\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nمقابل سعرها ومميزاتها تستاهل كل ريال فيها .. اشتريتها وقت التخفيضانصح فيها تذكر ( مقابل سعرها )لا تدور على مواصفات عالية وسعر رخيص\n"
        },
        {
            "rating": "5.0 ",
            "title": "A Great Buy !",
            "content": "\nI am more of an earbuds person and what made me switch to headphone is because I am looking for longer battery life, especially during long travel.In the realm of mid-range headphones, the Anker Soundcore Life Q30 Hybrid ANC Headphones stand out as a remarkable choice.What I like about this headphone:1. Comfort: Over-the-ear cups with plush foams fit perfectly and doesn't hurt my ears after using it for a long time.2. Controls/Connectivity: Easy to understand and operate. I get used to it pretty quickly.3. Battery:  The best battery life for mid-range headphone!4. Price: Truly a great value for money5. Audio Quality: for a casual listener like me I would say that the audio quality is okay not that impressive but it's already acceptable for me and it has an app where you can play with the equalizers to suit your listening mood.6. ANC: You can still hear a little bit of outside sounds especially car sounds even when you're on ANC mode,  but it filters just fine. It is not something that will trouble you that much.Overall, this headphone is a great buy!\n"
        },
        {
            "rating": "5.0 ",
            "title": "Nice Experience",
            "content": "\nThe sound quality is perfect and the headphones options are to the point.\n"
        },
        {
            "rating": "5.0 ",
            "title": "Headphone",
            "content": "\nAll done\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nعلزها ممتاز وصوتها ممتاز لاكن عيبها واحد صوتها منخفض شوي خاصة اني احب الأغاني الصاخبة\n"
        },
        {
            "rating": "4.0 ",
            "title": "Good quality",
            "content": "\nThing is, it's buffin the sound, it doesn't give u the real sound\n"
        },
        {
            "rating": "5.0 ",
            "title": "رهيب على هالسعر",
            "content": "\n.\n"
        },
        {
            "rating": "5.0 ",
            "title": "Good headphone for the price range..",
            "content": "\nThe headphone weight is perfect. Sound is also good, ANC is average. over all the product is good.\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nصوت حلو والعزل جيد جدا وتقدر تشغلها على السوني  ممتازه جدا\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nسماعة جودة عالية\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتازه انصح فيها اصليه\n"
        },
        {
            "rating": "5.0 ",
            "title": "Superb",
            "content": "\nCheap and quality.. worth every bucks you spent\n"
        },
        {
            "rating": "5.0 ",
            "title": "ممتازه وملحقاتها ممتازه",
            "content": "\n👍🏻👍🏻👍🏻\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nسعرها ممتاز وعزلها رهيب\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nزين\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالسماعة ممتازه من كل النواحي الصوت و العزل فيها ممتاز و مدة شحن السماعة انا اشحنها فل و استخدمها كل يوم تقعد معاي اسبوع و اكثر احيانا\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nالنظاره تضعف مع الوقت يعني الجلد مع الاستخدام الطويل بيبدء يتقطع و البلاستيك نوعه سيئ يطلع اصوات, العزل و الصوت جدا رهيب ولاكن الجلد و البلاستيك سيئ\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nبعد التجربه عزل الصوت وصفاووه ممتاز جدا\n"
        },
        {
            "rating": "5.0 ",
            "title": "👍",
            "content": "\n👍\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتازة وجباااارة خذها وانت مغمض للموسيقى صوت ولا اروع والعزل رهييييب وسعرها ممتاز على المواصفات الي تقدمها السماعة 👍🏻\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالصوت جداً ممتاز وفعلا Hi-Res لكن فيها مشكلة بسيطه مشكلة العزل\n"
        },
        {
            "rating": "5.0 ",
            "title": "Very good",
            "content": "\nOriginal headphone\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nثقيله بنسبه لي على الرأس ماقدر احطها فترات طويله ، لكنها ممتازة من ناحية الشحن تتطول معاك كم يوم و الصوت ممتاز\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nالصوت فيه رائع وكذلك العزل جيد\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nسعره مقابل الجوده جدا ممتاز\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nوضوح الصوت والعزل ممتازالتوصيل سريع\n"
        },
        {
            "rating": "4.0 ",
            "title": "Excellent value for money headphones",
            "content": "\nAn excellent, well made set of headphones, easy to use and comfortable. Noise cancelling could be a wee bit better, hence 4*s\n"
        },
        {
            "rating": "4.0 ",
            "title": "سماعة",
            "content": "\nانصح فيها\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nممتازه بس ماتدعم البلايستيشن\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nعمليه جدا شريته عشان الجامعة وافضل سماعه لا سلكيه مرت علي يوجد وضع العزل على ٣ مستويات والشحن يدوم لفتره طويله وحتى لو عليت الصوت مايطلع من السماعه وفيه ازرار على اليمين تطويل وتخفيض الصوت ويجي معه شنطه والشاحن ووصله تنشبك بالاجهزه مثل يد البلاستيشن وفيه وضع حساس على جوانب السماعه يمديك تتحكم بوضع العزل والسعر جيد مقارنه بالجوده\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتاز وسعر روعهممكن كمل معايا عشر شهور او سنه ماعرف بس ممتاز ماسمع احد ابدا عزل ممتاز وصوت روعه وشحن فوق الممتاز يستمر لساعات وايام طويله جدا\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتازة جدا والتغليف رائع\n"
        },
        {
            "rating": "5.0 ",
            "title": "As described",
            "content": "\nAs described, good value for price\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nجميلة و لا بأس تؤدي الغرض و سعرها رائع\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nجميله الصوت جبار واهم شي الشحن يطول بس اذا رفعت الصوت يسمعونه الي حولك اذا هدوء\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nموب افضل شي لكن مقابل القيمة رهيبة\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nتفوق قيمتها بمراحل وتتفوق على كثير من السماعات الغالية واخي لديه سماعة سوني قيمتها فوق الألف ريال وجرب هذه السماعة وقال انها ربما تضاهي سماعته كعزل وجودة ✋🏻\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالصراحه حلوه مره حتى سعره مناسب\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nرهيبههههههه\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nسعر مقبول جدا مقابل الجودة و  عزل الإزعاج الخارجي قوي\n"
        },
        {
            "rating": "3.0 ",
            "title": "It's not durable and could snap quickly",
            "content": "\nSound quality/Bass and the NC are great for a budget price BUT the built material is fragile and could break quickly if your not careful enough\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nممتازة\n"
        },
        {
            "rating": "5.0 ",
            "title": None,
            "content": "\nالسماعه كويسه اخذتها ب١٨٠ ممتازه على سعرها ذا\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nحلو سعرها بس ترا تعرق كثير\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nالسماعه قوية العزل ٧٠٪؜لكن فيها عيب قاتل واكثر شي ازعجني لما اعلي الصوت اللي حولي يسمعون لازم تخفض الصوت لنسبة معينه وهذا شي ما حبيته لكن باقي المواصفات مقارنة بالسعر قوية\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nكل شي فيها كويس معاد العزل اللي جنبي يسمعون\n"
        },
        {
            "rating": "3.0 ",
            "title": None,
            "content": "\nالعزل ممتاز الاقتران ممتاز مريحة في الاذن خفيفة لكن لقيت فيها خلل في السماعة اليسار لما اتحرك فيه تشويش يمكن خلل في الناقل وشكرا\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nحجمها كبير وماهي مريحه لأنها تضغط على الراس بقوه\n"
        },
        {
            "rating": "4.0 ",
            "title": None,
            "content": "\nكا اول استخدام مررره جميلبس عيبها اللى جنبك يسمع وش مشغل 😐\n"
        },
        {
            "rating": "5.0 ",
            "title": "Brings Peace To My Ears",
            "content": "\nIn a world saturated with noise, the Anker Soundcore Life Q30 emerges as a sanctuary for your ears. Its cutting-edge noise cancellation effectively blocks out distractions, allowing you to immerse yourself fully in your music or focus on work without interruptions.The Life Q30's sound quality is equally impressive, delivering high-resolution audio through its 40mm drivers. From the deep, rumbling bass to the crisp, clear treble, every note comes alive, transporting you to a world of pure auditory bliss.. 🤤🎧\n"
        }
    ]
        #reviews = get_reviews(product.url)
        return {"reviews": demo_rev}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def convert_review_link(original_url, page_number):

    # Split the URL into parts before and after the "ref" parameter
    url_parts = original_url.split('/ref=')
    base_url = url_parts[0]

    # Replace the existing "ref" parameter with the new one based on page number
    new_ref = f'ref=cm_cr_arp_d_paging_btm_next_{page_number}'

    # Reconstruct the URL with the new "ref" parameter and page number
    # The rest of the query string remains unchanged
    if len(url_parts) > 1:
        query_string = url_parts[1].split('?')[1] if '?' in url_parts[1] else ''
        modified_url = f"{base_url}/{new_ref}?{query_string}&pageNumber={page_number}"
    else:
        modified_url = f"{base_url}/{new_ref}?pageNumber={page_number}"
    
    return modified_url


def get_reviews(url):

    custom_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'cache-control' : 'no-cache',
    'x-Cache' : 'Miss from cloudfront'
    }

    page_number = 1
    scraped_reviews = []

    while True:

        paginated_url = convert_review_link(url, page_number)

        response = requests.get(paginated_url, headers=custom_headers)
        soup = BeautifulSoup(response.text, "lxml")

        review_elements = soup.select("div.review")

        for review in review_elements:

            r_rating_element = review.select_one("i.review-rating")
            r_rating = r_rating_element.text.replace("out of 5 stars", "") if r_rating_element else None

            r_title_element = review.select_one("a.review-title")
            r_title_span_element = r_title_element.select_one("span:not([class])") if r_title_element else None
            r_title = r_title_span_element.text if r_title_span_element else None

            r_content_element = review.select_one("span.review-text")
            r_content = r_content_element.text if r_content_element else None

            r = {
                "rating": r_rating,
                "title": r_title,
                "content": r_content,
            }

            scraped_reviews.append(r)

        if not soup.select_one("li.a-disabled.a-last"):
            page_number+=1
            #sleep(1) 
        else:
            break

    return scraped_reviews
    pass
