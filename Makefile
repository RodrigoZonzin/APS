pushGit:
	git add .
	git commit -m "commit $(shell date +%Y-%m-%d) by $(USER)"
	git push