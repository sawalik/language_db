"""Seed the vocab DB with common Korean and Japanese words.  Run: python -m language_os.seed_vocab"""
from . import db

# (word, reading, meaning)
KOREAN = [
    # people
    ("사랑", "sarang", "love"), ("친구", "chingu", "friend"), ("가족", "gajok", "family"),
    ("엄마", "eomma", "mom"), ("아빠", "appa", "dad"), ("형", "hyeong", "older brother (said by a man)"),
    ("누나", "nuna", "older sister (said by a man)"), ("오빠", "oppa", "older brother (said by a woman)"),
    ("언니", "eonni", "older sister (said by a woman)"), ("동생", "dongsaeng", "younger sibling"),
    ("선생님", "seonsaengnim", "teacher"), ("학생", "haksaeng", "student"), ("사람", "saram", "person"),
    ("남자", "namja", "man"), ("여자", "yeoja", "woman"), ("아이", "ai", "child"),
    # time & nature
    ("시간", "sigan", "time"), ("오늘", "oneul", "today"), ("내일", "naeil", "tomorrow"),
    ("어제", "eoje", "yesterday"), ("지금", "jigeum", "now"), ("아침", "achim", "morning"),
    ("저녁", "jeonyeok", "evening"), ("밤", "bam", "night"), ("날씨", "nalssi", "weather"),
    ("비", "bi", "rain"), ("눈", "nun", "snow; eye"), ("바람", "baram", "wind"),
    ("하늘", "haneul", "sky"), ("바다", "bada", "sea"), ("산", "san", "mountain"),
    ("꽃", "kkot", "flower"), ("나무", "namu", "tree"), ("물", "mul", "water"),
    # food & animals
    ("밥", "bap", "cooked rice; meal"), ("음식", "eumsik", "food"), ("김치", "gimchi", "kimchi"),
    ("고기", "gogi", "meat"), ("과일", "gwail", "fruit"), ("사과", "sagwa", "apple"),
    ("커피", "keopi", "coffee"), ("술", "sul", "alcohol"), ("개", "gae", "dog"),
    ("고양이", "goyangi", "cat"),
    # places & things
    ("집", "jip", "house; home"), ("학교", "hakgyo", "school"), ("회사", "hoesa", "company"),
    ("병원", "byeongwon", "hospital"), ("약", "yak", "medicine"), ("버스", "beoseu", "bus"), ("지하철", "jihacheol", "subway"),
    ("역", "yeok", "station"), ("공항", "gonghang", "airport"), ("전화", "jeonhwa", "phone call"),
    ("책", "chaek", "book"), ("영화", "yeonghwa", "movie"), ("노래", "norae", "song"),
    ("음악", "eumak", "music"), ("돈", "don", "money"), ("이름", "ireum", "name"),
    ("나라", "nara", "country"), ("한국", "hanguk", "Korea"),
    # abstract (drama staples)
    ("마음", "maeum", "heart; mind"), ("생각", "saenggak", "thought"), ("꿈", "kkum", "dream"),
    ("행복", "haengbok", "happiness"), ("거짓말", "geojitmal", "lie"), ("비밀", "bimil", "secret"),
    ("약속", "yaksok", "promise"), ("기억", "gieok", "memory"), ("운명", "unmyeong", "fate"),
    # verbs
    ("먹다", "meokda", "to eat"), ("마시다", "masida", "to drink"), ("가다", "gada", "to go"),
    ("오다", "oda", "to come"), ("보다", "boda", "to see; to watch"), ("듣다", "deutda", "to listen; to hear"),
    ("말하다", "malhada", "to speak"), ("알다", "alda", "to know"), ("모르다", "moreuda", "to not know"),
    ("주다", "juda", "to give"), ("받다", "batda", "to receive"), ("만나다", "mannada", "to meet"),
    ("기다리다", "gidarida", "to wait"), ("자다", "jada", "to sleep"), ("살다", "salda", "to live"),
    ("웃다", "utda", "to laugh; to smile"), ("울다", "ulda", "to cry"), ("읽다", "ikda", "to read"),
    ("배우다", "baeuda", "to learn"), ("사랑하다", "saranghada", "to love"),
    # adjectives & expressions
    ("좋다", "jota", "to be good"), ("예쁘다", "yeppeuda", "to be pretty"),
    ("맛있다", "masitda", "to be delicious"), ("슬프다", "seulpeuda", "to be sad"),
    ("어렵다", "eoryeopda", "to be difficult"), ("보고 싶다", "bogo sipda", "to miss (someone)"),
    ("감사합니다", "gamsahamnida", "thank you"), ("미안해요", "mianhaeyo", "I'm sorry"),
    ("괜찮아요", "gwaenchanayo", "it's okay"),
]

