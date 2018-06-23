#!/bin/bash
a=1 
# 1 
a=$((a+1))
echo $a
# 1.1 
a=$[a+1]
echo $a
# 2
let a+=1
echo $a

