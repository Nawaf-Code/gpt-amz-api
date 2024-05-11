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
        reviews = [
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nممتاز جداً بالنسبة لسعرهعازل للصوت و جودة الصوت ممتازة بالنسبة لي لكن يعيبه ان الي حولك يسمعون إذا كنت معلي الصوت\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nعزل وراحة وصوت ممتاز\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nالسلبيات: الصوت مكتوم لكن ممكن تعديله من البرنامج الخاص السماعه مزعجه لو الجو حار اذنك هاتتعرقالمايك مش احسن حاجه كمان لايوجد زر لتشغيلايجابيات : عزل الضوضاء عالم تانىالصوت مجسم رائعمريحه للاذن فترات طويلهالبطاريه اسبوع مع تفعيل عازل الضوضاءجوده تصنيع ممتازه يجى معاها حافظه شيك للسماعهاسم برنامج التشغيلsoundcore\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nافضل سماعة اشتريتها نسبة العزل فيها ممتاز جودة الصوت ممتازة مريحة في اللبس وسعرها ممتاز\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nالسماعة رائعة وجودة الصوت والعزل فوق المتوقع..\n"
        },
        {
            "rating": "3.0 ",
            "title": null,
            "content": "\nبشكل عام جميلة جداالعزل روعة والشفافية حلوةبس فيه ملاحظة لما تشغل العزل ومافي شيء شغال بالسماعة يسبب ضغط على السمع بالنسبة للصوت مزعج احيانابالنسبة للراحة مريحة\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nبعد استخدام شهر ترقيبا السماعه جدا ممتازه الصراحه والي فاجأني با السماعه بطاريتها تطول مره معي تقعد با الايام ولا اشحنها والعزل جيد و صوت السماعه كويس الصوت عالي و يطرب لاكن بس اعلي الصوت احس جودة الصوت تنخفض ويصير مزعج عشان تحل المشكلة لازم تعدل با الايكولايزر الي يجي مع برنامج السماعه ، والبيز يدغدغ حلو للي يسمع فونك مو الي يفجر الأذن طبعا لان هي با الأول والأخير بلوتوث لاكن تأدي صراحه بس في مشكله بسيطه والي هي البيز يصقع مره اذا عليت البيز اخر شي با الايكولايزر، على سعر 200 ممتازه جدا👌🏻\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nسماعة ممتازة سعرها عند جرير غالي وعند امازون رخيص يفرق 50 ريال او اكثر\n"
        },
        {
            "rating": "5.0 ",
            "title": "Fantastic headphones at this price range.",
            "content": "\nI'm not really a sound expert, so as many of you can certainly relate, I usually skip parts where the person doing a headphone review talks about the bass and sound quality. However, even to my inexperienced ears, this was paradise. The headphones sound quality shone through, and I found myself dropping my hyperx cloud II headphones (which are 5 times the price) whenever I am not gaming. Sound never escapes the headphones, which is a great plus whenever you really wanna jam on max audio. I tried to maximise the audio output and stood next to someone I knew, and he confirmed he heard nothing.The headphones are also very comfortable, and I almost always forget their presence. They are very light and rest well on the head. The size changing mechanism is very practical and ergonomic.I got this at a deal for around 50$, which was an absolute bargain. I debated splurging and going for the soundcore space ones, but I really don't think I need something better than this one.The control buttons are very practical and easy-to-use. The design is also very sleek and of high build quality. The ANC switch can be a little annoying to deal with since sometimes you just keep holding it with your hand while trying to reach the other buttons, but it is a minor inconvenience.Speaking of the ANC, the ANC allows little to no audio through, and the transparency mode even amplifies the surrounding voices in a way that didn’t feel noisy.All in all, it's a great purchase and one that I'm sure most people who are looking for bluetooth headphones would not regret. Sound experts could find faults with this headphone, but I honestly think the majority of people wouldn't.\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nإيجابي ؛ عزل ممتاز على ثلاث درجات- شحن سريع - مخرجات الصوت تقدر تلعب بها على كيفك من التطبيق .سلبي ؛ ثقيلة معدنها -تصدع - خامتها متوسطة - ماتشبك على جهازين تعلق شوي - بعض الميزات الزايدة مالها داعي مثل اللمس لانها تشغلك تلمس بالغلط وتتفعل -وايضاً حجمها كبير .شريتها خصم ١٧٦ والان سعرها أصلا ١٧٠ ملعوب علي هههه\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nفيها خاصيه عزل الصوت اعجبتنيالصراحه مااقدر اقيمها عدل لانها تو ماكملت شهر عنديلكن صعرها ممتاز وصوتها عاجبني والعزل بعد ممتاز فيها\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nالسماعة رهيبه عازله للأصوات  والصوت رهيب ومافي تقطيع بس مشكلته صغيره بس مايضر ماتوجع الاذن\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nبس الي جمبك يسمعون كل شي تشغله\n"
        },
        {
            "rating": "5.0 ",
            "title": "Cool",
            "content": "\nI like it very much specially the noise canceling\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nعزل وصوت وشكل توب انصح\n"
        },
        {
            "rating": "5.0 ",
            "title": "افضل سماعة",
            "content": "\n.\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nصوت رائع\n"
        },
        {
            "rating": "5.0 ",
            "title": "Clear sound",
            "content": "\nThe sound and mic is perfect\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nمنتج جيد جودة عالية سعر رخيص لدي ملاحظة واحدة فقطجودة صوت ممتازة كل شيء رائع الملاحظة الوحيده هي الازرار بارزة ومعرضة لضغط بالخطأ مع اي حركة يد  هذا شي وحيد الي ما حبيتو\n"
        },
        {
            "rating": "5.0 ",
            "title": "Very nice",
            "content": "\nI like its price compared to quality\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nاخذتها لي وبعدين ولدي عجبته واخذها لجامعته حرفياً قويه وعزلها خرافي وتجنن وخفيفه مو ثقيله\n"
        },
        {
            "rating": "4.0 ",
            "title": "Having same features to expensive brands",
            "content": "\nThis has same features with the other expensive brands in good price. The sound and ANC is good maybe it's not superb but it's okay based on the price... This product is new for me but I love this product now.\n"
        },
        {
            "rating": "5.0 ",
            "title": "Stunning 😍",
            "content": "\nI loved this one 😍\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nمن أفضل السماعات صراحه تكفي وتوفي\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nاستخدامها لي خمس اشهر على pc وعلى الجوال في نفس الوقت استعملها تقريبا كل يوم من اربع لخمس ساعات شحنها سريع العزل ممتاز\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nعزل الصوت ممتاز و عند الشحن تجلس فترات طويله وما احتاج اشحنها كثير\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nممتازه جداً و مواصفات عاليه\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nمنتج مميز والصوت واضح وتصميم سلسل وجميل.\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nالسماعة خفيفه ومريحه وصوتها صافي والعزل بالمقارنه بسعرها ممتاز انصحكم فيها وبقوه\n"
        },
        {
            "rating": "5.0 ",
            "title": "Powerful and Amazing Sound",
            "content": "\nVery high quality, Sound is amazing especially the deep bass, ling battery life\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nجيده و صوتها قوي و يبغالها شحن\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nعزل الصوت فيها ممتاز و الصوت جدا واضحمريحه اثناء الاستخدام و خفيفه\n"
        },
        {
            "rating": "4.0 ",
            "title": "Best Value for Money imo",
            "content": "\nFirst of all, these headphones are considered to be one of the best value-for-money options out there. Here are the advantages and disadvantages:1. The sound quality is acceptable, but you need to choose the right equalizer mode that suits the type of content you're listening to, such as music, movies, or YouTube videos.2. The Soundcore app provides a very smooth experience with a clean and easy-to-use interface. Bluetooth pairing is quick, but for some reason, NFC pairing didn't work for me.3. The headphone pads are comfortable and won't cause discomfort unless you wear them for a long period of time.4. The quality of materials used is the weakest aspect of these headphones. They feel okay in your hands, but there are some unsettling finishing sounds. Considering the price, it's understandable, but I feel like they could fall apart at any moment due to the weak and cheap plastic.5. I didn't like the default equalizer settings in the Soundcore app, but once you customize your own, the experience becomes significantly better, in my opinion.6. The noise cancellation is good if you prefer it, and you can quickly switch between two noise cancellation modes. Indoor noise cancellation is quite effective, but you might need some time to get used to the pressure sensation, similar to being on a plane.7. The headphone case is solid and made of good material, providing excellent protection for the headphones.Overall, it's a good choice if you're looking for a budget noise-canceling option with good sound quality, a user-friendly app, and a long-lasting battery. The only downsides are the cheap feel of the materials used and the short length of the Type-C USB cable.\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nسماعة مميزة ومريحة وميزة الغاء الازعاج شغال\n"
        },
        {
            "rating": "5.0 ",
            "title": "Just perfect",
            "content": "\nJust perfect\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nجيد\n"
        },
        {
            "rating": "5.0 ",
            "title": "Long lasting battery im using it for four days now and it’s still high",
            "content": "\nThe noise cancellation is on point you cant hear anybody around you\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nمن أفضل السماعات الي جربتها عزل وراحة وسعر وكمية شحن لدرجة عادي بالاسبوع مره فقط ما تناسب الجيم بسبب انزلاقها من الراس بسبب نعومتها لكن الباقي 10/10\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nممتازة عزل ممتاز للأستخدام مريحه للأذن\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nصوتها عالي العزل تمام وتشتغل مع الايفون تمام انصح بيها 👍🏼\n"
        },
        {
            "rating": "4.0 ",
            "title": "The Quality of the sound is so good.",
            "content": "\nThe only problem with this, is that if you are outside and the wind is strong, the whistling of the wind is disturbing because you can heard the  wind clairly, even with noise canceling on. onestly, it's not like the first time I bought the TOSHIBA brand, even if the wind is strong, you won't really notice that there is a strong wind. But when it comes to the sound quality, Yes.., I love it..😘 and lastly, the of this design of this  headphone is very cute, lovely and  admirable.Thank you so mush...😘🙋‍♂️NOT BAD.\n"
        },
        {
            "rating": "5.0 ",
            "title": "Price",
            "content": "\nIf you wear glasses, i will suggest you to try it out first before buying it but in this price range this is a very very good product\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nالسماعة صوتها خرافي والعزل حلو على سعرها\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nاشكر البائع على سرعة الشحن من افضل السماعات اللي جربتها للعزل والسعر بطل\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nماشاء الله جودة صوت وعزل فخم\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nحلوه\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nالمنتج ممتاز مقارنة بالسعر\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nاعجبتني واخذتها بناءا على التعليقات الايجايية وفعلا كان فيه مصداقيةوحتى سعرها ممتاز جداًصرلها معي تقريبا اسبوع وكم يوم ✔️\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nسنه بعدين انكسرت ما تنفع للتمارين ابدا كبير وزنها مره مره لكن العزل وكل شي مره تمام على سعرها حلوه مره وانكسرت بعد سنه بس كسر بسيط باقي استخدمها وكل شي تمام\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nاستخدمها لي شهر تقريبا بالنادي واحيانا بالبيتالايجابيات : البطارية ( احط العزل دائما ومع استخدام ساعتين يوميا تقريبا تقعد اكثر من اسبوع ) بالضبط ماادري لكن تطول مره.الصوت: جيد جداالعزل : مايعزلك تماما لكن عزلها كويس مثلا :(بالنادي يشغلون موسيقى وانا اكون حاط السماعه على العزل اسمعها لكن ضعيف واذا شغلت شي بالسماعه تصير اقل الموسيقى )الاتصال بالبلوتوث سرييييع جداالعيوب :اذا حطيت السماعه وماهو شغال شي احيانا قليله اسمع صفير بإذني اليسار ، يمكن لاني استخدم سماعه ثانيه داخل الاذن ( استخدمها عند النوم)\n"
        },
        {
            "rating": "5.0 ",
            "title": "Hmmmm",
            "content": "\nNice very good item\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nاحسن سماعات جربته من نحيت البيس من نحيت الوضوح لاكن المايك حقها ردي اي هواء لو بسيط يخرب الي تكلمه بينزعج فا إذ بتشتري لاتشتري علشان المكالمات\n"
        },
        {
            "rating": "5.0 ",
            "title": "Great product",
            "content": "\nI liked the product and price\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nقوية بتعجبكم 👍😍\n"
        },
        {
            "rating": "5.0 ",
            "title": "Best at it’s price",
            "content": "\nI really recommend for this price it’s got almost every feature u need the noise cancellation is great the mic is decent not that bad overall it’s great value\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nممتاز انصح به شريته بالعرض بسعر179\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nمنتج جيد و وسهل في الاقتران مع التليفونالمايك سيء و لا يمكن التحدث من خلاله بوضوح أبدا\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nفيه ٣ مستويات للعزل اخر مستوى قارنته مع سماعه سوني مقاربه جدا لها من ناحيه العزل والصوت والشحنعلى سعرها ممتازه جدا\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nجدا سماعة ممتازة في جميع خدماتها عدا وزنها جدا خفيف لدرجة مايثبت بالرأس\n"
        },
        {
            "rating": "5.0 ",
            "title": "👍🏻",
            "content": "\n👍🏻\n"
        },
        {
            "rating": "5.0 ",
            "title": "A Great Buy !",
            "content": "\nI am more of an earbuds person and what made me switch to headphone is because I am looking for longer battery life, especially during long travel.In the realm of mid-range headphones, the Anker Soundcore Life Q30 Hybrid ANC Headphones stand out as a remarkable choice.What I like about this headphone:1. Comfort: Over-the-ear cups with plush foams fit perfectly and doesn't hurt my ears after using it for a long time.2. Controls/Connectivity: Easy to understand and operate. I get used to it pretty quickly.3. Battery:  The best battery life for mid-range headphone!4. Price: Truly a great value for money5. Audio Quality: for a casual listener like me I would say that the audio quality is okay not that impressive but it's already acceptable for me and it has an app where you can play with the equalizers to suit your listening mood.6. ANC: You can still hear a little bit of outside sounds especially car sounds even when you're on ANC mode,  but it filters just fine. It is not something that will trouble you that much.Overall, this headphone is a great buy!\n"
        },
        {
            "rating": "5.0 ",
            "title": "good headset",
            "content": "\nGreat quality once compared with Price.\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nكنت متخوف منها من تجارب سابقة و لكن بعد قراءت المراجعات قمت بالشراء و لم اندم و اعتبرها استثمار ناجح تقدر انك توصل عليها اكثر من جهاز و التطبيق للجوال ممتاز و سهل الاستخدامو السعر جدا مناسب 179 على الجودة التي تتمتع به السماعة\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nكجودة اشوف سعر مناسب لكن الغريب هو لمن استخدمه على جوال في صوت \"تش\" يطلع خصوصا لمن اكون على السناب .. عموما انا راضي ومايتكرر كثير الا في ظروف غريبة وانا متاكد انها مشكلة بنظام السماعات\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nالمنتج وفى احتياجي بشكل كامل العزل حلو السماعه خفيفه وما تثقل على الراس و مرنه و البطاريه ما تخلص بسرعه بس لو فيها زر تحكم للمايك عشان القيمنق\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nممتازه جدا وحلوه\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nالعزل ممتاز وضوح الصوت مقارنه بالسعر جيد جدا\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nالعزل ماشاء الله شي اسطوري\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nسعرها مناسب لأدائها\n"
        },
        {
            "rating": "5.0 ",
            "title": "Recommend",
            "content": "\nGreat battery & transparencyI would recommend it to anyone\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nعلزها ممتاز وصوتها ممتاز لاكن عيبها واحد صوتها منخفض شوي خاصة اني احب الأغاني الصاخبة\n"
        },
        {
            "rating": "4.0 ",
            "title": "Good quality",
            "content": "\nThing is, it's buffin the sound, it doesn't give u the real sound\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nجيد جيدا\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nمقابل سعرها ومميزاتها تستاهل كل ريال فيها .. اشتريتها وقت التخفيضانصح فيها تذكر ( مقابل سعرها )لا تدور على مواصفات عالية وسعر رخيص\n"
        },
        {
            "rating": "5.0 ",
            "title": "Nice Experience",
            "content": "\nThe sound quality is perfect and the headphones options are to the point.\n"
        },
        {
            "rating": "5.0 ",
            "title": "Good headphone for the price range..",
            "content": "\nThe headphone weight is perfect. Sound is also good, ANC is average. over all the product is good.\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nصوت حلو والعزل جيد جدا وتقدر تشغلها على السوني  ممتازه جدا\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nاشتريت 2 و هاذي الثالثة\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nسماعة جودة عالية\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nممتازه انصح فيها اصليه\n"
        },
        {
            "rating": "5.0 ",
            "title": "ممتازه وملحقاتها ممتازه",
            "content": "\n👍🏻👍🏻👍🏻\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nزين\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nثقيله بنسبه لي على الرأس ماقدر احطها فترات طويله ، لكنها ممتازة من ناحية الشحن تتطول معاك كم يوم و الصوت ممتاز\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nالصوت فيه رائع وكذلك العزل جيد\n"
        },
        {
            "rating": "4.0 ",
            "title": null,
            "content": "\nالنظاره تضعف مع الوقت يعني الجلد مع الاستخدام الطويل بيبدء يتقطع و البلاستيك نوعه سيئ يطلع اصوات, العزل و الصوت جدا رهيب ولاكن الجلد و البلاستيك سيئ\n"
        },
        {
            "rating": "5.0 ",
            "title": "Headphone",
            "content": "\nAll done\n"
        },
        {
            "rating": "5.0 ",
            "title": "رهيب على هالسعر",
            "content": "\n.\n"
        },
        {
            "rating": "3.0 ",
            "title": null,
            "content": "\nالسماعة ممتازه بس وصلتني وفيها صوت اذا تحركت ، واكتشفت ان الصوت من الازرار مو ثابته . وثاني شي اذا شغلت الدسكورد لازم تختار مايك ثاني مو مايك السماعه ولا بيخرب الصوت .\n"
        },
        {
            "rating": "4.0 ",
            "title": "سماعة",
            "content": "\nانصح فيها\n"
        },
        {
            "rating": "5.0 ",
            "title": "Superb",
            "content": "\nCheap and quality.. worth every bucks you spent\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nعمليه جدا شريته عشان الجامعة وافضل سماعه لا سلكيه مرت علي يوجد وضع العزل على ٣ مستويات والشحن يدوم لفتره طويله وحتى لو عليت الصوت مايطلع من السماعه وفيه ازرار على اليمين تطويل وتخفيض الصوت ويجي معه شنطه والشاحن ووصله تنشبك بالاجهزه مثل يد البلاستيشن وفيه وضع حساس على جوانب السماعه يمديك تتحكم بوضع العزل والسعر جيد مقارنه بالجوده\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nسعرها ممتاز وعزلها رهيب\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nالسماعة ممتازه من كل النواحي الصوت و العزل فيها ممتاز و مدة شحن السماعة انا اشحنها فل و استخدمها كل يوم تقعد معاي اسبوع و اكثر احيانا\n"
        },
        {
            "rating": "5.0 ",
            "title": "👍",
            "content": "\n👍\n"
        },
        {
            "rating": "3.0 ",
            "title": null,
            "content": "\nجودة المنتج رووعه والعزل فيه للأمانه ممتاز جداً لكن دقيقه دقيقتين بالنسبه لي وحسيت بضغط على الاذن وشعور غير مريح ابداً ..\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nبعد التجربه عزل الصوت وصفاووه ممتاز جدا\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nسعره مقابل الجوده جدا ممتاز\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nوضوح الصوت والعزل ممتازالتوصيل سريع\n"
        },
        {
            "rating": "5.0 ",
            "title": null,
            "content": "\nممتازة وجباااارة خذها وانت مغمض للموسيقى صوت ولا اروع والعزل رهييييب وسعرها ممتاز على المواصفات الي تقدمها السماعة 👍🏻\n"
        },
        {
            "rating": "4.0 ",
            "title": "Excellent value for money headphones",
            "content": "\nAn excellent, well made set of headphones, easy to use and comfortable. Noise cancelling could be a wee bit better, hence 4*s\n"
        }
    ]
        return {"reviews": reviews}
    
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
