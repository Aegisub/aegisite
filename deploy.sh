#!/bin/sh

set -e

middleman build
rsync -ae ssh build/docs/ www-write@aegisub.org:/var/www/docs.aegisub.org/
rsync -ae ssh build/www/ www-write@aegisub.org:/var/www/www.aegisub.org/
rsync -ae ssh build/static/ www-write@aegisub.org:/var/www/static.aegisub.org/
