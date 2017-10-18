#!/bin/bash
cut -f2 -d' ' $1 | sort | uniq | wc -l
