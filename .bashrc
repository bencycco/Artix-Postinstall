#
#  bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='[\u@\h:[\w]]∝ '

alias ..='cd ..'
alias ...='cd ../..'
alias cp='cp -i'

mick {
     mkdir -p "$@"
     cd "$@"
}

alias rmd='rm -rf -i'
alias rr='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'
. "$HOME/.cargo/env"

alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
alias brba="sh ~/BrBa/main.sh"

chemproj () {
        mkdir -p "$@"
        cd "$@"
        touch proceedure.txt
        touch materials.txt
}
