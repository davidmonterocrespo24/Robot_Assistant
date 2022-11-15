# Instalacion del robot assistente

# Configuracion WI-Fi
Esta solución se aplica si acabas de flashear tu tarjeta SD y deseas habilitar Wi-Fi en tu sistema nuevo en el primer arranque (pero también funciona para una tarjeta SD antigua que hayas utilizado con Ethernet o una red inalámbrica antigua).

Tienes un archivo para crear y copiar en la tarjeta SD, así que en el próximo arranque Raspbian leerá el archivo y aplicará la configuración directamente.No tienes nada más que hacer.

wpa_supplicant.conf

Veamos cómo se hace:

Abre tu editor de texto favorito en tu ordenador
El editor básico de su sistema operativo estará bien (Notepad por ejemplo)
Copia y pegue estas líneas en él:
```
country=UY
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
 ssid="YOURSSID"
 scan_ssid=1
 psk="YOURPASSWORD"
 key_mgmt=WPA-PSK
}
```

Reemplaza las variables con tu SSID y contraseña, y cambia el valor del país si es necesario.
Guarda el archivo en una ubicación que puedas encontrar fácilmente la próxima vez que crees una nueva tarjeta SD.
Inserta tu tarjeta SD Raspbian en tu ordenador (para una nueva tarjeta SD creada con Etcher, tiene que expulsarla e insertarla de nuevo).
Luego copia el archivo wpa_supplicant.conf a la partición de arranque


# Configurar dispositivo de Sonido
```
sudo apt-get install libportaudio2
```
copiar el archivo ".asoundrc" a la carpeta root 
asi el usuario root puede encontrar el dispositivo de sonido


# Pantalla LCD via shell
```
sudo nano /boot/cmdline.txt
fbcon=map:10 fbcon=font:VGA8x8 
```


# RUN
Copiar el contenido de Prototipo2 y ejecutar el archivo main.py 
