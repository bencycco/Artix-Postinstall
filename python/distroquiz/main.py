# Distro list
#Debian based
debian = [1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2]
devuan_runit = [2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1]
devuan_openrc = [5, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1]
devuan_sysvinit = [6, 1, 1, 1, 2, 2, 2, 1, 2, 1, 1]
lmde = [1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 6]
# Ubuntu based
ubuntu = [1, 2, 2, 1, 2, 4, 1, 1, 3, 6, 2]
xubuntu = [1, 2, 2, 1, 2, 4, 1, 1, 2, 6, 1]
kubuntu = [1, 2, 2, 1, 2, 4, 1, 1, 2, 6, 3]
lubuntu = [1, 2, 2, 1, 2, 4, 1, 1, 1, 6, 5]
lxle = [1, 2, 2, 1, 2 , 3, 1, 1, 1, 7, 4]
ubuntu_cinnamon = [1, 2, 2, 1, 2, 4, 1, 1, 2, 6, 6]
ubuntu_mate = [1, 2, 2, 1, 2, 4, 1, 1, 2, 6, 7]
kde_neon = [1, 1, 2, 1, 2, 4, 1, 1, 2, 6, 3]
mint_cinnamon = [1, 2, 2, 1, 2, 2, 2, 1, 2, 7, 6]
mint_mate = [1, 2, 2, 1, 2, 2, 2, 1, 2, 7, 7]
mint_xfce = [1, 2, 2, 1, 2, 2, 2, 1, 1, 7, 1]
peppermint = [1, 2, 2, 1, 2, 2, 2, 1, 1, 6, 1]
pop = [1, 2, 2, 1, 2, 4, 1, 1, 2, 6, 2]
zorin = [1, 2, 2, 1, 2, 3, 1, 2, 7, 1, 1]
mx = [1, 2, 2, 1, 2, 3, 1, 1, 2, 6, 1]
# Arch Based
arch = [1, 1, 1, 2, 1, 2, 3, 3, 1, 1, 0]
artix_runit = [2, 1, 1, 2, 3, 2, 3, 3, 1, 1, 0]
artix_s6 = [3, 1, 1, 2, 3, 2, 3, 3, 1, 1, 0]
artix_dinit = [4, 1, 1, 2, 3, 2, 3, 3, 1, 1, 0]
artix_openrc = [5, 1, 1, 2, 3, 2, 3, 3, 1, 1, 0]
endeavour = [1, 1, 2, 2, 2, 2, 1, 3, 2, 1, 0]
manjaro = [1, 2, 2, 2, 2, 3, 2, 3, 2, 7, 0]
arco = [1, 1, 2, 2, 2, 2, 3, 3, 1, 1, 0]
# Red Hat OS base
fedora = [1, 1, 2, 1, 1, 2, 3, 3, 2, 7, 0]
redhat = [1, 2, 1, 1, 2, 4, 1, 1, 3, 7, 2]
qubes = [1, 1, 2, 2, 3, 1, 3, 3, 1, 1, 0]
# openSUSE based
opensuse = [1, 2, 1, 1, 2, 3, 3, 3, 2, 1, 0]
# Gentoo based
gentoo = [5, 1, 1, 2, 1, 1, 3, 3, 1, 3, 0]
# Slackware based
slackware = [6, 1, 1, 1, 3, 2, 3, 3, 2, 7, 3]
# Other
nix = [1, 1, 1, 2, 3, 2, 2, 3, 1, 3, 0]
puppy = [1, 1, 1, 1, 3, 2, 3, 3, 1, 1, 0]
solus_gnome = [1, 2, 1, 2, 2, 3, 1, 1, 2, 1, 2]
solus_mate = [1, 2, 1, 2, 2, 3, 1, 1, 2, 1, 7]
solus_plasma = [1, 2, 1, 2, 2, 3, 1, 1, 2, 1, 3]
void = [2, 1, 1, 1, 3, 2, 3, 3, 1, 1, 1]