JAPANESE = [
    # people
    ("愛", "あい (ai)", "love"), ("友達", "ともだち (tomodachi)", "friend"),
    ("家族", "かぞく (kazoku)", "family"), ("母", "はは (haha)", "mother (own)"),
    ("父", "ちち (chichi)", "father (own)"), ("兄", "あに (ani)", "older brother (own)"),
    ("姉", "あね (ane)", "older sister (own)"), ("先生", "せんせい (sensei)", "teacher"),
    ("学生", "がくせい (gakusei)", "student"), ("人", "ひと (hito)", "person"),
    ("男", "おとこ (otoko)", "man"), ("女", "おんな (onna)", "woman"),
    ("子供", "こども (kodomo)", "child"), ("先輩", "せんぱい (senpai)", "senior (school/work)"),
    ("仲間", "なかま (nakama)", "companion; comrade"),
    # time & nature
    ("時間", "じかん (jikan)", "time"), ("今日", "きょう (kyou)", "today"),
    ("明日", "あした (ashita)", "tomorrow"), ("昨日", "きのう (kinou)", "yesterday"),
    ("今", "いま (ima)", "now"), ("朝", "あさ (asa)", "morning"), ("夜", "よる (yoru)", "night"),
    ("天気", "てんき (tenki)", "weather"), ("雨", "あめ (ame)", "rain"), ("雪", "ゆき (yuki)", "snow"),
    ("風", "かぜ (kaze)", "wind"), ("空", "そら (sora)", "sky"), ("海", "うみ (umi)", "sea"),
    ("山", "やま (yama)", "mountain"), ("花", "はな (hana)", "flower"), ("木", "き (ki)", "tree"),
    ("水", "みず (mizu)", "water"),
    # food & animals
    ("ご飯", "ごはん (gohan)", "cooked rice; meal"), ("食べ物", "たべもの (tabemono)", "food"),
    ("肉", "にく (niku)", "meat"), ("魚", "さかな (sakana)", "fish"),
    ("果物", "くだもの (kudamono)", "fruit"), ("お茶", "おちゃ (ocha)", "tea"),
    ("酒", "さけ (sake)", "alcohol; sake"), ("犬", "いぬ (inu)", "dog"), ("猫", "ねこ (neko)", "cat"),
    # places & things
    ("家", "いえ (ie)", "house; home"), ("学校", "がっこう (gakkou)", "school"),
    ("会社", "かいしゃ (kaisha)", "company"), ("仕事", "しごと (shigoto)", "work; job"),
    ("病院", "びょういん (byouin)", "hospital"), ("薬", "くすり (kusuri)", "medicine"),
    ("道", "みち (michi)", "road; way"), ("車", "くるま (kuruma)", "car"),
    ("電車", "でんしゃ (densha)", "train"), ("駅", "えき (eki)", "station"),
    ("空港", "くうこう (kuukou)", "airport"), ("電話", "でんわ (denwa)", "phone call"),
    ("本", "ほん (hon)", "book"), ("映画", "えいが (eiga)", "movie"), ("歌", "うた (uta)", "song"),
    ("音楽", "おんがく (ongaku)", "music"), ("お金", "おかね (okane)", "money"),
    ("名前", "なまえ (namae)", "name"), ("国", "くに (kuni)", "country"),
    ("日本", "にほん (nihon)", "Japan"), ("言葉", "ことば (kotoba)", "word; language"),
    # abstract (anime staples)
    ("心", "こころ (kokoro)", "heart; mind"), ("夢", "ゆめ (yume)", "dream"),
    ("幸せ", "しあわせ (shiawase)", "happiness"), ("嘘", "うそ (uso)", "lie"),
    ("秘密", "ひみつ (himitsu)", "secret"), ("約束", "やくそく (yakusoku)", "promise"),
    ("思い出", "おもいで (omoide)", "memory; recollection"), ("運命", "うんめい (unmei)", "fate"),
    # verbs
    ("食べる", "たべる (taberu)", "to eat"), ("飲む", "のむ (nomu)", "to drink"),
    ("行く", "いく (iku)", "to go"), ("来る", "くる (kuru)", "to come"), ("見る", "みる (miru)", "to see; to watch"),
    ("聞く", "きく (kiku)", "to listen; to ask"), ("話す", "はなす (hanasu)", "to speak"),
    ("知る", "しる (shiru)", "to know"), ("分かる", "わかる (wakaru)", "to understand"),
    ("会う", "あう (au)", "to meet"), ("待つ", "まつ (matsu)", "to wait"),
    ("寝る", "ねる (neru)", "to sleep"), ("生きる", "いきる (ikiru)", "to live"),
    ("笑う", "わらう (warau)", "to laugh"), ("泣く", "なく (naku)", "to cry"),
    ("読む", "よむ (yomu)", "to read"), ("書く", "かく (kaku)", "to write"),
    ("買う", "かう (kau)", "to buy"), ("戦う", "たたかう (tatakau)", "to fight"),
    ("守る", "まもる (mamoru)", "to protect"),
    # adjectives & expressions
    ("大きい", "おおきい (ookii)", "big"), ("可愛い", "かわいい (kawaii)", "cute"),
    ("美味しい", "おいしい (oishii)", "delicious"), ("怖い", "こわい (kowai)", "scary"),
    ("悲しい", "かなしい (kanashii)", "sad"), ("難しい", "むずかしい (muzukashii)", "difficult"),
    ("強い", "つよい (tsuyoi)", "strong"), ("大丈夫", "だいじょうぶ (daijoubu)", "okay; all right"),
    ("ありがとう", "ありがとう (arigatou)", "thank you"), ("すみません", "すみません (sumimasen)", "excuse me; sorry"),
]


def main():
    for language, words in (("Korean", KOREAN), ("Japanese", JAPANESE)):
        added = sum(db.add_word(language, w, m, reading=r, source="seed") for w, r, m in words)
        print(f"{language}: {added} added, {len(words) - added} skipped, {len(words)} in list")


if __name__ == "__main__":
    main()
