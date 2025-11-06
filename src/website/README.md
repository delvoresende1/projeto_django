Projeto Django

Python e bootstrap

pip install django

pip install django-bootstrap5
pip install django-bootstrap-v5

atualizar repositorio local : 
git status   : verifique em qual branch você está  
git pull origin main  : atualize o repositório local  - certifique-se de estar na branch principal que deseja sincronizar e execute: git pull origin main  # main é o nome padrão da branch
ou somente: git pull

após alterações: 
1. git status : verificar status mostra quais arquvios foram modificados, quais são novos e quais estão prontos para serem      encaminhados para serem commitados - é útil para verificar se os arquivos estão corretos
2. git add . (ou git add [nome do arquivo]) : adicionar alterações para o 'staging area' - área de preparação - relacione arquivos que foram modificados para incluir no commit
2.1. git add nome_do_arquvio.extensão
3. git commit -m "mensagem descritiva" - descreva de forma resumida as alterações propostas - salva as alterações localmente na sua máquina. Para atualizar o repositório remoto, 'push' empurrar os commits no próximo passo
4. git push origin main (envia alterações ao repositório remoto)
5. origin é o nome padrão do seu controle remoto
6. main (ou master, develop) é o nome da branch para a qual você está enviando as alterações


