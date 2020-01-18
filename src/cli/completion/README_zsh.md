# OpenLMI Shell Completion for Zsh
Supplied completion function defined in `_lmishell` supports completion of all
command line arguments of `lmishell`. The completion also works for script
filename completion with `.lmi` or `.py` extension.

## Setup
To use the completion, it is necessary to place `_lmishell` into `fpath`.

You need to modify your `zshrc`, so it contains following line:
```sh
autoload -U compinit && compinit
```
