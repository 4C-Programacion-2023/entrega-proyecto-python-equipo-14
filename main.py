import os
import tkinter
from googletrans import Translator
from gtts import gTTS


# para que funcione hay que instalar directamente desde el cdm estos dos comandos:
# 1ro: pip install googletrans
# 2do: pip install googletrans==3.1.0a0
# 3ro: pip install gTTS
# hay que instalarlos en el documento de python, a si que hay que sacar su ubicacion con el comando:
# import os
# import sys
# print(os.path.dirname(sys.executable))
# Todo esto es en el archivo al que vamos a ejecutar nuestro proyecto
# esto ejecuta un print que dice la ubicacion del archivo
# vas a la terminal pones cd y lo que printeo el anterior programa. Despues de esto pones los tres primeros comandos.
class VentanaLenguajes:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1920x200")
        self.master.title("Lista de Lenguajes")
        self.etiqueta0 = tkinter.Label(self.master, text='LENGUAJES\n'
                                                         'af:  afrikaans,  sq:  albanian,  am:  amharic,  ar:  arabic,  hy:  armenian,  az:  azerbaijani,  eu:  basque,  be:  belarusian,  bn:  bengali,  bs:  bosnian,   "bg:  bulgarian,  ca:  catalan,  ceb:  cebuano,  ny:  chichewa,  \nzh-cn:  chinese (simplified),  zh-tw:  chinese (traditional),  co:  corsican,  hr:  croatian,  cs:  czech,  da:  danish,  nl:  dutch,  en:  english,  eo:  esperanto,  et:  estonian,  tl:  filipino,  fi:  finnish,  fr:  french,  fy:  frisian,  gl:  galician,  \nka:  georgian,  de:  german,  el:  greek,  gu:  gujarati,  ht:  haitian creole,  ha:  hausa,  haw:  hawaiian,  iw:  hebrew,  he:  hebrew,  hi:  hindi,  hmn:  hmong,  hu:  hungarian,  is:  icelandic,  ig:  igbo,  id:  indonesian,  ga:  irish,  \nit:  italian,  ja:  japanese,  jw:  javanese,  kn:  kannada,  kk:  kazakh,  km:  khmer,  ko:  korean,  ku:  kurdish (kurmanji),  ky:  kyrgyz,  lo:  lao,  la:  latin,  lv:  latvian,  lt:  lithuanian,  lb:  luxembourgish,  mk:  macedonian,  \nmg:  malagasy,  ms:  malay,  ml:  malayalam,  mt:  maltese,  mi:  maori,  mr:  marathi,  mn:  mongolian,  my:  myanmar (burmese),  ne:  nepali,  no:  norwegian,  or:  odia,  ps:  pashto,  fa:  persian,  pl:  polish,  pt:  portuguese,  \npa:  punjabi,  ro:  romanian,  ru:  russian,  sm:  samoan,  gd:  scots gaelic,  sr:  serbian,  st:  sesotho,  sn:  shona,  sd:  sindhi,  si:  sinhala,  sk:  slovak,  sl:  slovenian,  so:  somali,  es:  spanish,  su:  sundanese,  sw:  swahili,  \nsv:  swedish,  tg:  tajik,  ta:  tamil,  te:  telugu,  th:  thai,  tr:  turkish,  uk:  ukrainian,  ur:  urdu,  ug:  uyghur,  uz:  uzbek,  vi:  vietnamese,  cy:  welsh,  xh:  xhosa,  yi:  yiddish,  yo:  yoruba,  zu:  zulu,  ')
        self.etiqueta0.pack(fill=tkinter.X)
        # Creamos la ventana para mostrar la lista de lenguajes y la etiqueta

        self.historial = []
        self.boton_historial = tkinter.Button(self.master, text="Mostrar Historial", command=self.mostrar_historial)
        self.boton_historial.pack()
        # Creamos la lista del historial y un botón para mostrarla

    def mostrar_historial(self):
        Ventanadehistorial = tkinter.Toplevel(self.master)
        Ventanadehistorial.title("Historial de Traducciones")

        scrol = tkinter.Scrollbar(Ventanadehistorial)
        scrol.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        # Creamos una nueva ventana para mostrar el historial y una barra de desplazamiento

        listbox = tkinter.Listbox(Ventanadehistorial, yscrollcommand=scrol.set)
        listbox.pack(fill=tkinter.BOTH, expand=True)
        # Creamos una lista para mostrar el historial y la asociamos con la barra de desplazamiento

        for item in self.historial:
            listbox.insert(tkinter.END,
                           f"Frase a traducir: {item[0]}  -    Idioma: {item[1]}  -   Frase traducida: {item[2]}")
        # Agregamos elementos al historial en la ventana

        scrol.config(command=listbox.yview)


class Ventanadetraduccion:
    def __init__(self, master):
        self.master = master
        self.master.geometry("450x200")
        self.master.title("Traducción")
        # generamos la ventana donde traducimos
        self.etiqueta1 = tkinter.Label(self.master, text='Escribe lo que quieras traducir\n   ')
        self.etiqueta5 = tkinter.Label(self.master,
                                       text='Escribe al idioma que quieras traducir (con las abreviaciones de la otra ventana)')
        self.boton1 = tkinter.Button(self.master, text="Presiona para traducir", command=self.traduccion)
        self.cajadetexto = tkinter.Entry(self.master)
        self.cajadetexto1 = tkinter.Entry(self.master)
        self.etiqueta_resultado = tkinter.Label(self.master, text="")
        self.botontextoavoz = tkinter.Button(self.master, text="Toca para escuchar", command=self.leertexto)
        # Creamos las cajas de texto, las etiquetas y los botones con cada funcion correspondiente
        self.etiqueta5.pack(fill=tkinter.X)
        self.cajadetexto1.pack()
        self.etiqueta1.pack(fill=tkinter.X)
        self.cajadetexto.pack()
        self.boton1.pack()
        self.etiqueta_resultado.pack()
        self.botontextoavoz.pack()
        # las ponemos en pantalla con el comando pack()

    def idioma(self):
        textito = self.cajadetexto1.get()
        return textito
        # esto define el idioma que ponemos en la caja de texto donde nos pide las abreviaciones

    def traduccion(self):
        translator = Translator()
        texto = self.cajadetexto.get()
        destino = self.idioma()
        textotraducido = translator.translate(text=texto, dest=destino)
        self.etiqueta_resultado.config(text=textotraducido.text)
        ventanadelenguaje.historial.append((texto, destino, textotraducido.text))
        # este codigo traduce lo que pongamos y lo muestra, al mismo

    def leertexto(self):
        translator = Translator()
        texto = self.cajadetexto.get()
        destino = self.idioma()
        textotraducido = translator.translate(text=texto, dest=destino)
        textodetraduccion = self.text = textotraducido.text
        # hago lo mismo que hice antes para dejarlo como texto
        audio = gTTS(text=textodetraduccion, lang=destino, slow=False)
        audio.save('audio.mp3')
        os.system("start audio.mp3")
        # aca lo guardo al audio y lo ejecuto


if __name__ == "__main__":
    lenguajes = tkinter.Tk()
    ventanadelenguaje = VentanaLenguajes(lenguajes)
    traduccionsita = tkinter.Tk()
    translation_window = Ventanadetraduccion(traduccionsita)

    lenguajes.mainloop()
    traduccionsita.mainloop()

    # en esta parte muestro las ventanas
