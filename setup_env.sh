#!/usr/bin/env bash

brew install lilypond
brew install fluid-synth
pipenv --python 3.11
pipenv install

echo "Testing setup"
pipenv run python -c "\
from scamp import test_run
test_run.play(show_lilypond=True)
"
