class Televisao:
    def __init__(self,canal = None,volume = 5):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1

    def alterar_canal(self,canal):
        self.canal = canal

        
tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print(f'A tv está no canal {tv.canal}')             # A tv está no canal 5
print(f'A tv está no volume {tv.volume}')           # A tv está no volume 2


