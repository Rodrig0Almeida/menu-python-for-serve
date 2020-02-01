import datetime
import os
import cmd
import subprocess
from configparser import ConfigParser

tsh_version = "0.1.0"
TSH_CONFIG_PATH = str(os.path.join(os.path.expanduser("~"), ".config", "tsh"))
TSH_CONFIG_FILE = os.path.join(TSH_CONFIG_PATH, "config")
TSH_DOWNLOAD_PATH = {}


def tsh_create_config():
    if os.path.isdir(TSH_CONFIG_PATH):
        return True
    else:
        try:
            os.mkdir(TSH_CONFIG_PATH)
            return True
        except OSError:
            return False


def tsh_set_config(tsh_type, tsh_fullpath, tsh_label):
    config = ConfigParser()
    file = TSH_CONFIG_FILE
    if os.path.isfile(file):
        config.read(file)
        config.set(tsh_type, tsh_fullpath, tsh_label)
        with open(file, 'w') as data:
            config.write(data)
            data.flush()
            data.close()
    else:
        config.read(file)
        config.add_section(tsh_type)
        config.set(tsh_type, tsh_fullpath, tsh_label)
        with open(file, 'w') as data:
            config.write(data)
            data.flush()
            data.close()


def tsh_get_config(tsh_type, tsh_label):
    config = ConfigParser()
    config.read(TSH_CONFIG_FILE)
    return config.get(tsh_type, tsh_label)


class Console(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "tsh $ "
        self.doc_header = "Comandos documentados (digite: help TÓPICO)"

    def do_history(self, args):
        """
        Mostra o histórico de comandos
        """
        for item in self._hist:
            print("\t" + item)

    def do_exit(self, args):
        """
        Sai do console
        """
        return -1

    def do_clear(self, args):
        """
        Limpa a tela
        """
        os.system("cls||clear")

    def do_version(self, args):
        """
        Mostra a versão do tsh
        """
        print("version " + tsh_version)

    def do_shell(self, args):
        """
        Passa o comando para o shell do sistema quando a linha começar com '!'
        """
        os.system(args)

    def do_help(self, args):
        """
        Obtenha ajuda com os comandos
        'help' ou '?' sem nenhum argumento irá mostrar uma lista de comandos disponíveis.
        'help COMANDO' ou '? COMANDO' te mostra a ajuda de tal comando
        """
        cmd.Cmd.do_help(self, args)

    def do_add(self, args):
        """
        Adiciona um local para download do torrent
        exemplo:
        add PERFIL /local/para/pasta

        Você precisa adicionar o caminho completo para a pasta.
        O PERFIL pode ser qualquer um, contanto que não possua espaços.
        """
        arguments = args.split(" ")
        if len(arguments) >= 2:
            tsh_set_config('PATH', arguments[0], arguments[1])
        else:
            cmd.Cmd.do_help(self, "add")

    def do_download(self, args):
        """
        Download do torrent usando o perfil configurado
        exemplo:
        download PERFIL http://link.do.torrent
        """
        arguments = args.split(" ")
        arguments = list(filter(str.strip, arguments))
        if len(arguments) >= 2:
            if os.path.isfile(TSH_CONFIG_FILE):
                profile = arguments[0]
                profile_path = tsh_get_config("PATH", profile)
                torrent = arguments[1]
                process = subprocess.Popen(str('aria2c -d ' + profile_path + '--seed-time=0 --seed-ratio=0.0'
                                               + "'"+ torrent + "'"), shell=True, stderr=subprocess.STDOUT)
            else:
                print("Nenhuma configuração foi feita.\n\n\tUse o comando add para adicionar:")
                cmd.Cmd.do_help(self, "add")
        else:
            cmd.Cmd.do_help(self, "download")
            pass

    def preloop(self):
        cmd.Cmd.preloop(self)
        self._hist = []
        self._locals = {}
        self._globals = {}

    def postloop(self):
        cmd.Cmd.postloop(self)  ## Clean up command completion
        print("Saindo...")

    def precmd(self, line):
        current_time = datetime.datetime.now().strftime("%d/%b/%y %H:%M:%S ")
        if line.strip() != "":
            self._hist += [current_time + line.strip()]
        return line

    def postcmd(self, stop, line):
        return stop

    def emptyline(self):
        """Não faz nada quando receber um comanod vazio"""
        pass

    def default(self, line):
        """
         É chamado quando o input de uma linha não é reconhecido.
         Ele tenta executar como código Python.
        """
        try:
            exec(line) in self._locals, self._globals
        except Exception as e:
            print("tsh", ":", e)


if __name__ == '__main__':
    tsh_create_config()
    console = Console()
    console.cmdloop()
