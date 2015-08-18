## Git commands for git hub beginners
###Step 1
Git configuration 
```
git config --global user.name = "<username>"
git config --global useer.email ="<email address>"
git config --list
```
###Step 2
Create a file or have a file ready to add you can create a file with touch command and insert data with echo command.>> use this for append the exiting file.
```
echo "hi test file " > file.md
```
Check git status after performing above task.
```
git status
```
###Step 3
Adding new files command
```
git add . #It will do both task aswritten below.
git add -u #It will update current file.
git add -A #It will update all.
```
###Step 4
Commiting to the repository. 
```
git commit -m "any message"
```
Check git status again.

###Step 5
Define remote origin.
```
git remote add origin <url>.git
```
After step 5 ,Push the documents to remote origins.
###Step 6
Pushing command
```
git push -u origin master
```
