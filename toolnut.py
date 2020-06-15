import subprocess
import os


update_var = "sudo apt-get update ; sudo apt-get upgrade -y"
update_list = ["sudo apt-get update", "sudo apt-get upgrade -y"]


def run_command(cmd):
    subprocess.call(cmd, shell=True)


def run_commands(cmd: list):
    for i in range(len(cmd)):
        subprocess.call(cmd[i], shell=True)


def update_all():
    run_commands(update_list)


def option_list(opt):
    for i in range(len(opt)):
        print(str("[" + str(i + 1) + "] " + opt[i]))


def repo_install(repository, instl):
    commands = [str("sudo add-apt-repository -y " + repository), update_var, str("sudo apt-get install -y " + instl)]
    run_commands(commands)


func_opt = {}


def call_func(function_list, opt):
    function = function_list[opt - 1]
    function()
    run_again = input("Run script again?\n[y]Yes\n[n]No\n")
    if run_again == "y":
        run_command("clear")
        main_func()
    else:
        quit()


def logo():
    print("\n  ooooooooooo                         o888    oooo   oooo               o8   ")
    print("  88  888  88   ooooooo     ooooooo    888     8888o  88  oooo  oooo  o888oo ")
    print("      888     888     888 888     888  888     88 888o88   888   888   888   ")
    print("      888     888     888 888     888  888     88   8888   888   888   888   ")
    print("     o888o      88ooo88     88ooo88   o888o   o88o    88    888o88 8o   888o \n\n")


def free():
    run_command("free")


def shutdown():
    run_command("sudo shutdown")


def fast_apt():
    out = ""
    # out = subprocess.call("dpkg -s fast-apt", shell=True)
    try:
        out = subprocess.check_output("dpkg -s apt-fast", shell=True)
        out = out.decode()
        print(out)
    except:
        pass
    if "package 'fast-apt' is not installed" in out:
        subprocess.call("sudo add-apt-repository ppa:apt-fast/stable", shell=True)
        subprocess.call("sudo apt-get install apt-fast", shell=True)
    elif "Package: apt-fast" in out:
        print("jes")
    else:
        print("hmm")


def lst():
    direc = input("Enter a directory to list(leave empty to list current working directory):  ")
    if direc == "":
        print("Listing" + os.getcwd() + "\n")
    else:
        print("Listing" + direc + "\n")
    run_command(str("ls -a " + direc))


def optimize():
    run_command("sudo apt-get clean")
    run_command("sudo apt-get autoclean")
    run_command("sudo apt-get autoremove")


