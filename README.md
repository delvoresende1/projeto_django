sudo apt-get install libfuse2
cd /home/suporte/Downloads
#Baixe o Arquivo em clique aqui
sudo mv ExamLock-1.0.7.AppImage /usr/local/bin/examlock
sudo chown root:root /usr/local/bin/examlock
sudo chmod 755 /usr/local/bin/examlock
sudo nano /home/aluno/"Área de Trabalho"/examlock.desktop

[Desktop Entry]
Version=1.0
Type=Application
Name=ExamLock OBI
Exec=/usr/local/bin/examlock
Icon=system-run
Terminal=false
Categories=Education;

sudo chown aluno:aluno /home/aluno/"Área de Trabalho"/examlock.desktop
sudo chmod +x /home/aluno/"Área de Trabalho"/examlock.desktop

