import pygame
import pygame
import glob
import os
import time
first = True

SIZE = WIDTH, HEIGHT = 480, 320  # the width and height of our screen
FPS = 15 # Frames per second
first = True
current_emotion = 0
previous_emotion = 0

emotions =  [   ["Normal"], 
                ["Feliz", "bien","feliz","alegre","contento","encantado","extasiado","eufórico","contento","alegre","alegría","jubiloso","animado" ,  "lleno de alegría", "pacífico", "agradable", "complacido", "emocionado", "optimista", "bendecido", "dichoso",  "no me puedo quejar", "cautivado", "contento", "agradable", "exultante", "volando alto",  "gratificado", "intoxicado", " riendo", "ligero", "bien visto", "en la nube nueve", "animado"],
                ["Triste", "decepcionado", "disgustado","peor", "amargo", "desconsolado", "melancolía", "triste", "pesimista", "sombrío",  "perdón", "melancólico", "desconsolado" ,"azul","triste","desanimado","desesperado","desanimado","desconsolado","triste","triste","abajo","abajo","abajo","boca abajo"," abatido","desamparado","sombrío","sombrío","doloroso","afligido","descorazonado","pesado","dolido","de capa caída","en pena","en los vertederos ","languideciendo","bajo","malhumorado","lúgubre","morboso","malhumorado","malhumorado","pensativo","enfermo","perturbado","lloroso" ,"desconsolado",
                "abatido", "abatido", "desanimado", "desanimado", "desconsolado", "desanimado", "caído", "abatido", "deprimido", "decepcionado", "descorazonado", "desanimado", "desmoralizado", "aplastado", "desolado", "desconsolado", "desconsolado", "con el corazón apesadumbrado", "decaído", "de capa caída", "triste", " infeliz", "triste", "melancólico", "miserable", "afligido", "desamparado", "cara alargada", "harto", "miserable", "sombrío", "sombrío", "lúgubre", "avergonzado", "ahorcado"],
                ["Enojado", "Furioso","nunca", "peor", "enojado", "molesto", "amargo", "enfurecido", "exasperado", "furioso", "acalorado", "apasionado", "indignado", "furioso" , "irritado", "irritado", "ofendido", "indignado", "resentido", "malhumorado", "tenso", "ofendido", "antagonizado", "irritado", "colérico", "convulsionado", " cruz", "disgustado", "exacerbado", "feroz", "feroz", "ardiente", "furioso", "irritado", "odioso", "caliente", "enfadado", "malhumorado", " indignado", "inflamado", "enfurecido", "irascible", "irascible", "enloquecido", "irritado", "picado", "provocado", "rabioso", "irritado", "dolorido", "esplenético" , "tormenta", "malhumorado", "turbulento", "turbulento"],
                ["Asustado", "miedo","deprimido", "desanimado", "malhumorado", "pesimista", "triste", "infeliz", "sangrado", "azul", "abatido", "destruido", "desanimado", "abajo" , "arrastrado", "dolido", "bajo", "arrancado", "llorando", "malo", "desanimado", "abatido", "caído", "malhumorado", "desconsolado", "abajo y fuera", "abajo en los vertederos", "abajo en la boca", "abatido", "desanimado", "harto", "sombrío", "sombrío", "en un funk azul", "en dolor" , "en los vertederos", "en los pozos", "en el baño", "decepcionado", "bajo-abajo", "bajo-espíritu", "lúgubre", "melancólico", "malhumorado", "en una decepción", "historia de sollozos", "sin espíritu", "derribado", "destrozado", "desgraciado"],
                ["Really"],
                ["Sorprendido", "Exitado", "emocionado"],   
                ["Amor","dulce", "hermoso", "caliente", "enfermo de amor", "coqueto", "cariño", "admiro", "adorable", "cariño", "amor", "ángel", "increíble" , "atracción", "bebé", "bebé", "miel", "linda", "linda", "linda", "cuidado", "encantador", "cupido", "elegante", "novia", " novio", "San Valentín", "hermoso", "magdalena", "travieso", "pasión", "reina", "descarado", "seductor", "cariño", "unqiue", "cálido"] ,
                ["Bullying","gordo", "nerd", "feo", "zorra", "fenómeno", "idiota", "a nadie le gustas", "suicidate", "vete a morir", "deseo que mueras", "violación", "pornografía", "acecho", "asesinato", "violación", "amenaza", "asalto", "secuestro", "secuestro", "hurto en tiendas" , "robo", "bastardo", "hijo de puta", "gordo", "gay", "molesto", "racista", "perra", "muerto", "noob", "pequeño", "pequeño", "falso", "perdedor ", "joder", "más feo", "tonto", "estúpido", "perdedores", "diablos", "cirugía", "basura", "pinchazo", "culo", "trasero", "coño", "mierda", "mierda", "polla", "maldita", "pelusa", "cosas", "joder"],
                ["Disparar","disparo","dispara""arma","bala","matar", "asesinato","pistola"] ,       
            ]




