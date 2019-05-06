autoload colors 
if [[ "$terminfo[colors]" -gt 8 ]]; then 
    colors 
fi 
for COLOR in RED GREEN YELLOW BLUE MAGENTA CYAN BLACK WHITE; do 
    eval $COLOR='$fg_no_bold[${(L)COLOR}]' 
    eval BOLD_$COLOR='$fg_bold[${(L)COLOR}]' 
done 
eval RESET='$reset_color' 

echo "${BOLD_CYAN}***Python Version***${NOCOLOR}"
python --version

uname -m 
cat /etc/*release
uname -a
 
 
### VI MODE #################################### 
echo ${MAGENTA}vi mode enabled${RESET} 

