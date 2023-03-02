git_history:
	git log --pretty=format:"%h %ad %an %s" --stat

git_config:
	git config --list --show-origin