class MySprite(pygame.sprite.Sprite):

    expression_index = {}

    def __init__(self):
        super(MySprite, self).__init__()
        f_imagenes = []
        expression = ['Enojado', 'Normal', 'Muerto', 'Asustado', 'Feliz',
                      'Triste', 'Sorprendido', 'Guino', 'Really', 'Amor', 'Disparar']
        self.images = []
        index = 0
        for i in range(0, len(expression)):
            archivos = os.listdir(os.path.join(
                os.getcwd(), 'Eyes', expression[i]))
            #print("Cargando archivos..............:"+str(os.path.join(os.getcwd(),'Eyes',expression[i])))
            arch = []
            for k in range(0, len(archivos)):
                arch.append(archivos[k])
                print("Cargando archivos..............:" +
                      str(str(k+1)+archivos[k]))
            f_imagenes.append(arch)
            index_array = []
            for j in range(0, len(f_imagenes[i])):
                index_array.append(index)
                index = index+1
                ima = os.path.join(os.path.join(
                    os.getcwd(), 'Eyes', expression[i], f_imagenes[i][j]))
                self.images.append(pygame.transform.scale(
                    pygame.image.load(ima), (480, 320)))
            self.expression_index.update({expression[i]: index_array})
        self.index = 0
        self.state = 'Normal'
        self.rect = pygame.Rect(5, 5, 150, 198)
        print(self.expression_index)


    def update(self,):
        print("Update..."+self.state)
        self.animation(self.expression_index[self.state])

    def animation(self, index_image):        
        if self.index >= index_image[len(index_image)-1]:
            self.index = index_image[len(index_image)-1]
        if self.index < index_image[0]:
           self.index = index_image[0]
        self.image = self.images[self.index]
        self.index += 1
        
    def set_state(self,state):
        self.state=state
        self.index=0

class Animation ():

    def __init__(self, startEmotion):
        current_emotion = startEmotion
        previous_emotion = startEmotion
        pygame.init()
        screen = pygame.display.set_mode((480, 320))
        pygame.display.set_caption("Trace")
        self.my_sprite = MySprite()
        self.my_group = pygame.sprite.Group(self.my_sprite)
        #screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
        self.screen = screen
        self.clock = pygame.time.Clock()

    def run(self):
        global first
        global current_emotion
        global previous_emotion
        loop = 1
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE or event.type == pygame.K_LCTRL :
                    loop = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    current_emotion = current_emotion+1
            if first:
                first = False
                
            else:
                print("RUN------current_emotion----"+str(emotions[current_emotion][0])+"--------------"+str(
                    emotions[previous_emotion][0])+"--previous_emotion------")
                if current_emotion != previous_emotion:
                    print("Emociones------------------------------------" +
                          emotions[previous_emotion][0])
                    previous_emotion = current_emotion
                    self.my_sprite.set_state(emotions[current_emotion][0])

            self.my_group.update()
            self.screen.fill((0, 0, 0))
            self.my_group.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()
        quit()


def set_emotion(str):
    splits = str.split()
    for split in splits:
        for i in range(len(emotions)):
            for j in range(len(emotions[i])):
                if split.upper() == emotions[i][j].upper():
                    return i
    return 1


a = Animation(1)
a.run()