# recents
Conveniently store and fetch recent files

## Installation
```bash
cd
touch recents.txt
echo >> recents.txt
git clone git@github.com:ajgateno/recents.git
echo "alias recents=\"python3 ~/recents/recents.py\"" >> ~/.bashrc
source ~/.bashrc
cd -
```

## Usage
```bash
recents [LINE_NUMBER]
```

- Leaving out the line number prints all recents
- Including a line number fetches that recent
- Inputting an invalid line number should return an empty line
