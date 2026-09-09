.PHONY: check check-staged setup-hooks

check:
	python3 tools/check_repo.py --all

check-staged:
	python3 tools/check_repo.py --staged

setup-hooks:
	sh tools/install-git-hooks.sh
