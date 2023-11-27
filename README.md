# VisaoComp
Repositório de codigos e documentos para a disciplina de IOT e visao computacional. Código exemplo para controlar um carro com esp32 Cam e 2 servos endless e um display oled. O controle é feito pelo envio de requisições http do tipo get

Stream de video
http://yyy.yyy.yyy.yyy:81 


Servo parado
http://yyy.yyy.yyy.yyy/on?R=95
http://yyy.yyy.yyy.yyy/on?L=95

para acionar o servo: colocar um valor entre 0 e 180 tanto para o da esquerda quanto o da direita. valores abaixo de 95 roda em um sentido e acima no oposto.

Veja o codigo em py para entender o controle.

