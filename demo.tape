# brewfyi — Python Coffee Encyclopedia Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set Padding 20

Type `curl -s 'https://brewfyi.com/api/search/?q=espresso' | jq '.results[:3][] | {name, type}'`
Enter
Sleep 3s

Type `curl -s 'https://brewfyi.com/api/method/pour-over/' | jq '{name, category}'`
Enter
Sleep 3s

Type `curl -s 'https://brewfyi.com/api/random/' | jq '{name, type}'`
Enter
Sleep 3s

Sleep 2s
