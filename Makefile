documentation:
	jb clean docs
	jb build docs
	python policyengine-test/tools/add_plotly_to_book.py docs/_build
