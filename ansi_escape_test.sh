#!/bin/bash

author='WH-2099'
version='beta'

color_test() {
    local foregrounds=$(echo {{30..37},{90..97}})
    local backgrounds=$(echo {{40..47},{100..107}})

    echo -n '    '
    for b in $backgrounds; do
        if [[ ${#b} < 3 ]]; then
            space=' '
        else
            space=''
        fi
        # 设置前景色（字体颜色）为对应背景色
        echo -ne "\e[$((${b} - 10))m$b$space\e[m"
    done
    echo

    for f in $foregrounds; do
        echo -ne "\e[${f}m${f}  \e[m"
        for b in $backgrounds; do
            echo -ne "\e[${f};${b}mABC\e[m"
        done
        echo
    done
}

type_test() {
    local types=$(echo {{},{}})

}

font_test() {
    local types=$(echo {{},{}}) 
}

main() {
    echo -e "           \e[92mANSI escape code support test\e[m"
    echo -e '\e[96mplease select test mode (just entry the number):\e[m'
    select mode in color type font move quit; do
        case $mode in
        color)
            color_test
            ;;
        type)
            type_test
            ;;
        quit)
            exit 0
            ;;
        *)
            echo 'Invalid entry.'
            continue
            ;;
        esac
    done
}
main
