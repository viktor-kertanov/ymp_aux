history:
	git log --pretty=format:"%h %ad %an %s" --stat

git_config:
	git config --list --show-origin

git_previous:
	git reset --soft HEAD~1