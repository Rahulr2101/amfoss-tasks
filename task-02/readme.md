part1
cat>part1.txt
mv 1.txt ../solution
mv 1.txt part2.txt
git add -A
git log
git commit
git branch -a
git checkout asia
find . -name athens.txt
git checkout main
git merge asia
mv athens.txt ../../solution/part4.txt
cat part1.txt part2.txt part3.txt part4.txt>password.txt
rm part1.txt part2.txt part3.txt part4.txt
cat password.txt

