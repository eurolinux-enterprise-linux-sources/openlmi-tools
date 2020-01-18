#
# Copyright (C) 2013 Red Hat, Inc.  All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Authors: Roman Rakus <rrakus@redhat.com>
#
# Bash completion for LMI Shell


_lmishell() {
    oldifs=$IFS
    IFS=$'\n'
    local options=(-h -i -v -m -q -n --help --interact --verbose --more-verbose --quiet --noverify)
    local current="${COMP_WORDS[$COMP_CWORD]}"
    local hasfile=no
    for (( i=1; i < ${#COMP_WORDS[@]} - 1; i++ )); do
        [[ ${COMP_WORDS[$i]} != -* && ${COMP_WORDS[$i]} ]] && hasfile=yes
    done
    if [[ $hasfile == no ]]; then
        if [[ $current =~ ^- ]]; then
            COMPREPLY=( $(compgen "-W ${options[*]}" -- "$current" ) )
        else
            COMPREPLY=( $(compgen -f -o plusdirs -X '!*.lmi' -- "$current") )
            COMPREPLY+=( $(compgen -f -X '!*.py' -- "$current") )
        fi
    fi
    # for directories add slash
    # for others add space
    for (( i=0; i < ${#COMPREPLY[@]}; i++ )); do
        # using printf %q because we need to escape nonprintable chars
        if [[ -d ${COMPREPLY[$i]} ]]; then
            COMPREPLY[$i]=$(printf '%q/' "${COMPREPLY[$i]}")
        else
            COMPREPLY[$i]=$(printf '%q ' "${COMPREPLY[$i]}")
        fi
    done
    IFS=$oldifs
}

# nospace because of directories
# for dirs it will add /
# for others it will add space manually
complete -o nospace -F _lmishell lmishell
