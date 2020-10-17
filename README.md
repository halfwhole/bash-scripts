# bash-scripts

Scripts that I use from time to time.

| Script                          | Description                                                                                                                             |
|:-------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:|
| `backup`                        | Backs up selected locations as specified in `backup-list.txt` to a backup directory `BACKUPS/` in an external hard drive using `rsync`. |
| `backup-dump`                   | Dumps the entire contents of the backup directory `BACKUPS/` in the external hard drive as a single ZIP file. |
| `backup-remote`                 | Backs up all important data in my remote server to a local directory `$HOME/Documents/remote-backups`. |
| `declare-temp`                  | Declares my temperature on the NUS portal. It runs the main script from my `nus-temperature-declaration` project. |
| `extract <pdf>`                 | Takes in a PDF file of JPG images, and uses OCR to extract all the words into a single TXT file. Pirates may be interested in this one. |
| `fix-sound`                     | Runs `sudo alsa force-reload` to fix the sound issue in Ubuntu. I'm putting this into a script because I forget it far too often. |
| `kill-emacs`                    | Kills emacs, because it freezes way too often. Please fix :( |
| `luminus-download`              | Downloads files and folders from LumiNUS to my local directory. It runs the main script from my `luminus-downloader` project. |
| `soc-print <printer> [<file>]+` | Sends print jobs for selected files to a selected SoC printer over sunfire. |
| `2up <pdf>`                     | Converts a PDF file to 2-up in landscape format, with suffix `-2up`. |

## Setup

Clone this to your home directory, and add it to your path:

```sh
$ export PATH="$HOME/bash-scripts:$PATH"                 # (BASH) Add to ~/.bashrc
$ set -U fish_user_paths $fish_user_paths ~/bash-scripts # (FISH)
```
