#!/bin/bash

string="01234"
echo 'El largo es '${#string}
b=${string:1:${#string}}
echo $b