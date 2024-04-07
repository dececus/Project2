from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def flower(model_path, labels_path, image_path):           
  np.set_printoptions(suppress=True)
  model = load_model(model_path, compile=False)
  class_names = open(labels_path, "r", encoding = "utf-8").readlines()
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = Image.open(image_path).convert("RGB")
  
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
  
  image_array = np.asarray(image)
  
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
  
  data[0] = normalized_image_array
  
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]

  d = ""

  if(str(class_name[2:])=="Аллиум\n"):
    d = "Аллиум на "
  elif(str(class_name[2:])=="Алоэ траски\n"):
    d = "Алоэ траски на "
  elif(str(class_name[2:])=="Альстромерия\n"):
    d = "Альстромерия на "
  elif(str(class_name[2:])=="Амариллис\n"):
    d = "Амариллис на "
  elif(str(class_name[2:])=="Анемон\n"):
    d = "Анемон на "
  elif(str(class_name[2:])=="Антуриум\n"):
    d = "Антуриум на "
  elif(str(class_name[2:])=="Астильба\n"):
    d = "Астильба на "
  elif(str(class_name[2:])=="Астра\n"):
    d = "Астра на "
  elif(str(class_name[2:])=="Астранция\n"):
    d = "Астранция на "
  elif(str(class_name[2:])=="Ахиллея\n"):
    d = "Ахиллея на "
  elif(str(class_name[2:])=="Берцелия\n"):
    d = "Берцелия на "
  elif(str(class_name[2:])=="Брассика\n"):
    d = "Брассика на "
  elif(str(class_name[2:])=="Бруния\n"):
    d = "Бруния на "
  elif(str(class_name[2:])=="Бувардия\n"):
    d = "Бувардия на "
  elif(str(class_name[2:])=="Верба\n"):
    d = "Верба на "
  elif(str(class_name[2:])=="Вереск\n"):
    d = "Вереск на "
  elif(str(class_name[2:])=="Вероника\n"):
    d = "Вероника на "
  elif(str(class_name[2:])=="Вибурнум\n"):
    d = "Вибурнум на "
  elif(str(class_name[2:])=="Гвоздика\n"):
    d = "Гвоздика на "
  elif(str(class_name[2:])=="Гениста\n"):
    d = "Гениста на "
  elif(str(class_name[2:])=="Георгин\n"):
    d = "Георгин на "
  elif(str(class_name[2:])=="Гербера\n"):
    d = "Гербера на "
  elif(str(class_name[2:])=="Гиацинт\n"):
    d = "Гиацинт на "
  elif(str(class_name[2:])=="Гиперикум\n"):
    d = "Гиперикум на "
  elif(str(class_name[2:])=="Гипсофила\n"):
    d = "Гипсофила на "
  elif(str(class_name[2:])=="Гладиолус\n"):
    d = "Гладиолус на "
  elif(str(class_name[2:])=="Гортензия\n"):
    d = "Гортензия на "
  elif(str(class_name[2:])=="Декоративный ананас\n"):
    d = "Декоративный ананас на "
  elif(str(class_name[2:])=="Дельфиниум\n"):
    d = "Дельфиниум на "
  elif(str(class_name[2:])=="Ежевика\n"):
    d = "Ежевика на "
  elif(str(class_name[2:])=="Илекс\n"):
    d = "Илекс на "
  elif(str(class_name[2:])=="Ирис\n"):
    d = "Ирис на "
  elif(str(class_name[2:])=="Калла\n"):
    d = "Калла на "
  elif(str(class_name[2:])=="Кампанула\n"):
    d = "Кампанула на "
  elif(str(class_name[2:])=="Кортадерия\n"):
    d = "Кортадерия на "
  elif(str(class_name[2:])=="Красивоплодник\n"):
    d = "Красивоплодник на "
  elif(str(class_name[2:])=="Краспедия\n"):
    d = "Краспедия на "
  elif(str(class_name[2:])=="Лаванда\n"):
    d = "Лаванда на "
  elif(str(class_name[2:])=="Ландыш\n"):
    d = "Ландыш на "
  elif(str(class_name[2:])=="Левкой\n"):
    d = "Левкой на "
  elif(str(class_name[2:])=="Леукадендрон\n"):
    d = "Леукадендрон на "
  elif(str(class_name[2:])=="Лизиантус\n"):
    d = "Лизиантус на "
  elif(str(class_name[2:])=="Лилия\n"):
    d = "Лилия на "
  elif(str(class_name[2:])=="Лимониум\n"):
    d = "Лимониум на "
  elif(str(class_name[2:])=="Лист дуба\n"):
    d = "Лист дуба на "
  elif(str(class_name[2:])=="Лунария\n"):
    d = "Лунария на "
  elif(str(class_name[2:])=="Магнолия\n"):
    d = "Магнолия на "
  elif(str(class_name[2:])=="Мимоза\n"):
    d = "Мимоза на "
  elif(str(class_name[2:])=="Мускари\n"):
    d = "Мускари на "
  elif(str(class_name[2:])=="Нарцисс\n"):
    d = "Нарцисс на "
  elif(str(class_name[2:])=="Нерине\n"):
    d = "Нерине на "
  elif(str(class_name[2:])=="Нобилис\n"):
    d = "Нобилис на "
  elif(str(class_name[2:])=="Озотамнус\n"):
    d = "Озотамнус на "
  elif(str(class_name[2:])=="Оксипеталум\n"):
    d = "Оксипеталум на "
  elif(str(class_name[2:])=="Орхидея\n"):
    d = "Орхидея на "
  elif(str(class_name[2:])=="Орхидея дендробиум\n"):
    d = "Орхидея дендробиум на "
  elif(str(class_name[2:])=="Орхидея фаленопсис\n"):
    d = "Орхидея фаленопсис на "
  elif(str(class_name[2:])=="Персик\n"):
    d = "Персик на "
  elif(str(class_name[2:])=="Пион\n"):
    d = "Пион на "
  elif(str(class_name[2:])=="Пион корал шарм\n"):
    d = "Пион корал шарм на "
  elif(str(class_name[2:])=="Пион ред шарм\n"):
    d = "Пион ред шарм на "
  elif(str(class_name[2:])=="Пион сара бернар\n"):
    d = "Пион сара бернар на "
  elif(str(class_name[2:])=="Подснежник\n"):
    d = "Подснежник на "
  elif(str(class_name[2:])=="Подсолнух\n"):
    d = "Подсолнух на "
  elif(str(class_name[2:])=="Протея\n"):
    d = "Протея на "
  elif(str(class_name[2:])=="Пуансеттия\n"):
    d = "Пуансеттия на "
  elif(str(class_name[2:])=="Пшеница\n"):
    d = "Пшеница на "
  elif(str(class_name[2:])=="Ранункулюс\n"):
    d = "Ранункулюс на "
  elif(str(class_name[2:])=="Ранункулюс ханой\n"):
    d = "Ранункулюс ханой на "
  elif(str(class_name[2:])=="Роза\n"):
    d = "Роза на "
  elif(str(class_name[2:])=="Роза дэвида остина\n"):
    d = "Роза дэвида остина на "
  elif(str(class_name[2:])=="Роза кустовая\n"):
    d = "Роза кустовая на "
  elif(str(class_name[2:])=="Роза пионовидная\n"):
    d = "Роза пионовидная на "
  elif(str(class_name[2:])=="Роза пионовидная кахала\n"):
    d = "Роза пионовидная кахала на "
  elif(str(class_name[2:])=="Роза пионовидная мисти баблс\n"):
    d = "Роза пионовидная мисти баблс на "
  elif(str(class_name[2:])=="Роза пионовидная ред пиано\n"):
    d = "Роза пионовидная ред пиано на "
  elif(str(class_name[2:])=="Ромашка\n"):
    d = "Ромашка на "
  elif(str(class_name[2:])=="Седум\n"):
    d = "Седум на "
  elif(str(class_name[2:])=="Серрурия\n"):
    d = "Серрурия на "
  elif(str(class_name[2:])=="Сетария\n"):
    d = "Сетария на "
  elif(str(class_name[2:])=="Сирень\n"):
    d = "Сирень на "
  elif(str(class_name[2:])=="Скабиоза\n"):
    d = "Скабиоза на "
  elif(str(class_name[2:])=="Снежноягодник\n"):
    d = "Снежноягодник на "
  elif(str(class_name[2:])=="Статица\n"):
    d = "Статица на "
  elif(str(class_name[2:])=="Суккуленты\n"):
    d = "Суккуленты на "
  elif(str(class_name[2:])=="Сухоцветы\n"):
    d = "Сухоцветы на "
  elif(str(class_name[2:])=="Трахелиум\n"):
    d = "Трахелиум на "
  elif(str(class_name[2:])=="Туя\n"):
    d = "Туя на "
  elif(str(class_name[2:])=="Тысячелистник\n"):
    d = "Тысячелистник на "
  elif(str(class_name[2:])=="Тюльпан\n"):
    d = "Тюльпан на "
  elif(str(class_name[2:])=="Фрезия\n"):
    d = "Фрезия на "
  elif(str(class_name[2:])=="Хамелациум\n"):
    d = "Хамелациум на "
  elif(str(class_name[2:])=="Хелеборус\n"):
    d = "Хелеборус на "
  elif(str(class_name[2:])=="Хризантема\n"):
    d = "Хризантема на "
  elif(str(class_name[2:])=="Хризантема космо пёпл\n"):
    d = "Хризантема космо пёпл на "
  elif(str(class_name[2:])=="Хризантема момоко\n"):
    d = "Хризантема момоко на "
  elif(str(class_name[2:])=="Целозия\n"):
    d = "Целозия на "
  elif(str(class_name[2:])=="Цинерария\n"):
    d = "Цинерария на "
  elif(str(class_name[2:])=="Эвкалипт\n"):
    d = "Эвкалипт на "
  elif(str(class_name[2:])=="Эрингиум\n"):
    d = "Эрингиум на "
  elif(str(class_name[2:])=="Эулалия\n"):
    d = "Эулалия на "
  elif(str(class_name[2:])=="Эустома\n"):
    d = "Эустома на "

  c = d + str(int(confidence_score*100)) + "%"
  return c