import subprocess
import os

def send_folder(container_id,folder_path,container_path):
    
    #Verifica a existência do container
    container_exists = subprocess.run(['docker','inspect', container_id], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    if container_exists.returncode != 0:
        print(f"Container {container_id} não encontrado.")
        return
    
    #Verifica se a pasta existe
    if not os.path.exists(folder_path):
        print(f"Caminho da pasta local '{folder_path}' não existe.")
        return
    
    #Converte o caminho da pasta local para o formato do caminho do docker (barras invertidas)
    folder_path_docker_format = folder_path.replace("\\","\\\\")
    
    #Monta o comando para o envio da pasta para o container
    command = ["docker","cp", folder_path_docker_format, f"{container_id}:{container_path}"]
    try:
        subprocess.run(command,check=True)
        print(f"Pasta enviada com sucesso par ao container: {container_id}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao enviar a pasta para o container: {e}")
        return
#Envio
if __name__ == "__main__":
    container_id = ""
    folder_path = ""
    container_path = ''
    
    send_folder(container_id,folder_path,container_path)