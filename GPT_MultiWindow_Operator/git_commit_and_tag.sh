#!/bin/bash
cd "$(dirname "$0")"

git init
git add .
git commit -m "🚀 Initial commit: MultiWindow GPT Production Suite v1.0"
git tag v1.0

echo "✅ Git repo initialized, committed, and tagged as v1.0"
