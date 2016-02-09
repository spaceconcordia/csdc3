export TERM=xterm-256color

alias ..='cd ..'
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias apt-get='sudo apt-get'
alias py='python'

# some more ls aliases
alias ll='ls -alFh'
alias la='ls -A'
alias l='ls -CF'

# Git related
alias gs='git status'
alias gc='git commit'
alias ga='git add'
alias gd='git diff'
alias gb='git branch'
alias gl='git log'
alias gsb='git show-branch'
alias gco='git checkout'
alias gg='git grep'
alias gk='gitk --all'
alias gr='git rebase'
alias gri='git rebase --interactive'
alias gcp='git cherry-pick'
alias grm='git rm'
alias calc='bc'
alias woo='fortune'
alias diskspace="du -S | sort -n -r | more"

extract () {
   if [ -f $1 ] ; then
       case $1 in
           *.tar.bz2)   tar xvjf $1    ;;
           *.tar.bz)    tar xvjf $1    ;;
           *.tar.gz)    tar xvzf $1    ;;
           *.bz2)       bunzip2 $1     ;;
           *.rar)       unrar x $1     ;;
           *.gz)        gunzip $1      ;;
           *.tar)       tar xvf $1     ;;
           *.tbz2)      tar xvjf $1    ;;
           *.tgz)       tar xvzf $1    ;;
           *.zip)       unzip $1       ;;
           *.Z)         uncompress $1  ;;
           *.7z)        7z x $1        ;;
           *)           echo "don't know how to extract '$1'..." ;;
       esac
   else
       echo "'$1' is not a valid file!"
   fi
 }

function compress()  # create .tar.gz archive
{
    tar -cvzf $1 $2
}
# Use: compress archive.tar.gz dirname/

function __setprompt {
  local BLUE="\[\033[0;34m\]"
  local NO_COLOUR="\[\033[0m\]"
  local SSH_IP=`echo $SSH_CLIENT | awk '{ print $1 }'`
  local SSH2_IP=`echo $SSH2_CLIENT | awk '{ print $1 }'`
  if [ $SSH2_IP ] || [ $SSH_IP ] ; then
    local SSH_FLAG="@\h"
  fi
  PS1="$BLUE[\$(date +%H:%M)][\u$SSH_FLAG:\w]\$(__git_ps1)\$ $NO_COLOUR"
#  PS1="$BLUE[\$(date +%H:%M)][\u$SSH_FLAG:\w]\\$ $NO_COLOUR"
  PS2="$BLUE>$NO_COLOUR "
  PS4='$BLUE+$NO_COLOUR '
}
#__setprompt

#netinfo - shows network information for your system
netinfo ()
{
echo "--------------- Network Information ---------------"
/sbin/ifconfig | awk /'inet addr/ {print $2}'
/sbin/ifconfig | awk /'Bcast/ {print $3}'
/sbin/ifconfig | awk /'inet addr/ {print $4}'
/sbin/ifconfig | awk /'HWaddr/ {print $4,$5}'
myip=`lynx -dump -hiddenlinks=ignore -nolist http://checkip.dyndns.org:8245/ | sed '/^$/d; s/^[ ]*//g; s/[ ]*$//g' `
echo "${myip}"
echo "---------------------------------------------------"
}

#dirsize - finds directory sizes and lists them for the current directory
dirsize ()
{
du -shx * .[a-zA-Z0-9_]* 2> /dev/null | \
egrep '^ *[0-9.]*[MG]' | sort -n > /tmp/list
egrep '^ *[0-9.]*M' /tmp/list
egrep '^ *[0-9.]*G' /tmp/list
rm -rf /tmp/list
}

#copy and go to dir
cpg (){
  if [ -d "$2" ];then
    cp $1 $2 && cd $2
  else
    cp $1 $2
  fi
}

#move and go to dir
mvg (){
  if [ -d "$2" ];then
    mv $1 $2 && cd $2
  else
    mv $1 $2
  fi
}