def main():
    # Question One
    q_one = int(input("""
        Choose an init system:
        1) systemd
        2) runit
        3) s6
        4) dinit
        5) OpenRC
        6) sysvinit
        > """))
    
    q_two = int(input("""
        Are you a power user?
        1) yes
        2) no
        > """))

    q_three = int(input("""
        Independant or Forked Distro?
        1) independant
        2) forked
        > """))
    
    q_four = int(input("""
        Stable or Cutting Edge?
        1) stable
        2) cutting edge
        > """))

    q_five = int(input("""
        Choose installation method:
        1) manual (like arch)
        2) calamares
        3) either
        > """))

    q_six = int(input("""
        Are you worried about privacy?
        1) Very much so
        2) I don't want to be tracked easily
        3) I don't mind
        4) What's privacy?
        > """))
    
    q_seven = int(input("""
        How do you want your system?
        1) Preconfigured
        2) Configure myself post-install
        3) Configure myself pre-install
        > """))

    q_eight = int(input("""
        DE or WM?
        1) DE
        2) WM
        3) Either
        > """))

    q_nine = int(input("""
        Bloatware:
        1) Minimal
        2) Don't care
        3) Windows 11
        > """))
    
    q_ten = int(input("""
        How do you install apps?
        1) Package Manager
        2) Git
        3) Source
        4) Snaps
        5) Appimages
        6) App Store
        7) Any
        > """))

    if q_eight == 1:
        q_eleven = int(input("""
            Default DE:
            1) XFCE
            2) GNOME
            3) KDE
            4) LXDE
            5) LXQt
            6) Cinnamon
            7) MATE
            > """))
    else:
        q_eleven = 0

        
    option = [q_one, q_two, q_three, q_four, q_five, q_six, q_seven, q_eight, q_nine, q_ten, q_eleven]
   
    debian_opt = 0
    devuan_runit_opt = 0
    devuan_openrc_opt = 0
    devuan_sysvinit_opt = 0
    lmde_opt = 0
    ubuntu_opt = 0
    xubuntu_opt = 0
    kubuntu_opt = 0
    lubuntu_opt = 0
    lxle_opt  = 0
    ubuntu_cinnamon_opt = 0
    ubuntu_mate_opt = 0
    kde_neon_opt = 0
    mint_cinnamon_opt = 0
    mint_mate_opt = 0
    mint_xfce_opt = 0
    peppermint_opt = 0
    pop_opt = 0
    zorin_opt = 0
    mx_opt = 0
    arch_opt = 0
    artix_runit_opt = 0
    artix_s6_opt = 0
    artix_openrc_opt = 0
    endeavour_opt = 0
    manjaro_opt = 0
    fedora_opt = 0
    redhat_opt = 0
    qubes_opt = 0
    opensuse_opt = 0
    gentoo_opt = 0
    nix_opt = 0
    puppy_opt = 0
    solus_gnome_opt = 0
    solus_mate_opt = 0
    solus_plasma_opt = 0
    void_opt = 0

    for i in range(11):
        if option[i] == debian[i]:
            debian_opt += 1
        if option[i] == devuan_runit[i]:
            devuan_runit_opt += 1
        if option[i] == devuan_openrc[i]:
            devuan_openrc_opt += 1
        if option[i] == devuan_sysvinit[i]:
            devuan_sysvinit_opt += 1
        if option[i] == lmde[i]:
            lmde_opt += 1
        if option[i] == ubuntu[i]:
            ubuntu_opt += 1
        if option[i] == xubuntu[i]:
            xubuntu_opt += 1
        if option[i] == kubuntu[i]:
            kubuntu_opt += 1
        if option[i] == lubuntu[i]:
            lubuntu_opt += 1
        if option[i] == lxle[i]:
            lxle_opt += 1
        if option[i] == ubuntu_cinnamon[i]:
            ubuntu_cinnamon_opt += 1
        if option[i] == ubuntu_mate[i]:
            ubuntu_mate_opt += 1
        if option[i] == kde_neon[i]:
            kde_neon_opt += 1
        if option[i] == mint_cinnamon[i]:
            mint_cinnamon_opt += 1
        if option[i] == mint_mate[i]:
            mint_mate_opt += 1
        if option[i] == mint_xfce[i]:
            mint_xfce_opt += 1
        if option[i] == peppermint[i]:
            peppermint_opt += 1
        if option[i] == pop[i]:
            pop_opt += 1
        if option[i] == zorin[i]:
            zorin_opt += 1
        if option[i] == mx[i]:
            mx_opt += 1
        if option[i] == arch[i]:
            arch_opt += 1
        if option[i] == artix_runit[i]:
            artix_runit_opt += 1
        if option[i] == artix_s6[i]:
            artix_s6_opt += 1
        if option[i] == artix_openrc[i]:
            artix_openrc_opt += 1
        if option[i] == endeavour[i]:
            endeavour_opt += 1
        if option[i] == manjaro[i]:
            manjaro_opt += 1
        if option[i] == fedora[i]:
            fedora_opt += 1
        if option[i] == redhat[i]:
            redhat_opt += 1
        if option[i] == qubes[i]:
            qubes_opt += 1
        if option[i] == opensuse[i]:
            opensuse_opt += 1
        if option[i] == gentoo[i]:
            gentoo_opt += 1
        if option[i] == nix[i]:
            nix_opt += 1
        if option[i] == puppy[i]:
            puppy_opt += 1
        if option[i] == solus_gnome[i]:
            solus_gnome_opt += 1
        if option[i] == solus_mate[i]:
            solus_mate_opt += 1
        if option[i] == solus_plasma[i]:
            solus_plasma_opt += 1
        if option[i] == void[i]:
            void_opt += 1

    distros = [(debian_opt, 'Debian'),
               (devuan_runit_opt, 'Devuan Runit'),
               (devuan_openrc_opt, 'Devuan OpenRC'),
               (devuan_sysvinit_opt, 'Devuan Sysvinit'), 
               (lmde_opt, 'Linux Mint Debian Edition'),
               (ubuntu_opt, 'Ubuntu'),
               (xubuntu_opt, 'Xubuntu'),
               (kubuntu_opt, 'Kubuntu'),
               (lubuntu_opt, 'Lubuntu'),
               (lxle_opt, 'LXLE'),
               (ubuntu_cinnamon_opt, 'Ubuntu Cinnamon'),
               (ubuntu_mate_opt, 'Ubuntu MATE'),
               (kde_neon_opt, 'KDE Neon'),
               (mint_cinnamon_opt, 'Linux Mint Cinnamon'),
               (mint_mate_opt, 'Linux Mint MATE'),
               (mint_xfce_opt, 'Linux Mint XFCE'),
               (peppermint_opt, 'Peppermint OS'),
               (pop_opt, 'Pop!_OS'),
               (zorin_opt, 'Zorin OS'),
               (mx_opt, 'MX Linux'),
               (arch_opt, 'Arch Linux'),
               (artix_runit_opt, 'Artix Linux Runit'),
               (artix_s6_opt, 'Artix Linux s6'),
               (artix_openrc_opt, 'Artix Linux OpenRC'),
               (endeavour_opt, 'Endeavour OS'),
               (manjaro_opt, 'Manjaro'),
               (fedora_opt, 'Fedora'),
               (redhat_opt, 'Red Hat Enterprise (what is wrong with you)'),
               (qubes_opt, 'QubesOS - Sigma'),
               (opensuse_opt, 'openSUSE'),
               (gentoo_opt, 'Gentoo (hella based mf)'),
               (nix_opt, 'NixOS'),
               (solus_gnome_opt, 'Solus Linux (GNOME desktop)'),
               (void_opt, 'Void Linux (absolutely correct and cool person)')
               ]
    sort_distros = sorted(distros, reverse=True)
    print(sort_distros)




main()
