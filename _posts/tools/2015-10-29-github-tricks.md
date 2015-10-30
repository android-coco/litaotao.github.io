---
category: tools
published: false
layout: post
title: github 的一些小技巧
description: github 的一些小技巧
---


##
## 1. 更改分支名字  

```
git branch -m old_branch new_branch         # Rename branch locally    
git push origin :old_branch                 # Delete the old branch    
git push --set-upstream origin new_branch   # Push the new branch, set local branch to track the new remote
```
