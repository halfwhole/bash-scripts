# bash-scripts

Scripts that I use from time to time.

| Script                          | Description                                                                                                                             |
|:-------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:|
| `backup`                        | Backs up selected locations as specified in `backup-list.txt` to a backup directory `BACKUPS/` in an external hard drive using `rsync`. |
| `backup-dump`                   | Dumps the entire contents of the backup directory `BACKUPS/` in the external hard drive as a single ZIP file.                           |
| `backup-remote`                 | Backs up all important data in my remote server to a local directory `$HOME/Documents/remote-backups`.                                  |
| `extract <pdf>`                 | Takes in a PDF file of JPG images, and uses OCR to extract all the words into a single TXT file. Pirates may be interested in this one. |
| `soc-print <printer> [<file>]+` | Sends print jobs for selected files to a selected SoC printer over sunfire.                                                             |

## Setup

Clone this to your home directory, and add it to your path:

```sh
$ export PATH="$HOME/bash-scripts:$PATH"                 # (BASH) Add to ~/.bashrc
$ set -U fish_user_paths $fish_user_paths ~/bash-scripts # (FISH)
```
