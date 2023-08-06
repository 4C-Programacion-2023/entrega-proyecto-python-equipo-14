import tkinter

from googletrans import Translator

translator = Translator()

def traduccion():
    a = print(translator.translate(text=(texto_a_traducir()), dest = (idioma())))
    return (a)

ventana= tkinter.Tk()

ventana.geometry('1920x200')

ventanita = tkinter.Tk()

ventanita.geometry("450x200")

etiqueta0 = tkinter.Label(ventana, text = ('LENGUAJES'))

etiqueta = tkinter.Label(ventana, text = (
'af:  afrikaans,  '
'sq:  albanian,  '
'am:  amharic,  '
'ar:  arabic,  '
'hy:  armenian,  ',
'az:  azerbaijani,  ',
'eu:  basque,  ',
'be:  belarusian,  ',
'bn:  bengali,  ',
'bs:  bosnian,   ',
"bg:  bulgarian,  ",
'ca:  catalan,  ',
'ceb:  cebuano,  ',
'ny:  chichewa,  \n',
'zh-cn:  chinese (simplified),  ',
'zh-tw:  chinese (traditional),  ',
'co:  corsican,  ',
'hr:  croatian,  ',
'cs:  czech,  ',
'da:  danish,  ',
'nl:  dutch,  ',
'en:  english,  ',
'eo:  esperanto,  ',
'et:  estonian,  ',
'tl:  filipino,  ',
'fi:  finnish,  ',
'fr:  french,  ',
'fy:  frisian,  ',
'gl:  galician,  \n',
'ka:  georgian,  ',
'de:  german,  ',
'el:  greek,  ',
'gu:  gujarati,  ',
'ht:  haitian creole,  ',
'ha:  hausa,  ',
'haw:  hawaiian,  ',
'iw:  hebrew,  ',
'he:  hebrew,  ',
'hi:  hindi,  ',
'hmn:  hmong,  ',
'hu:  hungarian,  ',
'is:  icelandic,  ',
'ig:  igbo,  ',
'id:  indonesian,  ',
'ga:  irish,  \n',
'it:  italian,  ',
'ja:  japanese,  ',
'jw:  javanese,  ',
'kn:  kannada,  ',
'kk:  kazakh,  ',
'km:  khmer,  ',
'ko:  korean,  ',
'ku:  kurdish (kurmanji),  ',
'ky:  kyrgyz,  ',
'lo:  lao,  ',
'la:  latin,  ',
'lv:  latvian,  ',
'lt:  lithuanian,  ',
'lb:  luxembourgish,  ',
'mk:  macedonian,  \n',
'mg:  malagasy,  ',
'ms:  malay,  ',
'ml:  malayalam,  ',
'mt:  maltese,  ',
'mi:  maori,  ',
'mr:  marathi,  ',
'mn:  mongolian,  ',
'my:  myanmar (burmese),  ',
'ne:  nepali,  ',
'no:  norwegian,  ',
'or:  odia,  ',
'ps:  pashto,  ',
'fa:  persian,  ',
'pl:  polish,  ',
'pt:  portuguese,  \n',
'pa:  punjabi,  ',
'ro:  romanian,  ',
'ru:  russian,  ',
'sm:  samoan,  ',
'gd:  scots gaelic,  ',
'sr:  serbian,  ',
'st:  sesotho,  ',
'sn:  shona,  ',
'sd:  sindhi,  ',
'si:  sinhala,  ',
'sk:  slovak,  ',
'sl:  slovenian,  ',
'so:  somali,  ',
'es:  spanish,  ',
'su:  sundanese,  ',
'sw:  swahili,  \n',
'sv:  swedish,  ',
'tg:  tajik,  ',
'ta:  tamil,  ',
'te:  telugu,  ',
'th:  thai,  ',
'tr:  turkish,  ',
'uk:  ukrainian,  ',
'ur:  urdu,  ',
'ug:  uyghur,  ',
'uz:  uzbek,  ',
'vi:  vietnamese,  ',
'cy:  welsh,  ',
'xh:  xhosa,  ',
'yi:  yiddish,  ',
'yo:  yoruba,  ',
'zu:  zulu,  ',))



def texto_a_traducir():
    texto = cajadetexto.get()
    return(texto)

def idioma():
    textito = cajadetexto1.get()
    return(textito)

etiqueta1 = tkinter.Label(ventanita, text = ("\n"
                                             "escribe lo que quieras traducir\n"
                                             "   "))

etiqueta5 = tkinter.Label(ventanita, text = ("Escribe al idioma que quieras traducir(con las abreviaciones de la otra ventana)"))



boton1 = tkinter.Button(ventanita, text = "presiona para traducir", command = traduccion)

boton1.pack()

cajadetexto = tkinter.Entry(ventanita)

cajadetexto1 = tkinter.Entry(ventanita)

etiqueta5.pack(fill = tkinter.X)

cajadetexto1.pack()

etiqueta1.pack(fill = tkinter.X)

cajadetexto.pack()

boton1.pack()

etiqueta0.pack(fill= tkinter.X)

etiqueta.pack(fill = tkinter.X)

etiquetafinal = tkinter.Label(ventanita, text = (traduccion))

etiquetafinal.pack()

ventana.mainloop()

ventanita.mainloop()