def software():
    func_opt = {}
    global terminal
    run_command("sudo apt-get install -y snapd")

    def tools():
        opt_list = ["Wine", "GRUB customizer", "Timeshift machine"]
        option_list(opt_list)
        choice = input("Select tool: ")
        if choice == "1":
            codename = input(
                "please enter your ubuntu version(if you are not sure, you can check with 'about host' option):  ")
            branch = input("\nselect branch:  [1]Stable\n [2]Developement\n [3]Staging\n")
            if codename == "20.04":
                codename = "focal"
            elif codename == "19.10":
                codename = "eoan"
            elif codename == "18.04":
                codename = "bionic"
            elif codename == "16.04":
                codename = "xenial"
            if branch == "1":
                branch = "stable"
            elif branch == "2":
                branch = "devel"
            elif branch == "3":
                branch = "staging"
            commands = ["sudo dpkg --add-architecture i386 ",
                        "wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -", str(
                    "sudo add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ " + codename + " main'"),
                        str("sudo apt install -y --install-recommends winehq-" + branch)]

            run_command(
                "sudo apt-get install -y libgnutls30:i386 libldap-2.4-2:i386 libgpg-error0:i386 libxml2:i386 libasound2-plugins:i386 libsdl2-2.0-0:i386 libfreetype6:i386 libdbus-1-3:i386 libsqlite3-0:i386")
            run_commands(commands)
        elif choice == "2":
            repo_install("ppa:danielrichter2007/grub-customizer", "grub-customizer")
        elif choice == "3":
            repo_install("ppa:teejee2008/ppa", "timeshift")

    def p_langs():
        print(" [1] Java")
        print(" [2] Python2")
        print(" [3] Php")
        print(" [4] Ruby")
        print(" [5] MySQL")
        choice = input("Select language: ")
        if choice == "1":
            subprocess.call("sudo apt-get install -y default-jdk", shell=True)
        elif choice == "2":
            run_command("sudo apt-get install -y python2")
        elif choice == "3":
            run_command("sudo apt-get install -y php libapache2-mod-php")
        elif choice == "4":
            run_command("sudo apt-get install -y ruby-full")
        elif choice == "5":
            run_command("sudo apt-get install -y mysql-server")
            secure = input("Would you like to secure your MySQL server\n[0]No\n[1]Yes\n:")
            if secure == "1":
                run_command("sudo mysql_secure_installation")

    def t_clients():
        opt_list = ["Deluge", "qBittorent", "Transmission"]
        option_list(opt_list)
        choice = input("Select Torrent client: ")
        if choice == "1":
            repo_install("ppa:deluge-team/ppa", "deluge")
        elif choice == "2":
            repo_install("ppa:qbittorrent-team/qbittorrent-stable", "qbittorrent")
        elif choice == "3":
            repo_install("ppa:transmissionbt/ppa",
                         "transmission-gtk transmission-cli transmission-common transmission-daemon")

    def cl_editors():
        opt_list = ["Vim", "Emacs", "Nano"]
        option_list(opt_list)
        choice = input("Select commandline editor: ")
        if choice == "1":
            repo_install("ppa:jonathonf/vim", "vim")
        elif choice == "2":
            repo_install("ppa:kelleyk/emacs", "emacs25")
        elif choice == "3":
            repo_install("ppa:n-muench/programs-ppa", "nano")

    def d_manager():
        opt_list = ["Aria2", "uGet", "XDM"]
        option_list(opt_list)
        choice = input("Select Download Manager: ")
        if choice == "1":
            run_command("sudo apt-get install -y aria2")
        elif choice == "2":
            repo_install("ppa:plushuang-tw/uget-stable", "uget")
        elif choice == "3":
            repo_install("ppa:noobslab/apps", "xdman")

    def email_clients():
        opt_list = ["Thunderbird", "Geary", "Evolution"]
        option_list(opt_list)
        choice = input("Select Email Client: ")
        if choice == "1":
            run_command("sudo apt-get install -y aria2")
        elif choice == "2":
            repo_install("ppa:geary-team/releases", "geary")
        elif choice == "3":
            repo_install("ppa:gnome3-team/gnome3-staging", "evolution")

    def IDE():
        opt_list = ["IntelliJ IDEA", "Brackets", "Netbeans IDE", "Atom IDE", "Light Table", "Visual Studio Code"]
        option_list(opt_list)
        choice = input("Select IDE Editor: ")
        if choice == "1":
            run_command("sudo snap install intellij-idea-community --classic")
        elif choice == "2":
            run_command("sudo snap install netbeans --classic")
        elif choice == "3":
            repo_install("ppa:webupd8team/brackets", "brackets")
        elif choice == "4":
            run_command("sudo snap install atom --classic")
        elif choice == "5":
            repo_install("ppa:dr-akulavich/lighttable", "lighttable-installer")
        elif choice == "6":
            commands = ["wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -"
                , "sudo add-apt-repository \"deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main\""
                , update_var, "sudo apt-get install -y code"]
            run_commands(commands)

    def instant_msg():
        opt_list = ["Skype", "Pidgin", "Empathy"]
        option_list(opt_list)
        choice = input("Select Instant Mesagge app: ")
        if choice == "1":
            run_command("sudo snap install skype --classic")
        elif choice == "2":
            repo_install("ppa:geary-team/releases", "geary")
        elif choice == "3":
            run_command("sudo apt-get install -y empathy")

    def d_env():
        opt_list = ["Cinnamon", "Mate", "GNOME", "KDE", "LXQT"]
        option_list(opt_list)
        choice = input("Select Desktop Environment: ")
        if choice == "1":
            repo_install("ppa:embrosyn/cinnamon", "cinnamon-desktop-environment lightdm")
        elif choice == "5":
            run_command("sudo apt-get install -y lxqt sddm")
        else:
            run_command("sudo apt install tasksel")
            de = ""
            if choice == "2":
                de = "ubuntu-mate-desktop"
            elif choice == "3":
                de = "ubuntu-desktop"
            elif choice == "4":
                de = "kubuntu-desktop"
            run_commands(["sudo apt install -y tasksel", str("sudo tasksel install " + de)])

    def m_tools():
        opt_list = ["GNOME Tweak Tool", "Stacer"]
        option_list(opt_list)
        choice = input("Select maintenance Tool: ")
        if choice == "1":
            run_command("sudo apt-get install -y gnome-tweak-tool")
        elif choice == "2":
            repo_install("ppa:oguzhaninan/stacer", "stacer")

    def terminals():
        global terminal
        opt_list = ["GNOME Terminal", "Konsole", "Terminator", "Guake", "Terminology"]
        option_list(opt_list)
        choice = input("Select Terminal: ")
        if choice == "5":
            #run_command("wget -P $HOME/Downloads https://download.enlightenment.org/rel/apps/terminology/terminology-1.7.0.tar.xz")
            print("feature is coming...")
        else:
            if choice == "1":
                terminal = "gnome-terminal"
            elif choice == "2":
                terminal = "konsole"
            elif choice == "3":
                terminal = "terminator"
            elif choice == "4":
                terminal = "guake"
            run_command(str("sudo apt-get install -y " + terminal))


    opt_list = ["Tools", "Programming languages", "Torrent Clients", "Commandline Editors", "Download Manager",
                "Email Clients", "IDE Editors", "Instant Messaging", "Desktop Environments", "Maintenance Tools",
                "Terminals"]
    option_list(opt_list)
    category = input("\n Select category: ")
    func_list = [tools, p_langs, t_clients, cl_editors, d_manager, email_clients, IDE, instant_msg, d_env, m_tools,
                 terminals]
    call_func(func_list, int(category))


def about_os():
    run_command("cat /etc/os-release")


def about_host():
    run_command("hostnamectl")


def main_func():
    logo()
    main_opt_list = ["Update", "Display amount of free and used memory in the system", "Shutdown",
                     "Fast apt - shellscript wrapper for apt-get or aptitude to speed up installing packages",
                     "List directory contents", "Clear unnecessary junk", "Install software", "About OS release",
                     "About host"]
    option_list(main_opt_list)
    func_list = [update_all, free, shutdown, fast_apt, lst, optimize, software, about_os, about_host]
    option = int(input("\nPlease choose an option:  "))
    call_func(func_list, option)


main_func()
