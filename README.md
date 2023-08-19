# LofiGirlStudyMusic-Script
This is a simple bash and python script that plays the LofiGirlStudy livestream from youtube in the background using mpv --no-terminal
## How to run
- Put all the files in $HOME/.scripts/LofiGirlStudy
- Give executable permissions to the .sh files
- Add the following aliases to your .zshrc or .bashrc
  ```
  alias lofi="nohup ~/.scripts/LofiGirlStudy/LofiGirlStudyPlay.sh &"
  alias lofi_stop="~/.scripts/LofiGirlStudy/LofiGirlStudyKill.sh"
  ```
- Now you can run using the comand lofi and stop using lofi_stop
## Dependences
- mpv
- python3
- Python(Scrapetube)
- Python(re)
