#!/bin/bash
cut -f2 -d' ' $1 | uniq | wc -l
