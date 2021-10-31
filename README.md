# Integração Extreme EXOS com Python

Os códigos desenvolvidos servem para automatizar processos usando o interpetrador python presente nos switches que rodam o SO EXOS.

autoVlan:</br>
&nbsp; Script desenvolvido para adicionar e remover um dispositivo de uma VLAN, com base nos eventos de detecção e não detecção de dispositivos.</br></br>

&nbsp; O código é rodado quando o perfil UPM criado é executado. Adicione o seguinte comando na primeira linha do perfil UPM</br>
&nbsp; create upm profile PROFILENAME</br>
&nbsp; run script autoVlan.py $(EVENT.TYPE) $(EVENT.USER_PORT) $(EVENT.USER_MAC)</br>
