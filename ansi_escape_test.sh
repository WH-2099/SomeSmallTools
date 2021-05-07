#!/usr/bin/env bash
# MIT License
#
# Copyright (c) 2021 WH-2099
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

VERSION='0.3.0'

# 基础颜色测试
basic_color_test() {
    local test_string test_string
    local foreground=({{30..37},{90..97}})
    local background=({{40..47},{100..107}})

    while true; do
        read -p 'please input test string (at least 3 chars, default "ABC"): ' input_string
        test_string=${input_string:-'ABC'}
        if ((${#test_string} < 3)); then
            echo 'Invalid entry!'
        else
            break
        fi
    done

    printf '\n  Basic Color Test -- Foregound and Background: \e[92mESC[\e[91m#\e[92mm\e[m\n\n'
    printf '    '
    for b in "${background[@]}"; do
        # 设置前景色（字体颜色）为对应背景色
        printf "\e[%dm%${#test_string}d\e[m" $(($b - 10)) $b
    done
    printf '\n'
    for f in "${foreground[@]}"; do
        printf '  \e[%dm%-4d\e[m' $f $f
        for b in "${background[@]}"; do
            printf '\e[%d;%dm%s\e[m' $f $b $test_string
        done
        printf '\n'
    done
    printf '\n'
}

# rgb 颜色测试
rgb_color_test() {
    local rgb_color=({16..231})
    printf '  RGB Color Test -- Foreground: ESC[38;5;\e[96m#\e[mm  Background: ESC[48;5;\e[96m#\e[mm\n'
    printf '                     \e[96m#\e[m = 16 + 36 × \e[91mR\e[m + 6 × \e[92mG\e[m + \e[30;107mB\e[m (0 ≤ R, G, B ≤ 5)\n\n'
    for c in "${rgb_color[@]}"; do
        printf '\e[38;5;%dm%4d\e[m' $c $c
        if ((c % 24 == 15)); then
            printf '\n'
        fi
    done
    printf '\n'
}

# 灰度颜色测试
grayscale_color_test() {
    local grayscale_color=({232..255})
    printf '  Grayscale Color Test -- Foreground: ESC[38;5;\e[96m#\e[mm  Background: ESC[48;5;\e[96m#\e[mm\n\n'
    for c in "${grayscale_color[@]}"; do
        if (($c < 244)); then
            printf '\e[48;5;%dm%4d\e[m' $c $c
        else
            printf '\e[48;5;%d;30m%4d\e[m' $c $c
        fi
    done
    printf '\n\n'

}

# 效果测试
effect_test() {
    local effect=({0..9})
    printf '\n  Effect Test: \e[92mESC[\e[91m#\e[92mm\e[m\n\n'
    for e in "${effect[@]}"; do
        printf '  \e[%dm%d\e[m' $e $e
    done
    printf '\n\n'
}

# 字体测试
font_test() {
    local font=({{10..20},{50..55}})
    printf '\n  Font Test: \e[92mESC[\e[91m#\e[92mm\e[m\n\n'

    for f in "${font[@]}"; do
        printf '  %d:  \e[%dmABCabc123\e[m\n' $f $f
    done
    printf '\n'

}

# 光标相关测试
cursor_test() {
    # 考虑到部分终端可能不支持 Unicode 字符
    # 以 ASCII 内字符进行测试
    printf '\n  Cursor Test:\n'
    printf '              \e[92mESC[\e[91mA    \e[91m↑\e[m\n'
    printf '              \e[92mESC[\e[96mB    \e[96m↓\e[m\n'

    local up='\e[A'
    local down='\e[B'
    local clear='\b\b\b\b\b\b\b\b\b'
    for i in {0..10}; do
        printf '\n'
    done
    printf '      ◯ ◯'
    printf $up$clear'      /┯\'

    for i in {0..9}; do
        sleep 0.3
        printf $clear'      | |'
        printf $up$clear'      /┯\'
    done

    for i in {0..10}; do
        printf $down
    done
    printf '\n'
    
}

# 主流程
main() {
    printf '           \e[92mANSI Escape Code Support Test\e[m\n'
    printf '\e[96mplease select test mode (just entry the number):\e[m\n'
    select mode in color effect font cursor more_information quit; do
        case $mode in
        color)
            basic_color_test
            printf '\n\n'
            rgb_color_test
            printf '\n\n'
            grayscale_color_test
            ;;
        effect)
            effect_test
            ;;
        font)
            font_test
            ;;
        cursor)
            cursor_test
            ;;
        more_information)
            echo -e '\nhttps://en.wikipedia.org/wiki/ANSI_escape_code\n'
            ;;
        quit)
            exit 0
            ;;
        *)
            echo 'Invalid entry!'
            continue
            ;;
        esac
    done
}
main "$@"
